<div align="center">

# gamedev-skills

Skills, agentes, hooks y plugins para juegos 2D pixel art con Godot 4, asistidos por IA.

**23 skills. 9 agentes en jerarquia de estudio. 5 hooks de validacion. 3 plugins MCP. Claude Code y Codex.**

[![Skills](https://img.shields.io/badge/skills-23-ec4899?style=for-the-badge)](#skills)
[![Agentes](https://img.shields.io/badge/agentes-9-8b5cf6?style=for-the-badge)](#agentes)
[![Hooks](https://img.shields.io/badge/hooks-5-f97316?style=for-the-badge)](#hooks)
[![Plugins](https://img.shields.io/badge/plugins-3-0ea5e9?style=for-the-badge)](#plugins)
[![Godot](https://img.shields.io/badge/godot-4-478cbf?style=for-the-badge)](#flujo-de-trabajo)

[Ver skills](#skills) • [Ver agentes](#agentes) • [Ver hooks](#hooks) • [Ver flujo](#flujo-de-trabajo)

</div>

Cubre el ciclo completo de un juego 2D pixel art: concepto, diseno de sistemas, arte, arquitectura de escenas Godot, produccion por sprints y QA. Todo data-driven: los hooks avisan cuando aparece un valor hardcoded o un sistema sin GDD.

## Uso junto con ai-skills

Las skills de desarrollo general — `brainstorm`, `plan`, `tdd`, `debug`, `verify`, `execute`, `review`, `secure` — viven en el repositorio hermano [`ai-skills`](https://github.com/jhanva/ai-skills). Los flujos de este repo las usan; para tener ambas capas en un proyecto de juego:

```bash
claude --add-dir /ruta/a/ai-skills --add-dir /ruta/a/gamedev-skills
```

En Codex, copiar `.agents/skills/`, `.codex/` y `AGENTS.md` de ambos repos al proyecto destino.

El repositorio mantiene dos adaptaciones paralelas de las mismas capacidades:

- `.claude/` conserva la implementacion para Claude Code
- `.agents/skills/`, `.codex/agents/`, `.codex/config.toml`, `.codex/hooks.json` y `plugins/` contienen la adaptacion nativa para Codex

Invocacion explicita por runtime: Codex `$skill`, Claude Code `/skill`.

## Skills

### Game development

Stack orientado a juegos 2D pixel art (RPG, platformer, roguelike) con Godot 4, GDScript y C#. Incluye 20 skills y 9 agentes especializados.

#### Onboarding

| Skill | Activacion | Agente | Proposito |
|---|---|---|---|
| [`game-start`](./.agents/skills/game-start/SKILL.md) | Explicita | — | Setup guiado: Godot config, estructura de proyecto, GDScript vs C# |

#### Concepto

| Skill | Activacion | Agente | Proposito |
|---|---|---|---|
| [`game-concept`](./.agents/skills/game-concept/SKILL.md) | Explicita | [`game-designer`](./.codex/agents/game-designer.toml) | Formalizar idea en concept doc (genero, pillars, target audience) |
| [`art-bible`](./.agents/skills/art-bible/SKILL.md) | Explicita | [`pixel-artist`](./.codex/agents/pixel-artist.toml) + [`creative-director`](./.codex/agents/creative-director.toml) | Identidad visual: paleta, estilo, resoluciones, restricciones |

#### Diseno

| Skill | Activacion | Agente | Proposito |
|---|---|---|---|
| [`rpg-design`](./.agents/skills/rpg-design/SKILL.md) | Explicita | [`game-designer`](./.codex/agents/game-designer.toml) | Sistemas RPG (stats, formulas, turnos, balance, enemy AI) |
| [`design-system`](./.agents/skills/design-system/SKILL.md) | Explicita | [`game-designer`](./.codex/agents/game-designer.toml) | GDD para un sistema especifico (inventario, dialog, crafting) |
| [`level-brief`](./.agents/skills/level-brief/SKILL.md) | Explicita | [`level-designer`](./.codex/agents/level-designer.toml) | Disenar nivel: layout, encounters, curva de dificultad, pacing |
| [`balance-check`](./.agents/skills/balance-check/SKILL.md) | Contextual + explicita | [`game-designer`](./.codex/agents/game-designer.toml) | Validar balance numerico (damage curves, economy sinks/faucets) |

#### Arte y assets

| Skill | Activacion | Agente | Proposito |
|---|---|---|---|
| [`pixel-pipeline`](./.agents/skills/pixel-pipeline/SKILL.md) | Explicita | [`pixel-artist`](./.codex/agents/pixel-artist.toml) | Pipeline completo de pixel art (sprites, tiles, atlas, palette swap) |
| [`sprite-spec`](./.agents/skills/sprite-spec/SKILL.md) | Explicita | [`pixel-artist`](./.codex/agents/pixel-artist.toml) | Spec de sprite sheet: frames, estados, dimensiones, hitbox |
| [`tileset-spec`](./.agents/skills/tileset-spec/SKILL.md) | Explicita | [`pixel-artist`](./.codex/agents/pixel-artist.toml) | Spec de tileset: tile size, autotile rules, variantes |
| [`palette`](./.agents/skills/palette/SKILL.md) | Explicita | [`pixel-artist`](./.codex/agents/pixel-artist.toml) | Crear/gestionar paletas de color (ramps, restrictions) |
| [`sound-brief`](./.agents/skills/sound-brief/SKILL.md) | Explicita | [`sound-designer`](./.codex/agents/sound-designer.toml) | Brief de audio: SFX list, mood board musical, integracion Godot |

#### Arquitectura

| Skill | Activacion | Agente | Proposito |
|---|---|---|---|
| [`game-arch`](./.agents/skills/game-arch/SKILL.md) | Explicita | [`godot-architect`](./.codex/agents/godot-architect.toml) | Arquitectura de juegos 2D (game loop, FSM, commands, save system) |
| [`godot-setup`](./.agents/skills/godot-setup/SKILL.md) | Explicita | [`godot-architect`](./.codex/agents/godot-architect.toml) | Config proyecto Godot: autoloads, input map, export, folder structure |
| [`scene-design`](./.agents/skills/scene-design/SKILL.md) | Explicita | [`godot-architect`](./.codex/agents/godot-architect.toml) | Disenar escena: node tree, signals, script responsibilities |

#### Produccion

| Skill | Activacion | Agente | Proposito |
|---|---|---|---|
| [`sprint`](./.agents/skills/sprint/SKILL.md) | Explicita | [`producer`](./.codex/agents/producer.toml) | Planificar sprint: stories, estimacion, prioridades |
| [`story`](./.agents/skills/story/SKILL.md) | Explicita | [`producer`](./.codex/agents/producer.toml) | Crear dev story desde seccion de GDD |
| [`scope-check`](./.agents/skills/scope-check/SKILL.md) | Contextual + explicita | [`producer`](./.codex/agents/producer.toml) | Verificar que el scope es realista vs tiempo disponible |

#### QA

| Skill | Activacion | Agente | Proposito |
|---|---|---|---|
| [`playtest`](./.agents/skills/playtest/SKILL.md) | Explicita | [`qa-analyst`](./.codex/agents/qa-analyst.toml) | Reporte estructurado de playtest session |
| [`smoke-test`](./.agents/skills/smoke-test/SKILL.md) | Explicita | [`qa-analyst`](./.codex/agents/qa-analyst.toml) | Checklist rapido pre-merge/pre-release |

## Agentes

### Game dev — Jerarquia de estudio

9 agentes organizados en 2 niveles para concepto, arte, arquitectura, produccion y QA. La implementacion concreta depende del runtime; en Codex viven en `.codex/agents/`.

```
Tier 1 — Directores
  creative-director ──── pixel-artist
    (vision, coherencia       sound-designer
     arte + diseno)           game-designer
                              level-designer

  technical-director ─── godot-architect
    (arquitectura,            qa-analyst
     codigo + calidad)        producer
```

| Agente | Tier | Dominio | Se activa cuando... |
|---|---|---|---|
| [`creative-director`](./.codex/agents/creative-director.toml) | Director | Vision global, coherencia arte/diseno | Conflicto entre dominios creativos, review de concepto |
| [`technical-director`](./.codex/agents/technical-director.toml) | Director | Arquitectura global, performance | Conflicto codigo/performance, decision arquitectural |
| [`pixel-artist`](./.codex/agents/pixel-artist.toml) | Especialista | Sprites, tiles, animacion, paletas, atlas | Editando `assets/sprites/`, `assets/tiles/` |
| [`sound-designer`](./.codex/agents/sound-designer.toml) | Especialista | SFX, musica, audio pipeline | Editando `assets/audio/`, definiendo audio en GDD |
| [`game-designer`](./.codex/agents/game-designer.toml) | Especialista | Sistemas, mecanicas, balance, economia | Escribiendo GDDs en `design/`, discutiendo mecanicas |
| [`level-designer`](./.codex/agents/level-designer.toml) | Especialista | Niveles, encounters, dificultad, world building | Editando `design/levels/`, discutiendo layout |
| [`godot-architect`](./.codex/agents/godot-architect.toml) | Especialista | Escenas, signals, GDScript/C#, patterns Godot | Editando `.gd`, `.cs`, `.tscn`, `.tres` |
| [`qa-analyst`](./.codex/agents/qa-analyst.toml) | Especialista | Tests, bug triage, playtesting | Post-implementacion, pre-release |
| [`producer`](./.codex/agents/producer.toml) | Especialista | Sprints, scope, milestones, stories | Planificando trabajo, revisando progreso |

## Hooks (game dev)

Codex carga [`hooks.json`](./.codex/hooks.json) desde la capa confiable del
proyecto. Los handlers multiplataforma viven en
[`codex_hooks.py`](./.codex/hooks/codex_hooks.py) y consumen el JSON nativo de
`PreToolUse`, `PostToolUse` y `SessionStart`.

| Handler Codex | Evento | Que valida |
|---|---|---|
| `pre-tool-policy` | PreToolUse (Bash/apply_patch) | Bloquea `.env`, comandos destructivos y edits protegidos |
| `validate-gameplay-code` | PreToolUse (git commit) | Valores hardcoded, estrategia de delta y dependencias UI |
| `post-edit-checks` | PostToolUse (apply_patch) | Naming/JSON de assets y cobertura GDD de gameplay |
| `session-context` | SessionStart | Branch, commits, sprint y archivos modificados |

La capa Claude conserva sus cinco scripts originales:

5 hooks de validacion automatica para codigo, assets y seguridad. Comparten biblioteca `_parse.sh` para parsing JSON (cero duplicacion).

| Hook | Evento | Que valida |
|---|---|---|
| [`block-env-access.sh`](./.claude/hooks/block-env-access.sh) | PreToolUse (Bash) | Bloquea lectura/escritura/source de archivos `.env` (permite `.env.example`, `.env.sample`, `.env.template`) |
| [`validate-gameplay-code.sh`](./.claude/hooks/validate-gameplay-code.sh) | PreToolUse (git commit) | No hardcoded values en `src/gameplay/`, delta time usage, no imports de UI en gameplay |
| [`validate-assets.sh`](./.claude/hooks/validate-assets.sh) | PostToolUse (Write/Edit) | Naming convention en `assets/` (lowercase_snake), JSON valido en data files |
| [`check-design-coverage.sh`](./.claude/hooks/check-design-coverage.sh) | PostToolUse (Write/Edit) | Advierte si existe codigo en `src/gameplay/X/` sin su `design/gdd/X.md` correspondiente |
| [`session-context.sh`](./.claude/hooks/session-context.sh) | SessionStart | Muestra branch, sprint activo, archivos modificados sin commit |

## Plugins

| Plugin | Ruta | Proposito |
|---|---|---|
| [`aseprite-codex`](./plugins/aseprite-codex/.codex-plugin/plugin.json) | `plugins/aseprite-codex/` | Integracion local para Aseprite con `skill` + `MCP` para inspeccionar sprites, exportar sprite sheets y correr scripts Lua desde Codex |

## Pets

Custom pets portables para Codex, listas para copiar a otra maquina:

- [`albedo`](./pets/albedo/README.md): paquete portable final con `pet.json` y `spritesheet.webp`
- [`the-lich-king`](./pets/the-lich-king/README.md): paquete portable con `pet.json`, `spritesheet.webp`, QA visual y guia de instalacion, transporte y regeneracion con `hatch-pet`

## Flujo de trabajo

### Game development

```
Concepto:
  brainstorm  -->  game-concept  -->  art-bible
                         |
Diseno:                  |
  design-system  -->  rpg-design     -->  balance-check
  level-brief                                  |
                                                v
Arte:                                    Arquitectura:
  palette  -->  pixel-pipeline           game-arch  -->  godot-setup
  sprite-spec   tileset-spec             scene-design
  sound-brief                                  |
                                                v
Produccion:                              QA:
  sprint  -->  story  -->  plan         playtest  -->  smoke-test
                  |
                  v
            execute (usa tdd)  -->  review  -->  verify
```

Integracion con skills generales: `tdd` para todo codigo, `debug` para bugs, `verify` antes de completar, `review` para code review de GDScript/C#.

## Estructura

```
.claude/skills/                        # 23 skills para Claude Code
.claude/agents/gamedev/                # 9 agentes (2 directores + 7 especialistas)
.claude/hooks/                         # 5 hooks bash + _parse.sh
.agents/skills/                        # 20 skills para Codex (las 3 de MCP viven en plugins/)
.codex/agents/                         # 9 agentes custom para Codex + playbooks
.codex/hooks.json                      # registro de hooks nativos de Codex
.codex/hooks/codex_hooks.py            # handlers Python multiplataforma
plugins/                               # aseprite-codex, godot-codex, pixellab-codex
pets/                                  # pets portables para Codex
AGENTS.md                              # reglas de trabajo del repo
```

Estructura de proyecto de juego que asumen skills y hooks: `src/gameplay/`, `assets/`, `design/gdd/`, `production/sprints/`.

## Instalacion

```bash
git clone https://github.com/jhanva/gamedev-skills.git
```

**Claude Code**: `claude --add-dir /ruta/a/gamedev-skills` o copiar `.claude/` al proyecto.

**Codex**: copiar `.agents/skills/`, `.codex/`, `plugins/` y `AGENTS.md` al proyecto destino.

## Principios

1. **No codear sin disenar** — `game-concept` y `design-system` antes de implementar un sistema
2. **Nada hardcoded** — valores de gameplay en `assets/data/`, validado por hook
3. **No adivinar balance** — `balance-check` con tabla de escenarios
4. **No decir "listo" sin evidencia** — `playtest` y `smoke-test` antes de merge
5. **No confiar en reportes de subagentes** — verificar independientemente
6. **No referenciar origenes externos** — no mencionar repos o proyectos de terceros como inspiracion en documentacion

## Licencia

Uso personal.
