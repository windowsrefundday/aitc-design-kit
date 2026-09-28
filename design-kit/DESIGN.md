---
version: alpha
name: AITC
description: >-
  Design system for the AI Technology Club at Enloe High School. Cream on forest
  green, one typeface, everything lowercase, type set enormous and tightly
  tracked inside a single floating rounded panel.
colors:
  # Brand core
  primary: "#216434"            # forest — the brand green, ink on light grounds
  primary-mid: "#174b2a"        # deep green, gradient stop
  primary-deep: "#0c2719"       # darkest — the "black" of the system
  primary-light: "#8dad82"      # sage — gradients and light-ground steps only
  secondary: "#2b7244"          # ink — body and headline color on cream
  neutral: "#fff3cb"            # cream — the "white" of the system
  neutral-soft: "#f4e8b8"       # secondary text on dark, lower half of cream gradients
  neutral-hi: "#fff9e6"         # top stop of the cream text gradient only

  # Surface roles — dark ground (body sections, closers, most content)
  surface: "#0c2719"
  on-surface: "#fff3cb"
  on-surface-variant: "rgba(255, 243, 203, 0.78)"
  on-surface-caption: "rgba(255, 243, 203, 0.58)"
  outline: "rgba(255, 243, 203, 0.16)"

  # Surface roles — light ground (hero, covers, anything that opens)
  surface-light: "#fff3cb"
  on-surface-light: "#2b7244"
  on-surface-light-variant: "rgba(33, 100, 52, 0.62)"
  outline-light: "rgba(12, 39, 25, 0.12)"

  # Gradient stops — exact, used only inside grounds. Never as flat fills.
  gradient-sage-1: "#6f9d6f"
  gradient-sage-2: "#558f61"
  gradient-forest-1: "#35744a"
  gradient-forest-2: "#1d5730"
  gradient-forest-3: "#0f3a20"
  bridge-sage: "#dbe1b3"        # never place text on this band
  bridge-sage-deep: "#d5dfb0"   # never place text on this band

  # Effects
  shadow-glow: "rgba(30, 96, 55, 0.81)"    # the signature type glow
  shadow-ambient: "rgba(4, 28, 15, 0.2)"   # card shadow, always green-black
  shadow-frame: "rgba(8, 28, 16, 0.75)"    # image-frame shadow
typography:
  # Sizes are canonical at S = 1080 (the short edge of the canvas).
  # See "Typography" prose for the % rule that ports these to any medium.
  display-mega:
    fontFamily: Inter Tight
    fontSize: 320px
    fontWeight: 600
    lineHeight: 0.76
    letterSpacing: -0.08em
  display-lg:
    fontFamily: Inter Tight
    fontSize: 160px
    fontWeight: 600
    lineHeight: 0.96
    letterSpacing: -0.04em
  headline-title:
    fontFamily: Inter Tight
    fontSize: 112px
    fontWeight: 600
    lineHeight: 0.94
    letterSpacing: -0.045em
  headline-name:
    fontFamily: Inter Tight
    fontSize: 100px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: -0.035em
  headline-kicker:
    fontFamily: Inter Tight
    fontSize: 94px
    fontWeight: 600
    lineHeight: 0.98
    letterSpacing: -0.04em
  subhead:
    fontFamily: Inter Tight
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: -0.035em
  body-lg:
    fontFamily: Inter Tight
    fontSize: 54px
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: -0.035em
  body-md:
    fontFamily: Inter Tight
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.02em
  label-eyebrow:
    fontFamily: Inter Tight
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0.14em
  label-pill:
    fontFamily: Inter Tight
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0.04em
rounded:
  sm: 12px
  md: 24px
  lg: 40px      # image frames — 3.7% of S
  xl: 56px      # the panel — 5.2% of S
  full: 9999px  # pills, badges, nav buttons
spacing:
  # Canonical at S = 1080. Every value is a fixed % of the short edge.
  panel-inset: 22px          # 2.0% of S
  panel-padding-top: 46px    # 4.3% of S
  panel-padding-x: 42px      # 3.9% of S
  panel-padding-bottom: 42px # 3.9% of S
  logo-gap: 28px             # 2.6% of S
  header-gap: 34px           # 3.1% of S
  gutter: 36px               # 3.3% of S
  xs: 12px
  sm: 22px
  md: 34px
  lg: 46px
  xl: 72px
