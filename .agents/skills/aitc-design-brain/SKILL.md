---
name: aitc-design-brain
description: Joel's personal design-taste layer for AITC. Load alongside aitc-brand whenever producing visual output for AITC — posts, slides, web pages, flyers, thumbnails, email headers, merch, motion. This is not a replacement for BRAND.md or DESIGNER.md; it is the interpretation layer that keeps the output soft, spacey, lowercase-informal, and regresssion-free. Use when the user gives feeling/metaphor feedback, asks for "premium" or "spacey", or when a design choice is underdetermined by the brand spec.
---

# AITC design brain (Joel's taste layer)

## Relationship to the brand spec

1. **BRAND.md / DESIGNER.md are law.** Follow them exactly unless the user explicitly says to break them.
2. This skill is the *taste* layer: how to interpret soft, premium, spacey, and modern-informal within those rules.
3. When in conflict, the spec wins. When the spec is silent, this skill decides.

## Core instincts

- **Softness first.** Gradients, shadows, and transitions should feel like atmosphere, not borders. If a fade has a shoulder, shelf, or hard edge, it is wrong.
- **Space is the hero.** Easy to look at means generous negative space. Type should breathe. The eye should catch a rest, not chase clutter.
- **Type and spacing are sacred.** Do not mess with font choice, line-height, letter-spacing, or alignment unless the user asks. Random regressions here are the fastest way to break trust.
- **Premium = Apple modern + lowercase informal.** Clean geometry, restrained palette, exact proportions, but the voice stays relaxed and lowercase.

## How to interpret feedback

Joel gives feedback by feeling and metaphor, not numbers. Translate like this:

| He says | He means |
| --- | --- |
| "softer" | Lengthen transitions, reduce contrast/chroma, add perceptual evenness (oklab), dither if needed. No hard edges. |
| "spacey" | Add or preserve negative space; don't crowd the frame; let the eye rest. |
| "premium" | Tighten to BRAND.md proportions, keep it clean, make it feel designed-not-decorated, lowercase informal. |
| "rough" | The gradient/stepping/edge is visible; smooth it, stretch it, or add grain dither. |
| "circle fade thing" / "faded to both sides" | Use a radial/elliptical falloff, not a linear diagonal. Stretch the ellipse so it fades gradually along multiple axes. |
| "this feels off" | First suspect a regression in type, spacing, alignment, or a brand-rule violation before inventing a new direction. |

## Hard rules

- **No styling departures without explicit permission.** Do not introduce a new font, color, layout pattern, or effect because it "might look cool."
- **No regressions.** If you change one element, check that nothing else shifted, clipped, or reset.
- **Ask first on ambiguity.** If a direction is underdetermined, ask before guessing — especially on expensive renders or broad layout changes.
- **Small nudges, not big jumps.** Iterate softly; don't overcorrect.

## Pre-ship check for any visual

Before showing a render:

1. Re-read the relevant section of `BRAND.md` and confirm no rule was bent.
2. Check type: font, size, line-height, letter-spacing, alignment, and that no glyph is clipped.
3. Check spacing: margins, padding, and negative space match the established geometry.
4. Check the gradient/shadow: is it soft? Is there a visible band or edge?
5. Open the actual PNG and look at it. Do not ship HTML-only.

## When this skill fires

- User describes something as "soft", "spacey", "premium", "rough", "Nothing ad", "circle fade", etc.
- User is reviewing a visual and the issue is taste, not a spec violation.
- User has not given literal specs and the next move is unclear — ask first.
