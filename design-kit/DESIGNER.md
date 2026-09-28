# AITC — DESIGNER.md

**Prompt pack for AI design tools.** Google Stitch, Figma Make, v0, Lovable, Claude Artifacts, Midjourney, Canva Magic. Paste the blocks below verbatim.

Companion file: `BRAND.md` — the engineering spec (exact CSS, math, render pipeline). This file is the *natural-language* version, because design tools read prose, not stylesheets. Where the two disagree, `BRAND.md` wins.

**Honest note on Stitch:** Stitch generates **app and web UI screens**. It is excellent for a site, a member dashboard, an event page, a mobile app. It is *not* a social-post generator — it will not reproduce the carousel look, because that depends on masked logos, gradient-clipped text, and hand-set photo crops that Stitch does not expose. For posts, keep `generate_ig_posts.py`. Use §5 here for image-generation tools instead.

---

## 0. How to use this with Google Stitch

1. Open Stitch → new project.
2. **Upload reference images first** (§4 tells you which). Stitch weights uploaded images heavily; this is the single biggest quality lever.
3. Paste **§1, the master theme prompt**, as your first message. Do not summarize it — paste all of it.
4. Then paste one **screen prompt** from §3 per screen you need.
5. Generate, then run the **§6 fix list**. Stitch will get 4 specific things wrong every time.
6. Export to Figma or code, then map values back to real tokens using §7.

Same flow for Figma Make / v0 / Lovable: §1 becomes the system prompt, §3 the per-page prompt.

---

## 1. MASTER THEME PROMPT — paste this first, in full