components:
  panel:
    backgroundColor: "rgba(255, 249, 230, 0.135)"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.xl}"
    padding: 46px
  panel-light:
    backgroundColor: "rgba(12, 39, 25, 0.045)"
    textColor: "{colors.on-surface-light}"
    rounded: "{rounded.xl}"
    padding: 46px
  image-frame:
    backgroundColor: "{colors.primary-deep}"
    rounded: "{rounded.lg}"
  content-card:
    backgroundColor: "#387043"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
    padding: 34px
  pill:
    backgroundColor: "rgba(255, 243, 203, 0.12)"
    textColor: "{colors.neutral-soft}"
    typography: "{typography.label-pill}"
    rounded: "{rounded.full}"
    padding: 8px 13px
  pill-active:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.label-pill}"
    rounded: "{rounded.full}"
    padding: 8px 13px
  cta-primary:
    textColor: "{colors.neutral}"
    typography: "{typography.display-lg}"
  eyebrow:
    textColor: "{colors.on-surface-caption}"
    typography: "{typography.label-eyebrow}"
---

# AITC DESIGN.md

Machine-readable summary of the AITC design system, in the
[DESIGN.md format](https://github.com/google-labs-code/design.md).

| Need | Read |
|---|---|
| Exact math, render pipeline, starter template | `BRAND.md` |
| Prose prompts for Stitch / v0 / Figma Make | `DESIGNER.md` |
| Tokens for a coding agent | this file |

Where files disagree, `BRAND.md` wins.

## Overview

AITC is the AI Technology Club at Enloe High School. Tagline: **build with ai.
create whats next.**

Confident, oversized, editorial. A modern sportswear brand crossed with an Apple
keynote slide — calm, spacious, expensive. Not playful, not techy, not corporate,
not startup. The audience is high-school students and the adults who fund them,
so the work has to read as serious craft rather than club flyer.

The personality lives in exactly two moves: **type is far larger than a normal
design system, and tracking tightens as it grows.** Everything else is restraint.
Empty space is the point — do not fill it. Nothing decorates: every mark on a
canvas is type, photo, logo, or ground. No lines, rules, arrows, icons, dots,
corner ornaments, or texture anywhere.

Compositions sit inside one rounded translucent panel floating in a diagonal
gradient. Nesting stops at panel plus one image frame.

## Colors

Two families only — cream and forest. No third hue exists in the system. The
accent is a *contrast jump*, not a color: when something needs to pop, it becomes
cream on deep forest.

- **Cream (`neutral` #fff3cb):** the primary light ground and the primary text
  color on dark grounds. This is the system's white. Pure white is never used.
- **Soft cream (`neutral-soft` #f4e8b8):** secondary text on dark, and the lower
  stop of every cream text gradient.
- **Forest (`primary` #216434):** the brand green. Ink on light grounds.
- **Deep forest (`primary-deep` #0c2719):** the darkest value and the system's
  black. Page grounds, image-frame backing, headline text on cream. Pure black is
  never used.
- **Ink (`secondary` #2b7244):** body and headline color on cream grounds.
- **Sage (`primary-light` #8dad82, `bridge-sage` #dbe1b3):** appears only as a
  transition step inside a gradient. Never a flat fill, and **never behind text** —
  neither cream nor forest reads on the sage bridge band.

Grays do not exist; anything gray-adjacent is a tinted forest. All shadows are
green-black (`rgba(4, 28, 15, ·)`), never neutral.

**Text-on-ground pairings:**

| Ground | Primary text | Secondary text |
|---|---|---|
| Cream / light gradient | `secondary` #2b7244 | `on-surface-light-variant` |
| Deep forest / green gradient | `neutral` #fff3cb | `on-surface-variant` |
| Sage bridge band | — | never place text here |

Secondary-text opacity ladder on dark: `.90` card copy → `.78` lede → `.68`
caption → `.58` whisper → `.45` footer.

**Measured contrast** (WCAG 2.1, opaque pairs):

| Pair | Ratio | Verdict |
|---|---|---|
| cream on `primary-deep` | 14.35:1 | AAA |
| soft cream on `primary-deep` | 12.94:1 | AAA |
| `secondary` ink on cream | 5.27:1 | AA |
| `primary` forest on cream | 6.45:1 | AA |
| cream on `gradient-forest-1` #35744a | 5.05:1 | AA |
| cream on `gradient-sage-1` #6f9d6f | **2.81:1** | fails AA |

The mid-green ground crosses that threshold roughly a third of the way down.
Display type carries it (large-text AA is 3:1, and the glow adds separation), but
**body copy and captions must sit on the lower two-thirds of the gradient**, past
`#35744a`. Do not run small text across the light top-left corner.

The three translucent components below (`panel`, `panel-light`, `pill`) will trip
a contrast linter, because their fills are 4–14% overlays and a linter composites
them against nothing. In use they always sit on one of the three grounds, where
the effective pairs are the opaque ones in the table above.

**Three canonical grounds.** Every surface is one of these; do not invent a fourth.

```css
/* A. Light — hero, covers, anything that opens */
background:
  radial-gradient(circle at 100% 100%, rgba(12,39,25,0.96) 0%,
    rgba(33,100,52,0.68) 24%, rgba(255,243,203,0) 68%),
  linear-gradient(135deg, #fff3cb 0%, #fff3cb 56%, #dbe1b3 78%, #174b2a 100%);

/* B. Dark — body sections, closers, most content */
background:
  radial-gradient(120% 78% at 14% 6%, rgba(45,110,66,0.58) 0%, rgba(12,39,25,0) 62%),
  linear-gradient(140deg, #1d5730 0%, #123f22 44%, #0c2719 100%);

/* C. Mid-green — repeating series items (officer cards, feature posts) */
background: linear-gradient(140deg, #6f9d6f 0%, #558f61 26%,
  #35744a 58%, #1d5730 84%, #0f3a20 100%);
```

**140° is the house angle** — light top-left, dark bottom-right. Use `140deg` for
full-bleed grounds, `135deg` for the light hero, `145deg` for small card fills.
Never a vertical, horizontal, radial-only, or mesh gradient on a full ground.

Carousels and decks ramp the value: **light cover → mid-green body → dark closer.**

## Typography

One typeface: **Inter Tight**, falling back to SF Pro Display, then Helvetica
Neue. Weight 600 everywhere, 500 for long body copy, 700 for rasterized social and
print (headless Chrome renders 600 thin at display sizes). No italics, no serif,
no mono, no second family. Set `font-synthesis: none` on web so a missing weight
fails loudly instead of faking.

**Everything is lowercase** — headlines, buttons, nav, labels, captions, CTAs.
The only exceptions are human names (`Joel Manuel`) and proper nouns inside body
copy (`Face ID`, `AlphaFold`, `3D`). Never uppercase, never title case, never
small caps. Apply `text-transform: lowercase` only to elements that can never
hold a proper noun; elsewhere type the string lowercase by hand.

**Sizes scale off the short edge.** Let `S = min(canvasWidth, canvasHeight)`.
Every token above is a fixed percentage of S, which is why a 1080×1350 post and
a 1920×1080 slide use identical pixel values:

| Token | % of S | @ S=1080 |
|---|---|---|
| `display-mega` (background word) | 24–44% | 260–475px |
| `display-lg` (closing statement) | 14–16% | 150–172px |
| `headline-title` (cover) | 10–11% | 108–118px |
| `headline-name` (section) | 8.5–9.5% | 92–102px |
| `subhead` (role) | 5.0–5.5% | 54–60px |
| `body-lg` (callout) | 4.5–5.6% | 48–60px |
| `body-md` | 2.6–3.3% | 28–36px |
| `label-eyebrow` | 1.3–1.8% | 14–20px |

On the web the same relationships are expressed as clamps capped on *both* axes
so type never overflows a short laptop viewport:

```css
--hero-type-size: clamp(48px, min(14.5vw, 8.5vh), 76px);
/* section headline */ font-size: clamp(3.2rem, 9.5vw, 8.5rem); line-height: 0.86;
/* lede            */ font-size: clamp(1.05rem, 1.8vw, 1.35rem); line-height: 1.25;
```

**Ratio locks** — these are what make the output feel designed:

- subhead ÷ name = **0.56**
- body ÷ name ≤ **0.60** (supporting text never rivals the headline)
- caption ÷ body ≈ **0.55**
- across a repeating series, headline sizes stay within **±5%**

**The cream text treatment.** On dark grounds, at display sizes only, two effects
always travel together:

```css
background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
```

Those shadow numbers are the brand's signature and are identical across every
asset ever shipped. Never alter them. It must be `filter: drop-shadow`, not
`text-shadow` — it has to trace the glyph outlines. Do not apply it below ~2.5%
of S; small text turns to mud and should be flat cream at reduced opacity.

Body copy caps at **24–27 characters per line**. Headlines get `text-wrap:
balance` plus a manual `<br/>` at the intended break.

## Layout

Text is left-aligned or right-aligned — **never centered**, except a deliberate
full-screen "moment" statement. When a text column sits right of an image, right-
align it: the ragged edge faces the image, the flush edge holds the margin.

Everything derives from S. The panel is inset 2.0% with a 5.2% corner radius and
4%-ish padding; the logo mark is 14.6% of S in-layout and fills 45–60% of the
panel height on a cover.

**Two-column body split** (the workhorse): image `67%` of panel inner width ·
gutter `4%` · text column `29%`. Set the image `flex: 0 0 <px>` and never let it
shrink. The narrow measure is deliberate — copy breaks at 8–11 characters and
stacks into a tall ragged block. Do not widen it to make the text "read better."

**Five layout archetypes.** Pick one per surface; do not blend.

1. **Cover / title** — light ground, dark title top-left, giant logo centered,
   cream kicker bottom-right on the dark corner.
2. **Header + split body** — mid-green ground, logo top-left, name right-aligned
   beside it, then the 67/29 image-and-text split.
3. **Statement** — dark ground, small logo top-left, one huge right-aligned block
   of cream type, vertically centered.
4. **Grid** — dark ground, section headline top-left, lede beneath, then a 4–5
   column card or portrait grid.
5. **Full-bleed moment** — one edge-to-edge image, cream type over the darkest
   corner, no panel.

**Web:** `--page-width: 1440px`, `--page-gutter: clamp(20px, 5vw, 80px)`,
`--nav-height: 72px`.

**Canvas sizes:** IG post 1080×1350 · story 1080×1920 · deck 1920×1080 · print at
300 dpi with S = the short edge. Never 1:1 or 4:3 for social.

## Elevation & Depth

Depth comes from the diagonal value ramp of the ground and from one translucent
panel — not from stacked cards. Maximum nesting is **panel + one image frame**.

Every shadow is green-black. There are three, and they do different jobs:

```css
/* type glow — reads as lift, never as an offset copy of the letters */
filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
/* image frame */
box-shadow: 0 32px 80px rgba(8, 28, 16, 0.75);
/* content card */
box-shadow: 0 1.5rem 4rem rgba(4, 28, 15, 0.2);
```

Borders are a whisper, not a stroke: `1px solid rgba(255, 243, 203, 0.12–0.22)`
on dark, `1px solid rgba(12, 39, 25, 0.12)` on light. At 12–16% opacity the panel
edge should read as a change of light. If you can clearly see a line, it is too
strong.

**Motion** (web and video only):

```css
--motion-fast: 160ms; --motion-base: 220ms; --motion-reveal: 560ms;
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
```

Scroll reveal is `opacity 0→1` plus `translate3d(0, 1.5rem, 0) → 0` over
`--motion-reveal`, staggered 60–80ms per sibling. Hover is a 1px lift or a 1.04
scale over 180–400ms. Nothing bounces, nothing spins. Always honor
`prefers-reduced-motion`. Blur filters cost real frames on mobile — swap
decorative `filter: blur()` for a radial gradient on touch devices.

## Shapes

Very round, never sharp. The panel carries a `56px` radius at S = 1080 (5.2% of
the short edge) — large enough to read as a soft slab rather than a rounded
rectangle. Image frames sit at `40px` (3.7%). Anything interactive and small — 
pills, badges, nav buttons, the experience dock — is a **full 999px pill**. Web
surfaces use `--radius-card: clamp(22px, 3vw, 42px)`.

There are no other shapes. No circles as decoration, no cut corners, no dividers,
no icon shapes.

**The logo** is `logo.png`, 1024×1024 RGBA with clean alpha. Always recolor by CSS
mask — never tint, never `filter: invert`, never re-export a colored PNG:

```css
.logo {
  -webkit-mask: url("logo.png") center / contain no-repeat;
  mask: url("logo.png") center / contain no-repeat;
  background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);  /* on dark */
  filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
}
```

On light grounds the fill becomes `linear-gradient(160deg, #216434, #174b2a 55%,
#0c2719)`. Clear space is at least 0.25× the mark's width on every side. Never
stretch, rotate, outline, or drop it on a busy photo without a scrim.

## Components

**Panel** — the floating container behind nearly every composition. `inset: 22px`,
`border-radius: 56px`, `rgba(255, 249, 230, 0.135)` on dark or
`rgba(12, 39, 25, 0.045)` on light, with the whisper border. One panel, always.

**Image frame** — `border-radius: 40px`, `overflow: hidden`, `2px solid
rgba(255, 243, 203, 0.35)`, `background: #0c2719` behind transparency, and the
house grade on the photo: `filter: contrast(1.04) saturate(1.03)`. Every photo
gets a hand-set `object-position` (eyes on the upper third, no dead headroom).
Source images must be ≥ 2× the rendered box.

**Content card** — a per-card gradient in the sage→forest range so a grid gets
rhythm, plus the ambient shadow:

```css
background: linear-gradient(145deg, rgba(63,122,77,0.98), rgba(24,73,43,0.96));
border: 1px solid rgba(255,243,203,0.16);
border-radius: var(--radius-card);
box-shadow: 0 1.5rem 4rem rgba(4,28,15,0.2);
padding: clamp(1.4rem, 2.2vw, 2.5rem);
```

**Pill / badge / nav button** — `border-radius: 999px`, lowercase, translucent
cream fill at 12% with a 22% cream border and `backdrop-filter: blur(6px)`.
Hover and active **invert** to solid cream with deep-forest text.

**Eyebrow** — the tiny lowercase label above a headline. `letter-spacing: 0.14em`
is the only wide tracking in the system, at 58% cream.

**Mega background word** — one huge word behind content at `opacity: 0.15`,
`letter-spacing: -0.08em`, `line-height: 0.7`, `pointer-events: none`. Once per
page, maximum.

**Copy voice** is part of the component set. Lowercase, short, declarative.
Ask a question and answer it in enormous type: *"what's even possible?"* Talk
about what got built, never about the mission statement. CTAs are verbs: *"join
aitc"*, *"see whats possible"*. No em-dashes in headlines — break the line instead.

## Do's and Don'ts

- **Do** derive every dimension from S, the canvas short edge, so the system ports
  between post, slide, and page unchanged.
- **Do** go bigger when in doubt. An agent's default type size is roughly half of
  what this brand wants; a headline that looks too big is probably correct.
- **Do** tighten tracking and leading as size grows — that pairing *is* the brand.
- **Do** keep the exact glow `drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81))`
  on display type over dark grounds.
- **Do** mask the logo to recolor it.
- **Do** open the rendered output and look at it. Layout bugs in this system are
  invisible in code and obvious in the image.
- **Don't** use pure white or pure black. Cream is the white, `#0c2719` is the black.
- **Don't** introduce a second typeface, a weight outside 500/600/700, or italics.
- **Don't** uppercase or title-case anything. Human names and proper nouns keep
  their real capitalization; everything else is lowercase.
- **Don't** nest a card inside a card inside a card. Panel plus one frame is the max.
- **Don't** place text on the sage bridge band (`#dbe1b3` / `#d5dfb0`).
- **Don't** run a gradient vertically or horizontally on a full ground — 135–145°,
  light top-left.
- **Don't** let supporting text approach the headline size (≤ 0.60×).
- **Don't** center body text, and don't widen the 29% text column to help it read.
- **Don't** use wide letter-spacing anywhere except eyebrows and captions.
- **Don't** add stock illustration, emoji as iconography, gradient meshes,
  glassmorphism beyond the one panel, or neutral-gray shadows.
- **Don't** ship 1:1 or 4:3 for social. Portrait (4:5, 9:16) or 16:9.
