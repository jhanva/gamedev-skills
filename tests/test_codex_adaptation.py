import json
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOK_SCRIPT = ROOT / ".codex" / "hooks" / "codex_hooks.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def run_hook(action: str, payload: dict) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(HOOK_SCRIPT), action],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        cwd=ROOT,
        check=False,
    )


class CodexConfigTests(unittest.TestCase):
    def test_project_config_contains_only_real_agent_settings(self) -> None:
        config = tomllib.loads(read(".codex/config.toml"))

        self.assertEqual({"max_threads", "max_depth"}, set(config["agents"]))
        self.assertTrue(config["features"]["hooks"])

    def test_custom_agents_have_required_codex_fields(self) -> None:
        for path in sorted((ROOT / ".codex" / "agents").glob("*.toml")):
            with self.subTest(path=path.name):
                agent = tomllib.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(agent.get("name"))
                self.assertTrue(agent.get("description"))
                self.assertTrue(agent.get("developer_instructions"))

    def test_gamedev_agents_do_not_implicitly_run_user_skills(self) -> None:
        playbooks = [
            "game-designer/playbook.md",
            "level-designer/playbook.md",
            "pixel-artist/playbook.md",
            "producer/playbook.md",
            "qa-analyst/playbook.md",
            "sound-designer/playbook.md",
        ]
        for relative in playbooks:
            with self.subTest(playbook=relative):
                content = read(f".codex/agents/{relative}")
                self.assertIn("Las skills las invoca el usuario", content)

    def test_hooks_are_registered_with_cross_platform_commands(self) -> None:
        hooks = json.loads(read(".codex/hooks.json"))["hooks"]

        self.assertIn("SessionStart", hooks)
        self.assertIn("PreToolUse", hooks)
        self.assertIn("PostToolUse", hooks)
        handlers = [
            handler
            for groups in hooks.values()
            for group in groups
            for handler in group["hooks"]
        ]
        self.assertTrue(all("command" in handler for handler in handlers))
        self.assertTrue(all("commandWindows" in handler for handler in handlers))

    def test_model_bump_helper_only_updates_standalone_agent_files(self) -> None:
        helper = read("scripts/bump-codex-model.sh")

        self.assertNotIn("[agents.models]", helper)
        self.assertNotIn("Update .codex/config.toml", helper)
        self.assertIn("python", helper)


class CodexHookTests(unittest.TestCase):
    def test_pre_tool_policy_blocks_env_but_allows_template(self) -> None:
        blocked = run_hook(
            "pre-tool-policy",
            {"tool_name": "Bash", "tool_input": {"command": "Get-Content .env"}},
        )
        allowed = run_hook(
            "pre-tool-policy",
            {"tool_name": "Bash", "tool_input": {"command": "Get-Content .env.example"}},
        )

        self.assertEqual(0, blocked.returncode, blocked.stderr)
        decision = json.loads(blocked.stdout)["hookSpecificOutput"]
        self.assertEqual("deny", decision["permissionDecision"])
        self.assertEqual("", allowed.stdout)

    def test_pre_tool_policy_blocks_destructive_git_command(self) -> None:
        result = run_hook(
            "pre-tool-policy",
            {"tool_name": "Bash", "tool_input": {"command": "git reset --hard"}},
        )

        self.assertEqual("deny", json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"])

    def test_post_edit_checks_understand_apply_patch_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            asset = root / "assets" / "data" / "Bad-Name.json"
            asset.parent.mkdir(parents=True)
            asset.write_text("{broken", encoding="utf-8")
            payload = {
                "cwd": str(root),
                "tool_name": "apply_patch",
                "tool_input": {
                    "command": "*** Begin Patch\n*** Update File: assets/data/Bad-Name.json\n*** End Patch"
                },
            }

            result = run_hook("post-edit-checks", payload)

        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("NAMING", context)
        self.assertIn("JSON", context)

    def test_post_edit_checks_warn_when_gameplay_has_no_gdd(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            gameplay = root / "src" / "gameplay" / "combat" / "damage.gd"
            gameplay.parent.mkdir(parents=True)
            gameplay.write_text("extends Node\n", encoding="utf-8")
            payload = {
                "cwd": str(root),
                "tool_name": "apply_patch",
                "tool_input": {
                    "command": "*** Begin Patch\n*** Add File: src/gameplay/combat/damage.gd\n*** End Patch"
                },
            }

            result = run_hook("post-edit-checks", payload)

        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("design/gdd/combat.md", context)
        self.assertIn("$design-system", context)


class SkillRegressionTests(unittest.TestCase):
    def test_godot_fixes_are_present_in_codex_skills(self) -> None:
        game_start = read(".agents/skills/game-start/SKILL.md")
        setup = read(".agents/skills/godot-setup/SKILL.md")
        sprite = read(".agents/skills/sprite-spec/SKILL.md")
        architecture = read(".agents/skills/game-arch/references/runtime-architecture.md")

        self.assertIn("src/{core,gameplay,ui,autoloads}", game_start)
        self.assertNotIn("src/{core,entities,systems,ui,utils}", game_start)
        self.assertIn("2d/snap/snap_2d_transforms_to_pixel", setup)
        self.assertNotIn("HTML5", setup)
        self.assertIn("AtlasTexture", sprite)
        self.assertIn("SpriteFrames", sprite)
        self.assertIn("CharacterBody2D", architecture)
        self.assertNotIn("SpriteBatch", architecture)

    def test_planning_fixes_are_consistent(self) -> None:
        sprint = read(".agents/skills/sprint/SKILL.md")
        story = read(".agents/skills/story/SKILL.md")

        self.assertIn("3S + 1M por semana", sprint)
        self.assertIn("6S + 2M", sprint)
        self.assertIn("$design-system", story)
        self.assertIn("src/gameplay/", story)
        self.assertNotIn("$brainstorm {system}", story)



if __name__ == "__main__":
    unittest.main()