```
Design system: AITC (AI Technology Club, Enloe High School). Tagline "build with ai. create whats next."

VIBE
Confident, oversized, editorial. Think a modern sportswear brand crossed with an Apple keynote slide. Calm, spacious, expensive. Not playful, not techy, not corporate, not "startup". Zero clutter. Empty space is the point — do not fill it.

COLOR — use only these
Cream #FFF3CB — the primary light background, and the primary text color on dark backgrounds.
Soft cream #F4E8B8 — secondary text on dark, and the lower half of cream gradients.
Forest #216434 — mid green, the brand color, used as text on cream backgrounds.
Deep forest #0C2719 — the darkest color. This is the "black" of the system. Page backgrounds, image backings, headline text on cream.
Mid forest #174B2A — gradient stop between forest and deep forest.
Sage #8DAD82 and #DBE1B3 — only ever appear inside gradients as a transition step, never as a flat fill, and never behind text.
Ink #2B7244 — body and headline text on cream backgrounds.

Never pure white, never pure black, never gray, never any other hue. Cream is the white. Deep forest is the black. There is no accent color — when something needs to pop, it becomes cream on deep forest. All shadows are green-black (rgba(4,28,15,·)), never neutral gray.

BACKGROUNDS — every surface is one of exactly three
1. Light: a 135° diagonal gradient that stays cream for the first half, passes through sage, and drops into forest green in the bottom-right corner, with a soft dark radial glow anchored at that corner. Dark text lives top-left, cream text lives bottom-right on the dark part. This two-tone split is deliberate.
2. Dark: flat deep forest #0C2719, optionally with a soft green radial glow in the upper-left.
3. Mid-green: a 140° gradient from a light sage-green top-left through mid greens to near-black forest bottom-right.

Gradients always run diagonally, roughly 135–145°, light in the top-left, dark in the bottom-right. Never vertical, never horizontal, never radial-only, never a mesh.

TYPOGRAPHY — this is the personality, get it right
One typeface only: Inter Tight (fall back to SF Pro Display, then Helvetica Neue). Weight 600 for everything, 500 for long body copy. No other family, no italics, no serif, no monospace, no display faces.

Everything is lowercase. Headlines, buttons, navigation, labels, captions, calls to action — all lowercase. "build with ai." "what's even possible?" "join aitc." The only exceptions are human names (Joel Manuel) and proper product nouns inside a sentence (Face ID, iPhone, Wikipedia, 3D). Never uppercase, never title case, never small caps.

Type is MUCH larger than a normal design system. Section headlines run 8–12% of the screen's short edge — on a 1080px-tall screen that is a 100–130px headline. Hero statements go bigger still. If a headline looks too big, it is probably correct.

Letter-spacing tightens as size grows, and this is mandatory:
  huge display type: -0.08em
  large display: -0.04em
  headlines: -0.03em
  subheads: -0.025em
  body: -0.015em
  tiny lowercase labels: +0.04em to +0.14em (the only wide tracking in the system)

Line-height tightens the same way: 0.86 for headlines, 0.94–1.0 for display, 1.15–1.25 for body. Headlines are set solid or tighter — lines nearly touch.

Body copy never exceeds 24–27 characters per line.

Supporting text must never rival the headline: subheads are 0.56× the headline size, body is at most 0.60×.

LAYOUT
Text is left-aligned or right-aligned, never centered — the only exception is a deliberate full-screen "moment" statement.

Most compositions sit inside a single rounded container: a large rounded rectangle inset about 2% from the edge of the canvas, corner radius roughly 5% of the short edge (very round, ~56px on a 1080px canvas), filled with a barely-there translucent wash (about 13% cream over dark grounds, 4% deep-forest over light grounds) and edged with a whisper-thin border at ~14% opacity. The border should be almost invisible — a suggestion of an edge, not a stroke.

Never nest a card inside a card inside a card. Maximum depth is that one container plus one image frame.

Images sit in rounded frames — corner radius ~4% of the short edge, a thin translucent cream border, and a large soft green-black drop shadow beneath. Photos are cropped tight: eyes on the upper third, no dead headroom, subject filling the frame.

Buttons and badges are fully rounded pills (radius 999px), lowercase, small, with a translucent cream fill and a thin cream border. On hover they invert to solid cream with deep-forest text.

Tiny labels ("eyebrows") sit above headlines: very small, lowercase, wide letter-spacing, cream at about 58% opacity.

MOTION (if animated)
Content reveals by fading in while rising ~1.5rem, over 560ms, easing cubic-bezier(0.23, 1, 0.32, 1), staggered 60–80ms between siblings. Hovers are subtle: a 1px lift or a 1.04 scale over 180–400ms. Nothing bounces, nothing spins.

VOICE
Short, lowercase, declarative, confident. Ask a question then answer it in enormous type: "what's even possible?" Talk about things that got built, never about mission statements. Calls to action are verbs: "join aitc", "see whats possible". No corporate language, no buzzwords, no exclamation stacking except as one deliberate warm beat.

FORBIDDEN
No uppercase. No second font. No gray. No pure white or black. No centered body text. No cards inside cards. No stock illustration, no emoji as icons, no glassmorphism beyond the one container, no neon, no mesh gradients, no drop shadows in neutral gray, no small text.
```

---

## 2. Quick reference card

Keep this open while reviewing what the tool gives back.

| | |
|---|---|
| **Fonts** | Inter Tight 600 (headlines), 500 (body). One family, period. |
| **Case** | lowercase everything, except human names + proper nouns |
| **Light bg** | `#FFF3CB` → `#DBE1B3` → `#174B2A`, 135°, dark radial bottom-right |
| **Dark bg** | `#0C2719` |
| **Mid bg** | `#6F9D6F` → `#35744A` → `#0F3A20`, 140° |
| **Text on dark** | `#FFF3CB` (body at 66–78% opacity) |
| **Text on light** | `#2B7244` headline, `#0C2719` display |
| **Headline size** | 8–12% of the short edge |
| **Subhead** | 0.56 × headline |
| **Body** | ≤ 0.60 × headline, max 27 characters wide |
| **Tracking** | −0.08em huge → −0.03em headline → −0.015em body → +0.14em micro-label |
| **Leading** | 0.86 headline, 1.20 body |
| **Container radius** | ~5% of short edge |
| **Image radius** | ~4% of short edge |
| **Pills** | radius 999px |
| **Shadow** | large, soft, green-black — never gray |
| **Nesting** | max 2 levels |

---

## 3. Screen prompt library

Append any of these after the §1 theme prompt. One per screen.

