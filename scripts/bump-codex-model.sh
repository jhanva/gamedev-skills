#!/usr/bin/env bash
# Actualiza el pin de modelo de Codex en todos los agentes a la vez.
#
# Uso:
#   scripts/bump-codex-model.sh <model>
#
# Ejemplo:
#   scripts/bump-codex-model.sh gpt-5.5
#
# Actualiza:
#   - .codex/agents/creative-director.toml
#   - .codex/agents/technical-director.toml
#   - .codex/agents/game-designer.toml
#   - .codex/agents/level-designer.toml
#   - .codex/agents/godot-architect.toml
#   - .codex/agents/pixel-artist.toml
#   - .codex/agents/sound-designer.toml
#   - .codex/agents/qa-analyst.toml
#   - .codex/agents/producer.toml

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <model>" >&2
  exit 2
fi

MODEL="$1"

cd "$(dirname "$0")/.."

PYTHON_BIN=""
for candidate in python python3 py; do
  if command -v "$candidate" >/dev/null 2>&1 && "$candidate" -c "import pathlib" >/dev/null 2>&1; then
    PYTHON_BIN="$candidate"
    break
  fi
done

if [ -z "$PYTHON_BIN" ]; then
  echo "Error: Python is required (python, python3 or py)." >&2
  exit 3
fi

"$PYTHON_BIN" - "$MODEL" <<'PY'
import re, sys, pathlib

model = sys.argv[1]

agents = [
    ".codex/agents/creative-director.toml",
    ".codex/agents/technical-director.toml",
    ".codex/agents/game-designer.toml",
    ".codex/agents/level-designer.toml",
    ".codex/agents/godot-architect.toml",
    ".codex/agents/pixel-artist.toml",
    ".codex/agents/sound-designer.toml",
    ".codex/agents/qa-analyst.toml",
    ".codex/agents/producer.toml",
]

def bump(path: str, model: str) -> None:
    p = pathlib.Path(path)
    text = p.read_text()
    new, n = re.subn(r'^(model\s*=\s*)"[^"]+"', rf'\1"{model}"', text, count=1, flags=re.M)
    if n == 0:
        print(f"  warn: no model line in {path}")
        return
    if new == text:
        print(f"  noop (already {model}): {path}")
        return
    p.write_text(new)
    print(f"  updated {path} -> {model}")

print(f"Setting model to {model}")
for a in agents:
    bump(a, model)
PY

echo "Done. Review changes with: git diff .codex/"
