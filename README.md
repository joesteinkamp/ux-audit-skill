# ux-audit-skill

A Claude Code skill (`/ux-audit`) that audits UI screenshots against 15 published UX
heuristics frameworks and produces severity-rated, principle-cited findings, calibrated
0–100 scores, annotated screenshots, and a self-contained HTML report.

**Usage:** in any Claude Code session with the skill installed, provide 1+ screenshots and
say "audit this design" / "/ux-audit". One round of intake questions (goal, persona,
platform, artifact stage), then the audit runs. Outputs land in `audits/<slug>-<date>/`:
`findings.json`, `summary.md`, `annotated/*.png`, `report.html`.

**Install:** `ln -s ~/projects/ux-audit-skill ~/.claude/skills/ux-audit`

| Doc | Purpose |
|---|---|
| `plan.html` | Design plan (frameworks, tiers, scoring model, architecture) |
| `execution-plan.html` | Milestone/task breakdown M0–M7 with gates |
| `SKILL.md` | The skill itself |
| `references/` | Scoring rubric, filter, report spec, 11 framework files + registry |
| `scripts/` | measure / annotate / build_report / registry / fixtures (see scripts/README.md) |
| `fixtures/` | Golden screenshots + expected findings for calibration |

## Milestone status
| | Milestone | Status |
|---|---|---|
| M0 | Scaffolding | done |
| M1 | Framework registry | done |
| M2 | Single-screen MVP | done |
| M3 | measure.py | done |
| M4 | annotate.py | done |
| M5 | Flow mode | done |
| M6 | HTML report | done |
| M7 | Calibration & hardening | done (baselines recorded for fixtures a, b; c–e await first audit) |