**Landing hero**
```
A full-viewport hero on the light diagonal gradient background. A four-line headline set flush left, filling the left two-thirds of the screen, at roughly 76px on desktop, weight 600, letter-spacing -0.03em, line-height 0.94, in ink green #2B7244 — the last two lines drop to 75% opacity. Text reads:
build
with ai.
create
whats next.
A small lowercase eyebrow label sits above it. In the bottom-left corner, the AITC logo mark at about 160px. In the bottom-right corner, two right-aligned lowercase calls to action stacked vertically: "join aitc" large and cream, "see whats possible" below it, smaller and cream at 48% opacity. Fixed transparent top navigation: lowercase wordmark "aitc" at the left, three lowercase links and one outlined pill button "join" at the right. Enormous empty space in the middle. Do not add imagery, icons, or decoration.
```

**Content section with a card grid**
```
A section on the flat deep-forest background. Top-left: a tiny lowercase wide-tracked eyebrow, then a two-line headline in cream at roughly 8.5rem, weight 600, letter-spacing -0.03em, line-height 0.86, with a manual line break. Beneath it a short lowercase lede in cream at 76% opacity, capped at 24 characters wide. Below, a four-column grid of tall cards with generous gaps. Each card is a 145° green gradient (light sage-green to deep forest, varying slightly per card), a thin cream border at 16% opacity, very rounded corners, and a large soft green-black shadow. Inside each card, top-aligned: a large lowercase card title, a tiny wide-tracked subtitle beneath it, then a short paragraph capped at 26 characters wide, then a rounded pill badge. The lower half of each card holds one rounded image area. Left-aligned throughout. No icons.
```

**Team / people grid**
```
A section on deep forest. Left-aligned cream headline at 8.5rem, line-height 0.86. Below, a five-column grid of people. Each person is a portrait image in a rounded rectangle with aspect ratio 0.78, thin translucent cream border, soft dark shadow, cropped so the eyes sit on the upper third. Beneath each portrait, left-aligned: the person's name in cream, lowercase, about 1.4rem, weight 600, letter-spacing -0.025em; below it their role in soft cream #F4E8B8, tiny, lowercase, letter-spacing 0.04em. Nothing centered. No cards around the people — the portrait and the two lines of text sit directly on the background.
```

**Statement / full-screen moment**
```
A full-screen section on deep forest with a soft green radial glow in the upper-left corner. A small cream AITC logo mark in the top-left corner at about 15% of the screen height. One enormous block of cream lowercase text, right-aligned, vertically centered, filling most of the frame — roughly 15% of the screen's short edge in size, weight 600, letter-spacing -0.04em, line-height 0.98, wrapping onto five or six lines with a ragged left edge and a flush right edge. Nothing else on the screen. No buttons, no decoration, no supporting text.
```

**Event / detail page**
```
Deep forest background. A rounded container inset from the edges with a barely-visible translucent cream wash and whisper-thin border. Inside, top row: small cream AITC logo mark on the left, and to its right the event name right-aligned in large cream lowercase type with the date beneath it at 0.56× that size. Below, a two-column split: on the left a rounded image at about two-thirds width; on the right a narrow right-aligned column of lowercase cream copy. A rounded pill call-to-action at the bottom right. Left column and right column separated by a generous gutter. No nested cards.
```

**Mobile app screen**
```
A mobile screen on deep forest. Fixed lowercase header with the wordmark "aitc" left and a small pill button right. Content is a vertical stack of very tall rounded cards, each a 145° green gradient with a thin cream border, generous internal padding, a large lowercase title, a tiny wide-tracked subtitle, a short paragraph, and a rounded image area. Bottom tab bar with lowercase text labels and no icons — the labels alone. Everything lowercase, everything left-aligned, type noticeably larger than a typical mobile app.
```

**Dashboard**
```
Deep forest background, cream text. Left sidebar with a lowercase wordmark and lowercase nav labels at 72% opacity, the active one at full opacity. Main area: a very large lowercase page title at the top-left with tight negative tracking, then a grid of stat cards — each a subtle green gradient with a thin cream border and very rounded corners, containing one enormous number in cream with tight tracking and a tiny wide-tracked lowercase label beneath it. The numbers should be dramatically oversized relative to their labels. Tables use lowercase headers, cream text at reduced opacity, thin cream row dividers at 12% opacity, and no vertical rules. No icons, no color-coded status chips other than cream pills.
```

