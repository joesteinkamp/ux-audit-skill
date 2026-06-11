---
prefix: FOGG
framework: "Fogg Behavior Model (B = MAP)"
source: https://behaviormodel.org/
tier: [3]
category: trust_persuasion
---
## Principles
| ID | Name | Definition |
|---|---|---|
| FOGG-M | Motivation | The drive to perform the behavior; can compensate for low ability. |
| FOGG-A | Ability | How easy the behavior is at that moment; simplicity beats motivation boosts. |
| FOGG-P | Prompt | The cue that triggers the behavior; without it nothing happens. |

## Diagnostic logic
When a target behavior (signup, purchase, activation) isn't happening, exactly these
three failure modes exist. From screenshots you can form HYPOTHESES only:
- **FOGG-P hypothesis**: the prompt is weak/invisible — CTA below fold, low salience,
  competing prompts. Visible evidence is real, but whether it explains a conversion gap
  is unproven.
- **FOGG-A hypothesis**: ability barriers — long forms, many steps, unclear effort/cost.
- **FOGG-M hypothesis**: motivation gap — value proposition absent or generic at the
  decision point; benefit stated nowhere near the ask.

## Output rules (hard)
1. Every FOGG finding has `type: "hypothesis"`, never moves scores.
2. Every FOGG hypothesis names its validation method, e.g.:
   - FOGG-P → "instrument CTA viewability + click-through at this step"
   - FOGG-A → "funnel analysis: drop-off per form field / step"
   - FOGG-M → "A/B value-proposition copy at this decision point; exit survey"
3. If the visible evidence alone is a Tier-1/2 violation (e.g. CTA contrast failure),
   file THAT as an observed finding under its own principle, and keep the conversion
   claim in the hypothesis.

## Worked example
```json
{ "principles": ["FOGG-P"], "type": "hypothesis", "severity": "medium",
  "issue": "The only signup prompt sits below the fold behind two scroll lengths of features.",
  "why_it_matters": "If visitors don't reach the prompt, motivation and ability never get a chance to act.",
  "recommendation": "Add a persistent header CTA and test placement.",
  "validation": "Measure CTA viewability and CTR by scroll depth before/after." }
```
