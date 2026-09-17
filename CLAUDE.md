@AGENTS.md

# Gamedev Skills — Skills & Agents para juegos 2D pixel art con Godot 4

Skills, agentes, hooks y plugins para desarrollar juegos 2D pixel art con Godot 4 de forma asistida. Cubren el ciclo completo: concepto, diseno de sistemas, arte, arquitectura de escenas, produccion y QA.

Las skills de desarrollo general (`/brainstorm`, `/plan`, `/tdd`, `/debug`, `/verify`, `/execute`, `/review`, `/secure`) viven en el repositorio hermano `ai-skills` (https://github.com/jhanva/ai-skills). Los flujos de este documento las referencian; para tenerlas disponibles, cargar ambos repos:

```bash
claude --add-dir /ruta/a/ai-skills --add-dir /ruta/a/gamedev-skills
```

## Estructura

```
.claude/skills/
  rpg-design/SKILL.md              — Diseno de sistemas RPG (stats, combate, balance)
  game-arch/SKILL.md               — Arquitectura de juegos 2D (game loop, FSM, commands)
  pixel-pipeline/SKILL.md          — Pipeline de assets pixel art (sprites, tiles, atlas)
  game-start/SKILL.md              — Onboarding de proyecto Godot (setup guiado)
  game-concept/SKILL.md            — Formalizar concepto de juego (pillars, core loop, MVP)
  art-bible/SKILL.md               — Identidad visual (paleta, estilo, restricciones)
  design-system/SKILL.md           — GDD por sistema (inventario, dialogo, crafting)
  level-brief/SKILL.md             — Diseno de nivel (layout, encounters, dificultad)
  balance-check/SKILL.md           — Validacion de balance numerico
  sprite-spec/SKILL.md             — Spec de sprite sheet (frames, estados, hitbox)
  tileset-spec/SKILL.md            — Spec de tileset (autotile, variantes, layers)
  palette/SKILL.md                 — Gestion de paletas de color (ramps, swaps)
  sound-brief/SKILL.md             — Brief de audio (SFX, musica, Godot integration)
  godot-setup/SKILL.md             — Config proyecto Godot (autoloads, input, display)
  scene-design/SKILL.md            — Diseno de escena Godot (node tree, signals)
  sprint/SKILL.md                  — Planificacion de sprints (1-2 semanas, 3-5 stories)
  story/SKILL.md                   — GDD -> user story con scope y acceptance criteria
  scope-check/SKILL.md             — Validacion de scope (MVP alcanzable? velocity, riesgos)
  playtest/SKILL.md                — Sesion de playtest con checklist y game feel rating
  smoke-test/SKILL.md              — Smoke test pre-merge/pre-release (automated + manual)
  aseprite-workflows/SKILL.md      — Automatizacion de Aseprite via MCP (inspect, export, Lua)
  aseprite-workflows/references/tool-map.md  — Recetas y mapeo de tools MCP
  godot-workflows/SKILL.md         — Automatizacion headless de Godot 4 via MCP (import, export, scripts)
  godot-workflows/references/tool-map.md     — Recetas y mapeo de tools MCP
  pixellab-workflows/SKILL.md      — Generacion de assets pixel art via PixelLab MCP
  pixellab-workflows/references/tool-map.md  — Catalogo de tools del MCP oficial

.claude/agents/
  gamedev/creative-director.md     — Director: vision arte + diseno (opus)
  gamedev/technical-director.md    — Director: arquitectura + calidad (opus)
  gamedev/pixel-artist.md          — Especialista: sprites, tiles, animacion
  gamedev/sound-designer.md        — Especialista: SFX, musica
  gamedev/game-designer.md         — Especialista: sistemas, mecanicas, balance
  gamedev/level-designer.md        — Especialista: niveles, encounters
  gamedev/godot-architect.md       — Especialista: engine patterns, escenas
  gamedev/qa-analyst.md            — Especialista: testing, playtesting
  gamedev/producer.md              — Especialista: sprints, scope, milestones

.claude/hooks/
  _parse.sh                        — Biblioteca compartida (JSON parsing)
  block-env-access.sh              — Bloquea acceso a archivos .env
  validate-gameplay-code.sh        — No hardcoded values, delta time, layer separation
  validate-assets.sh               — Naming convention, JSON valido en data files
  check-design-coverage.sh         — Codigo sin GDD = warning
  session-context.sh               — Contexto del proyecto al iniciar sesion

plugins/
  aseprite-codex/                  — Plugin Codex: skill + MCP para Aseprite
  godot-codex/                     — Plugin Codex: skill + MCP para Godot 4 headless
  pixellab-codex/                  — Plugin Codex: skill + MCP oficial de PixelLab

pets/
  the-lich-king/                   — Pet portable para Codex (pet.json + spritesheet)
  albedo/                          — Pet portable para Codex (pet.json + spritesheet)
```

## Skills disponibles

| Skill | Invocacion | Proposito |
|---|---|---|
| `/rpg-design` | Solo usuario | Diseno de sistemas RPG (stats, formulas, turnos, balance, enemy AI) |
| `/game-arch` | Solo usuario | Arquitectura de juegos 2D (game loop, FSM, commands, save system) |
| `/pixel-pipeline` | Solo usuario | Pipeline de assets pixel art (sprites, tiles, atlas, palette swap) |
| `/game-start` | Solo usuario | Onboarding: Godot config, estructura, GDScript vs C# |
| `/game-concept` | Solo usuario | Formalizar idea en concept doc (pillars, core loop, MVP) |
| `/art-bible` | Solo usuario | Identidad visual: paleta, estilo, restricciones pixel art |
| `/design-system` | Solo usuario | GDD para un sistema especifico (inventario, dialogo, crafting) |
| `/level-brief` | Solo usuario | Disenar nivel: layout ASCII, encounters, dificultad |
| `/balance-check` | Auto + usuario | Validar balance numerico (damage curves, economy) |
| `/sprite-spec` | Solo usuario | Spec de sprite sheet: frames, estados, dimensiones, hitbox |
| `/tileset-spec` | Solo usuario | Spec de tileset: autotile rules, variantes, layers |
| `/palette` | Solo usuario | Crear/gestionar paletas de color (ramps, swaps) |
| `/sound-brief` | Solo usuario | Brief de audio: SFX list, musica, integracion Godot |
| `/godot-setup` | Solo usuario | Config proyecto Godot: autoloads, input, display |
| `/scene-design` | Solo usuario | Disenar escena: node tree, signals, scripts |
| `/sprint` | Solo usuario | Planificacion de sprint (stories, capacity, acceptance criteria) |
| `/story` | Solo usuario | GDD -> user story (scope, files, estimacion S/M/L, dependencies) |
| `/scope-check` | Auto + usuario | Validar si MVP es alcanzable (velocity, proyeccion, riesgos) |
| `/playtest` | Solo usuario | Playtest estructurado (funcionalidad + game feel + bugs) |
| `/smoke-test` | Solo usuario | Smoke test pre-merge/pre-release (automated + manual) |
| `/aseprite-workflows` | Solo usuario | Inspeccionar, exportar y automatizar Aseprite via MCP |
| `/godot-workflows` | Solo usuario | Import headless, export builds, scripts de Godot 4 via MCP |
| `/pixellab-workflows` | Solo usuario | Generar personajes, tilesets y props con PixelLab MCP |

"Solo usuario" = `disable-model-invocation: true` (se invoca manualmente con `/nombre`)
"Auto + usuario" = Claude puede invocarlo automaticamente cuando detecta el contexto relevante

## Flujo recomendado

### Game development

Workflow completo para juegos 2D pixel art con Godot 4. 9 agentes en jerarquia de estudio + 5 hooks.

#### Concepto → Diseno → Arte → Arquitectura → Produccion → QA
```
/game-start  -->  /brainstorm  -->  /game-concept  -->  /art-bible
                                         |
                  /design-system  -->  /rpg-design  -->  /balance-check
                  /level-brief
                                                            |
/palette  -->  /pixel-pipeline                     /game-arch  -->  /godot-setup
/sprite-spec   /tileset-spec                       /scene-design
/sound-brief   /pixellab-workflows                      |
/aseprite-workflows                                     |
                                                        v
/scope-check  -->  /sprint  -->  /story  -->  /plan  -->  /execute (usa /tdd)
                                                              |
                                                    /playtest  -->  /smoke-test
                                                              |
                                                    /review  -->  /verify  -->  merge
```

#### Agentes gamedev (jerarquia de estudio)
```
Tier 1 — Directores (opus)
  creative-director ──── pixel-artist, sound-designer, game-designer, level-designer
  technical-director ─── godot-architect, qa-analyst, producer
```


### Herramientas externas (MCP)
```
/aseprite-workflows    Inspeccionar .aseprite, exportar sheets/frames, correr Lua
/godot-workflows       Import headless, export builds, scripts de automatizacion
/pixellab-workflows    Generar personajes, tilesets, props con PixelLab AI
```


## Hooks

| Hook | Evento | Que hace |
|---|---|---|
| `session-context.sh` | SessionStart | Branch, commits recientes, sprint activo, cambios sin commit |
| `block-env-access.sh` | PreToolUse (Bash) | Bloquea lectura/escritura de archivos de entorno |
| `validate-gameplay-code.sh` | PreToolUse (Bash, en `git commit`) | Valores hardcoded, delta time, separacion de capas en `.gd`/`.cs` |
| `validate-assets.sh` | PostToolUse (Write/Edit) | Naming `lowercase_snake_case` en `assets/`, JSON valido en `assets/data/` |
| `check-design-coverage.sh` | PostToolUse (Write/Edit) | Codigo en `src/gameplay/<sistema>/` sin `design/gdd/<sistema>.md` = warning |

Estructura de proyecto que asumen hooks y skills: `src/gameplay/`, `assets/`, `design/gdd/`, `production/sprints/`.

## Principios

1. **No codear sin disenar** — `/game-concept` y `/design-system` antes de implementar un sistema
2. **Nada hardcoded** — valores de gameplay en `assets/data/`, validado por hook
3. **No adivinar balance** — `/balance-check` con tabla de escenarios
4. **No decir "listo" sin evidencia** — `/playtest` y `/smoke-test` antes de merge
5. **No confiar en reportes de subagentes** — verificar independientemente
6. **No referenciar origenes externos** — no mencionar repos, librerias o proyectos de terceros como inspiracion u origen en documentacion del proyecto. El contenido se presenta como propio