---

## 4. Reference images — upload these

From `instagram_board_posts/`. Uploading beats describing.

| Upload | What it teaches the tool |
|---|---|
| `00_cover.png` | The light gradient, the two-tone dark/cream text split, logo scale, the cream-into-forest corner fall |
| `01_joel.png` | The mid-green ground, the container, header logo + right-aligned name/role, the image frame, the narrow right-hand text column |
| `07_outro.png` | Dark ground, oversized right-aligned type, ragged-left wrapping, correct type-to-canvas ratio |
| `logo.png` | The mark itself — **upload for reference only.** AI tools will redraw it wrong. Composite the real file in afterward. |

Ask the tool to "match the typography scale, color, and spacing of the attached images."

---

## 5. Image-generation prompt (Midjourney / DALL·E / Firefly / Canva)

For moodboards and backgrounds only. Never for anything containing text or the logo — generators cannot set type and cannot draw the mark.

```
Minimalist editorial graphic design, deep forest green and warm cream palette, smooth 140-degree diagonal gradient from soft sage green in the upper left to near-black forest green in the lower right, large soft rounded rectangle floating with a barely visible lighter edge, generous negative space, calm and expensive, no text, no logo, no people, matte finish, subtle grain, flat modern art direction --ar 4:5
```

Swap `--ar 4:5` for `--ar 16:9` (slides) or `--ar 9:16` (stories).

---

## 6. Fix list — what these tools get wrong every single time

Run this after every generation. In order of how often it happens.

1. **Type is too small.** By far the most common failure. Every AI design tool reverts to a conventional 48–64px headline. AITC headlines are 100–130px on a 1080px-tall canvas. Scale headlines up until they feel slightly uncomfortable, then keep them.
2. **Capitalization creeps back in.** Buttons become "Join AITC", nav becomes "Home / About". Force everything back to lowercase, then restore the capitals on human names and proper nouns only.
3. **Letter-spacing goes to zero or positive.** Tools default to normal tracking. Reapply the ladder: −0.03em at headline size, tighter as it grows.
4. **A gray or a fourth color appears** — a neutral shadow, a `#333` body text, a blue link, a red error state. Replace with the green-black or cream equivalents.
5. **Nested cards.** A card inside a section inside a container. Flatten to two levels.
6. **Icons appear.** This system has no icon set. Delete them; text labels alone.
7. **Body text gets centered.** Left- or right-align it.
8. **The container border becomes a visible stroke.** Drop it to ~14% opacity so it reads as an edge, not a line.
9. **Line-height loosens.** Headlines must be set at 0.86–1.0, not 1.4.
10. **The logo is redrawn.** Always replace with the real `logo.png`, masked to a solid brand color.

---

## 7. Handoff — bringing generated output back into code

Whatever a tool exports, map its values onto the real tokens before merging. Never ship generated hex values.

```css
:root {
  --cream: #fff3cb;  --cream-soft: #f4e8b8;  --cream-hi: #fff9e6;
  --forest: #216434; --forest-mid: #174b2a;  --forest-deep: #0c2719;
  --forest-light: #8dad82; --ink: #2b7244;
  --muted-ink: rgba(33, 100, 52, 0.62);
  --font: 'Inter Tight', -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
  --page-gutter: clamp(20px, 5vw, 80px);
  --page-width: 1440px;
  --radius-card: clamp(22px, 3vw, 42px);
  --motion-fast: 160ms; --motion-base: 220ms; --motion-reveal: 560ms;
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
}
```

Three things a design tool cannot produce, which must be added by hand:

**The logo.** Always a CSS mask over the real PNG, never a colored image file:
```css
.logo {
  background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
  -webkit-mask: url("logo.png") center / contain no-repeat;
  mask: url("logo.png") center / contain no-repeat;
}
```

**The signature text treatment** — cream gradient fill plus forest glow, on display type over dark grounds only. The shadow values are fixed and never change:
```css
background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
```

**Photo crops.** Every image needs a hand-set `object-position`, plus a `transform: scale()` when the subject sits small in frame. No tool will do this correctly.

Then read `BRAND.md` §12 (hard rules) and §13 (pre-ship checklist) before shipping.
