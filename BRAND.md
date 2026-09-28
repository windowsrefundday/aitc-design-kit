# AITC Brand & Design System

**Audience: an AI agent.** Read this whole file before producing anything visual for AITC — Instagram post, website, slide deck, poster, email header, video title card, merch mock, PDF. Follow it literally. If you follow it, the output looks native. If you improvise, it does not.

AITC = the AI Technology Club at Enloe High School. Tagline: **build with ai. create whats next.**

Repo assets (if this file ships inside `aitc-parallax`, use the real files; otherwise recreate from the specs below):

| Asset | Path | Notes |
|---|---|---|
| Logo | `logo.png` | 1024×1024 RGBA. Solid alpha, no baked color — **use as a mask, never as a colored image.** |
| Site tokens | `styles.css` | `:root` block is the canonical token source |
| Site markup | `index.html` | canonical copy voice + section order |
| Post generator | `generate_ig_posts.py` | canonical implementation of everything below |
| Reference output | `instagram_board_posts/*.png` | the look you are matching |

---

## 0. The one-paragraph summary

Cream on forest green. One typeface, one weight-ish, all lowercase except human names and product names. Type is **enormous** and **tightly tracked** — that is the whole personality. Layout is a rounded translucent panel floating inside a diagonal gradient, with generous inset. Nothing is centered except deliberate "moment" slides. Never more than one card inside another. Text on dark grounds gets a cream gradient fill plus a forest-green glow. Empty space is a feature; do not fill it.

---

## 1. Color

### 1.1 Tokens (exact — never eyeball these)

```css
:root {
  --cream:        #fff3cb;  /* primary light ground + primary text on dark */
  --cream-soft:   #f4e8b8;  /* gradient partner for cream, secondary text on dark */
  --cream-hi:     #fff9e6;  /* top stop of the cream text gradient only */
  --forest:       #216434;  /* mid brand green, ink on light grounds */
  --forest-mid:   #174b2a;  /* deep green, gradient stop */
  --forest-deep:  #0c2719;  /* darkest — page ground, image-frame backing */
  --forest-light: #8dad82;  /* sage, only for card gradients + light-ground steps */
  --ink:          #2b7244;  /* body/headline color on cream grounds */
  --muted-ink:    rgba(33, 100, 52, 0.62);  /* secondary text on cream */
}
```

Extra stops used in gradients (not tokens, but exact): `#dbe1b3` (sage bridge), `#d5dfb0`, `#6f9d6f`, `#558f61`, `#35744a`, `#1d5730`, `#123f22`, `#0f3a20`, `#082810`.

### 1.2 Text-on-ground pairings — memorize this table

| Ground | Primary text | Secondary text | Notes |
|---|---|---|---|
| Cream / light gradient | `--ink` `#2b7244` | `--muted-ink` | Never cream text here. Never pure black. |
| Forest deep / mid / green gradient | `--cream` | `rgba(255,243,203, .66–.78)` | Add the cream gradient fill + glow (§4.4) at display sizes. |
| Sage bridge band (`#dbe1b3`, `#d5dfb0`) | **neither reads** | — | Never place text on the bridge band. Push a gradient stop under it or move the text. |

Secondary-text opacity ladder on dark: `.90` card copy → `.78` lede → `.68` caption → `.58` whisper → `.45` footer.

### 1.3 Rules

- Two families only: cream and forest. No blue, no orange, no red, no gray. Grays are always tinted forest.
- Never pure white (`#fff`) and never pure black (`#000`). Cream is the white; `--forest-deep` is the black.
- Accent = the *contrast jump*, not a third hue. If something needs to pop, put cream on `--forest-deep`.
- Borders on dark: `1px solid rgba(255,243,203, 0.12–0.22)`. Borders on light: `1px solid rgba(12,39,25, 0.12)`.
- Shadows are always green-black, never neutral: `rgba(4,28,15,·)`, `rgba(8,28,16,·)`, `rgba(12,39,25,·)`.

---

## 2. The three canonical grounds

Every AITC surface is one of these three. Pick one per screen/slide/section; do not invent a fourth.

**A. Light ground** — hero, cover slides, title cards, anything that opens.
```css
background:
  radial-gradient(circle at 100% 100%,
    rgba(12, 39, 25, 0.96) 0%,
    rgba(33, 100, 52, 0.68) 24%,
    rgba(255, 243, 203, 0) 68%),
  linear-gradient(135deg, #fff3cb 0%, #fff3cb 56%, #dbe1b3 78%, #174b2a 100%);
```
Cream 56% of the way, then it falls into forest in the bottom-right corner. Dark type top-left, cream type bottom-right. That two-tone split is intentional — lean into it, do not neutralize it.

For a punchier print/social version, push the radial to `circle at 102% 103%` with an opaque center and move the linear's cream stop to `50%`.

**B. Dark ground** — body sections, closing slides, most content.
```css
background: #0c2719;
/* optional depth: */
background:
  radial-gradient(120% 78% at 14% 6%, rgba(45,110,66,0.58) 0%, rgba(12,39,25,0) 62%),
  linear-gradient(140deg, #1d5730 0%, #123f22 44%, #0c2719 100%);
```

**C. Mid-green gradient ground** — repeating series items (officer cards, feature posts, stat cards). Same layout every time, so the gradient carries the rhythm.
```css
background: linear-gradient(140deg,
  #6f9d6f 0%, #558f61 26%, #35744a 58%, #1d5730 84%, #0f3a20 100%);
```
**140° is the house angle.** Light in the top-left, dark in the bottom-right. Use `140deg` for full-bleed grounds and `135deg` for the light hero; `145deg` for small card fills. Never a vertical or horizontal gradient on a full ground.

Sequencing rule for carousels/decks: **light cover → mid-green body → dark closer.** The value ramp is the narrative.

---

## 3. Proportion — scale everything off the short edge

This is the most important section. AITC design reads "big" because element sizes are a large fraction of the canvas, and because those fractions are constant across media.

Let **S = the shorter edge of the canvas** (1080 for a 1080×1350 post, 1080 for a 1920×1080 slide, `min(100vw,100vh)` on web). Every size below is a percentage of S. A 1920×1080 slide and a 1080×1350 post therefore use **identical pixel values** — that is why the system ports.

```
S = min(width, height)
```

| Element | % of S | @ S=1080 |
|---|---|---|
| Outer panel inset | 2.0% | 22px |
| Panel corner radius | 5.2% | 56px |
| Panel padding (top / x / bottom) | 4.3 / 3.9 / 3.9% | 46 / 42 / 42px |
| Logo mark (in-layout) | 14.6% | 158px |
| Logo → text gap | 2.6% | 28px |
| Header → body gap | 3.1% | 34px |
| Image frame radius | 3.7% | 40px |
| Column gutter | 3.3% | 36px |
| Hero logo (cover slide) | fills 45–60% of panel height | — |

**Two-column body split** (image + text, the workhorse layout):
image `67%` of panel inner width · gutter `4%` · text column `29%`. Set the image with `flex: 0 0 <px>` — never let it shrink.

**Type scale** (also % of S — see §4 for treatment):

| Role | % of S | @1080 | Tracking |
|---|---|---|---|
| Mega display (background word) | 24–44% | 260–475px | −0.08em |
| Display / closing statement | 14–16% | 150–172px | −0.04em |
| Title / cover headline | 10–11% | 108–118px | −0.045em |
| Name / section headline | 8.5–9.5% | 92–102px | −0.035em |
| Kicker | 8.5–9% | 92–96px | −0.04em |
| Subhead / role | 5.0–5.5% | 54–60px | −0.035em |
| Body / callout | 4.5–5.6% | 48–60px | −0.035em |
| Small body | 2.6–3.3% | 28–36px | −0.02em |
| Eyebrow / caption | 1.3–1.8% | 14–20px | +0.035em … +0.14em |

**Ratio locks** (enforce these, they are what makes it feel designed):
- subhead ÷ name = **0.56**
- body ÷ name ≤ **0.60** — supporting text must never rival the name
- caption ÷ body ≈ **0.55**
- In a repeating series, the name/headline size must be **near-identical across items** (±5%). Type that jumps between slides is the #1 tell of a generated set. Autofit (§4.6) with a tight floor.

**Web equivalents.** Use the site's own clamps rather than raw px:
```css
--page-gutter: clamp(20px, 5vw, 80px);
--page-width: 1440px;
--radius-card: clamp(22px, 3vw, 42px);
--hero-type-size: clamp(48px, min(14.5vw, 8.5vh), 76px);
/* section headline */ font-size: clamp(3.2rem, 9.5vw, 8.5rem); line-height: 0.86;
/* lede         */ font-size: clamp(1.05rem, 1.8vw, 1.35rem); line-height: 1.25;
```
The `min(Xvw, Yvh)` pattern is deliberate: type is capped by *both* axes so it never overflows a short laptop viewport.

---

## 4. Typography

### 4.1 Family

```css
font-family: 'Inter Tight', -apple-system, BlinkMacSystemFont,
             "SF Pro Display", "SF Pro Text", "Helvetica Neue", Helvetica, Arial, sans-serif;
```
Web → Inter Tight first. Local render (headless Chrome on macOS, Keynote, print) → put `"SF Pro Display"` first; it is the metric the reference posts were built on. Never a serif, never a mono, never a display/script face. One family, everywhere.

Always set `font-synthesis: none;` on web so a missing weight fails loudly instead of faking.

### 4.2 Weight

600 on web. 700 for rasterized social/print (headless Chrome renders 600 thin at large sizes). 500 for body/lede on web. That is the entire weight palette — no 300, no 900, no italics anywhere.

### 4.3 Case — the lowercase rule

**Everything is lowercase.** Headlines, roles, buttons, nav, captions, CTAs, section titles. `"build with ai."` `"what's even possible?"` `"president/founder of aitc"` `"fun fact: i'm double-jointed."`

**Exceptions — these keep their real capitalization:**
- Human names: `Joel Manuel`, `Aarit Srivastava`
- Product and proper nouns inside body copy: `Face ID`, `iPhone`, `Kingdom Hearts`, `Ken Carson`, `Wikipedia`, `AlphaFold`, `3D`
- `AITC` in `alt` text and accessibility labels (visually it is the mark or lowercase `aitc`)

Implementation: write the string in its true case, then apply `text-transform: lowercase` **only** to elements that never hold a proper noun (roles, eyebrows, captions, nav). For body copy that may contain a proper noun, do **not** use `text-transform` — type the string lowercase by hand and leave the proper nouns capitalized.

Never `UPPERCASE`. Never Title Case. Never small-caps.

### 4.4 The cream text treatment (on dark grounds, display sizes only)

Two effects, always together:

```css
/* vertical cream gradient fill */
background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;

/* forest glow — 150.8°, 39px blur, 23px distance, 81% opacity */
filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
```

**Never alter those shadow numbers.** They are the brand's signature and they are consistent across every asset ever shipped. Note it is `filter: drop-shadow`, not `text-shadow` — it must trace the glyph outlines, and `text-shadow` is disabled by `-webkit-text-fill-color: transparent` anyway.

Apply to: display, title, name, kicker, subhead, large callouts. **Do not apply** to small body, captions, eyebrows, or any text below ~2.5% of S — it turns to mud. Small text on dark is flat `--cream` at reduced opacity.

Web CTA variant (cheaper, no clip): flat `--cream` plus
```css
text-shadow: 0 4px 16px rgba(10,38,20,0.4), 0 16px 40px rgba(10,38,20,0.3);
```

On **light** grounds the equivalent is flat `--forest-deep` or `--ink` with a soft green shadow:
```css
color: #0c2719;
filter: drop-shadow(7px 13px 28px rgba(12, 39, 25, 0.22));
```

### 4.5 Line-height and tracking ladder

Bigger type ⇒ tighter tracking **and** tighter leading. Non-negotiable.

| Size band | line-height | letter-spacing |
|---|---|---|
| Mega display | 0.70–0.82 | −0.08em |
| Display | 0.94–0.98 | −0.04em |
| Title / name | 0.86–1.00 | −0.03 … −0.045em |
| Subhead | 1.03–1.08 | −0.025 … −0.035em |
| Body | 1.15–1.25 | −0.015 … −0.02em |
| Caption / eyebrow | 1.0–1.15 | +0.035 … +0.14em |

Line-length cap on body copy: `max-width: 24ch–27ch`. Headlines get `text-wrap: balance` and manual `<br/>` at the intended break.

### 4.6 Autofit — how type stays big without overflowing

Do not guess a font size that fits. Start at the design size and shrink until it fits, with a floor that keeps it big. Run before rasterizing.

```js
// single-line: shrink on width only. NEVER also test height —
// line-box rounding makes the height test fail forever and collapses the size.
function fitWidth(el, start, min) {
  if (!el) return start;
  for (var s = start; s >= min; s -= 1) {
    el.style.fontSize = s + 'px';
    if (el.scrollWidth <= el.clientWidth + 1) return s;
  }
  return min;
}

// multi-line block: shrink on the container's available height
function fitBlock(el, box, start, min) {
  for (var s = start; s >= min; s -= 1) {
    el.style.fontSize = s + 'px';
    if (el.scrollHeight <= box.clientHeight) return s;
  }
  return min;
}

var nameSize = fitWidth(document.querySelector('.name'), 100, 78);   // floor = 78% of start
fitWidth(document.querySelector('.role'), Math.round(nameSize * 0.56), 38);
```

Two gotchas that will bite you:
- The measured element must **stretch** to its container. With `align-items: flex-end` (or any shrink-to-fit) `scrollWidth === clientWidth` always, and the loop never shrinks. Use `align-items: stretch` + `text-align: right`.
- Single-line elements need `white-space: nowrap`, or they wrap instead of failing the width test, and you get a two-line role on one card and a one-line role on the rest.

---

## 5. Logo

`logo.png` — 1024×1024 RGBA, clean alpha (edge antialiasing only, no baked glow).

**Always recolor via CSS mask. Never tint, never `filter: invert`, never re-export a colored PNG.**

```css
.logo {
  width: 158px; height: 158px;            /* 14.6% of S */
  background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);  /* cream, on dark */
  -webkit-mask: url("logo.png") center / contain no-repeat;
  mask: url("logo.png") center / contain no-repeat;
  filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
}
```

Fills by ground:
- On dark → the cream gradient above, with the standard glow.
- On light → `linear-gradient(160deg, #216434 0%, #174b2a 55%, #0c2719 100%)` with `drop-shadow(12px 20px 38px rgba(12,39,25,0.34))`.
- Flat single color is acceptable at small sizes: `background-color: var(--cream)` / `var(--forest-deep)`.

Placement and size:
- In-layout mark (header of a content slide, nav, footer): **14.6% of S**, top-left, aligned to the panel padding.
- Hero / cover mark: the star. Let it fill **45–60% of the panel height** (`flex: 1 1 auto; min-height: 0`). On the site it is bottom-left of the hero at `clamp(68px, 15vw, 160px)`.
- Clear space: at least **0.25× the mark's width** on every side. Nothing crosses it.
- Never stretch (always `contain`), never rotate, never outline, never drop it on a busy photo without a scrim.

Performance note if you animate near it: give the masked element `transform: translateZ(0)` so the 1024² mask resolves once instead of on every repaint.

---

## 6. Photography & imagery

**Frame** (portraits, product shots, screenshots):
```css
.frame {
  border-radius: 40px;                              /* 3.7% of S; web: var(--radius-card) */
  overflow: hidden;
  border: 2px solid rgba(255, 243, 203, 0.35);      /* on dark; 1px at web scale */
  box-shadow: 0 32px 80px rgba(8, 28, 16, 0.75);
  background: #0c2719;                              /* backing shows through transparency */
}
.frame img {
  width: 100%; height: 100%; object-fit: cover; display: block;
  filter: contrast(1.04) saturate(1.03);            /* the house grade */
}
```
Web portrait tiles use `aspect-ratio: 0.78`, `border-radius: clamp(16px, 2.2vw, 24px)`, `box-shadow: 0 16px 36px rgba(0,0,0,0.35)`, `filter: contrast(1.04) brightness(0.96)`, and lift to `scale(1.04)` on hover over `400ms cubic-bezier(0.16,1,0.3,1)`.

**Cropping.** Every photo gets a hand-set `object-position`, and a `transform: scale()` + `transform-origin` when the subject is small in frame:
```html
<img style="object-position: 50% 100%; transform: scale(1.42); transform-origin: 50% 62%;" />
```
Target: eyes on the upper third, shoulders in frame, no forehead crop, minimal dead headroom. Phone shots (9:16) usually need `object-position: 50% 100%` plus a 1.2–1.5× zoom.

**Flex trap:** a flex item defaults to `min-height: auto`, so a tall source image will refuse to shrink and will punch through the panel's rounded bottom. Always put `min-height: 0` on both the flex row **and** the frame, plus `height: 100%` on the frame.

Source resolution: at least 2× the rendered box. Anything under ~600px on the long edge will look visibly soft at post scale — say so rather than shipping it silently.

---

## 7. Components

**Panel** — the floating container that defines nearly every AITC composition.
```css
.panel {
  position: absolute; inset: 22px;         /* 2% of S */
  border-radius: 56px;                     /* 5.2% of S */
  background: rgba(255, 249, 230, 0.135);  /* on dark  */
  border: 1px solid rgba(255, 249, 230, 0.14);
  padding: 46px 42px 42px;
  display: flex; flex-direction: column;
}
/* on a light ground, invert it */
.panel--light { background: rgba(12,39,25,0.045); border-color: rgba(12,39,25,0.12); }
```
One panel. **Never a card inside a card inside a card.** The panel plus one image frame is the maximum nesting depth.

**Content card** (web/deck grids):
```css
background: linear-gradient(145deg, rgba(63,122,77,0.98), rgba(24,73,43,0.96));
border: 1px solid rgba(255,243,203,0.16);
border-radius: var(--radius-card);
box-shadow: 0 1.5rem 4rem rgba(4,28,15,0.2);
padding: clamp(1.4rem, 2.2vw, 2.5rem);
```
Vary the two gradient stops per card to give a grid rhythm; keep them all in the sage→forest range.

**Pill / badge**:
```css
border-radius: 999px;
padding: 0.25rem 0.75rem;                       /* badge */
padding: 8px 13px;                              /* nav button */
font-size: clamp(0.68rem, 1.2vw, 0.8rem);
font-weight: 600; letter-spacing: 0.04em;
color: #f4e8b8;
background: rgba(255,243,203,0.12);
border: 1px solid rgba(255,243,203,0.22);
backdrop-filter: blur(6px);
```
Hover/active inverts: `color: var(--forest-deep); background: var(--cream);`

**Eyebrow / whisper** — the tiny lowercase label above a headline:
```css
font-size: 0.76rem; font-weight: 600;
letter-spacing: 0.14em;              /* the ONLY place tracking goes wide */
text-transform: lowercase;
color: rgba(255,243,203,0.58);
```

**Mega background word** — a huge word behind content at `opacity: 0.15`, `letter-spacing: -0.08em`, `line-height: 0.7`, `pointer-events: none`, `user-select: none`. Use once per page maximum.

---

## 7.5 Signatures — what the rendered output actually looks like

Read off the shipped PNGs in `instagram_board_posts/`. These are the tells that separate a native asset from a close-but-wrong one.

- **The narrow text column.** In the split layout the right-hand column is only ~29% of the panel width, so copy breaks at roughly **8–11 characters per line** and stacks into a tall ragged block — flush right, ragged left, sitting hard against the image's gutter. That extreme measure is intentional. Do not widen the column to make the text "read better"; the stack is the look.
- **The border is a whisper.** At 12–16% opacity the panel edge is barely perceptible in the render — it reads as a change of light, not a drawn line. If you can clearly see a stroke, it is too strong.
- **The glow reads as depth, not as shadow.** At 39px blur and 81% opacity over a green ground, the drop-shadow does not look like a shadow — it looks like the type is lifted off the surface. It should never be legible as an offset copy of the letters.
- **Words nearly touch.** At −0.035em on a 100px name, the gap between words is visibly tight and adjacent letters almost kiss. That is correct.
- **Cover type is two-tone by position, not by choice.** Dark type sits on the cream half, cream type sits on the forest corner, and the eye reads it as one composition. When adapting the cover to another size, move the text to follow the gradient — do not recolor the text to fight it.
- **The photo dominates.** In the split layout the image occupies roughly a third of the total canvas area. It is the subject; the type frames it.
- **Nothing decorates.** No lines, rules, arrows, icons, dots, corner ornaments, or texture anywhere in the set. Every mark on the canvas is type, photo, logo, or ground.

---

## 8. Motion (web / video only)

```css
--motion-fast:   160ms;
--motion-base:   220ms;
--motion-reveal: 560ms;
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
```
- Scroll reveal: `opacity 0→1` + `translate3d(0, 1.5rem, 0) → 0` over `--motion-reveal` `--ease-out`, staggered `60–80ms` per child via `--reveal-delay`.
- Entrance: scale up from `0.82` with a small upward translate, `~0.85–1s`, `cubic-bezier(0.22,0.61,0.21,1)`, staggered.
- Hover: `translateY(-1px)` or `scale(1.04)`, `180–400ms`.
- Always honor `prefers-reduced-motion`.
- Blur filters cost real frames on mobile — swap `filter: blur()` decoration for a radial gradient on touch devices.

---

## 9. Copy voice

- Lowercase, short, declarative, confident. Fragments are fine.
- Ask a question, then answer it big: `"what's even possible?"` / `"things that couldn't exist without ai."`
- No corporate register, no exclamation-point stacking except as a deliberate warm beat (`"stay tuned!!"`).
- No em-dashes in headlines; use a line break instead.
- Talk about what got *built*, not about the club's mission statement.
- Ledes cap at ~24 characters wide and one or two sentences: `"projects built by the people behind aitc."`
- CTAs are verbs: `join aitc`, `see whats possible`.
- Contractions on, apostrophes casual (`whats` in the hero is intentional).

---

## 10. Layout archetypes

Pick one; do not blend.

1. **Cover / title** — light ground, dark title top-left, giant logo center, cream kicker bottom-right on the dark corner.
2. **Header + split body** — mid-green ground. Logo top-left, name/role right-aligned beside it; below, image at 67% left and a right-aligned text column at 29%. The workhorse for any repeating series.
3. **Statement** — dark ground, small logo top-left, one huge right-aligned block of cream type vertically centered. Closers, quotes, announcements, section dividers.
4. **Grid** — dark ground, section headline top-left at `clamp(3.2rem, 9.5vw, 8.5rem)` / `line-height: 0.86`, lede beneath, then a 4–5 column card or portrait grid.
5. **Full-bleed moment** — one image edge to edge, cream type over the darkest corner, no panel.

Alignment: text blocks are **left-aligned or right-aligned, never centered**, except archetype 3 and the site's "turn" section. When a text column sits to the right of an image, right-align it — the ragged edge faces the image and the flush edge holds the margin.

### Canvas sizes

| Medium | Size | S |
|---|---|---|
| IG feed post / carousel | 1080 × 1350 (4:5) | 1080 |
| IG story / reel cover | 1080 × 1920 (9:16) | 1080 |
| Slide deck | 1920 × 1080 (16:9) | 1080 |
| Web | fluid, `--page-width: 1440px` | `min(100vw,100vh)` |
| Print flyer | 300 dpi, S = short edge in px | scale the % table |

**Never** ship 1:1 or 4:3 for social. Portrait or 16:9 only.

---

## 11. Render pipeline (static output)

HTML + CSS → headless Chrome screenshot. Deterministic, pixel-exact, no design tool needed. This is how every AITC post is made; reuse it for slides, flyers, and thumbnails by changing `--window-size`.

```python
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new", "--disable-gpu", "--hide-scrollbars",
    "--force-device-scale-factor=1",
    f"--screenshot={out_png}",
    "--window-size=1080,1350",
    "--virtual-time-budget=3000",     # lets webfonts + autofit JS settle
    f"file://{html_file}",
], check=True, capture_output=True)
```

Rules:
- Set `html, body { width: <W>px; height: <H>px; }` explicitly and `overflow: hidden` on body.
- Embed every image as a base64 data URI so the HTML is self-contained and Chrome never races a file load.
- Run the autofit JS inline at the end of `<body>` — it executes before the screenshot.
- For 2× output use `--force-device-scale-factor=2` and keep the CSS pixel dimensions unchanged.
- Verify by opening the rendered PNG and looking at it. Always. Layout bugs in this system are invisible in code and obvious in the image.

---

## 12. Hard rules — violating any of these breaks the brand

1. Never change the shadow: `drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81))`.
2. Never uppercase. Never title case. Human names and proper nouns keep their real capitalization; everything else is lowercase.
3. Never a card inside a card inside a card. Panel + one frame, maximum.
4. Never 1:1 or 4:3 for social. Portrait (4:5, 9:16) or 16:9.
5. Never pure white or pure black. Cream and `--forest-deep`.
6. Never a second typeface, and never a weight outside 500/600/700.
7. Never place text on the sage bridge band (`#dbe1b3`/`#d5dfb0`) — it reads on neither.
8. Never tint the logo as an image; mask it.
9. Never wide letter-spacing except on eyebrows/captions under ~2% of S.
10. Never small type. When in doubt, go bigger — an AI agent's default type size is roughly half of what this brand wants.
11. Never center body text.
12. Never let supporting text approach the size of the headline (≤ 0.60×).
13. Never a vertical or horizontal gradient on a full ground — 135–145°, light top-left.
14. Never stock illustration, emoji as iconography, gradient meshes, glassmorphism beyond the one panel, or drop-shadowed boxes with neutral gray shadows.

---

## 13. Pre-ship checklist

- [ ] Canvas is a permitted size; every dimension derived from S via §3.
- [ ] Ground is one of the three in §2, angled 135–145°.
- [ ] Type sizes hit the §3 ladder; headline ≥ 8.5% of S.
- [ ] Ratio locks hold: subhead = 0.56× name, body ≤ 0.60× name.
- [ ] In a series, headline sizes are within ±5% across all items.
- [ ] Tracking tightens as size grows; leading ≤ 1.0 above the title band.
- [ ] Lowercase everywhere except human names and proper nouns.
- [ ] Cream gradient fill + exact glow on all display type over dark; nothing under 2.5% of S carries the glow.
- [ ] Logo masked, not tinted; ≥ 0.25× clear space; not stretched.
- [ ] Photos: hand-set `object-position`, house grade applied, `min-height: 0` on flex parents, source ≥ 2× the box.
- [ ] Nesting depth ≤ 2. Nothing is centered that shouldn't be.
- [ ] Rendered output opened and visually inspected, not just built.

---

## 14. Paste-ready starter

Drop this in, swap the content, render. It is the whole system in one file.

```html
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>aitc</title><style>
* { margin:0; padding:0; box-sizing:border-box;
    -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility; }
html, body { width:1080px; height:1350px; }        /* S = 1080 */
:root { --logo: url("data:image/png;base64,..."); }  /* logo.png, base64 */

body {
  position:relative; overflow:hidden;
  font-family:"SF Pro Display", 'Inter Tight', -apple-system, BlinkMacSystemFont, sans-serif;
  background: linear-gradient(140deg,#6f9d6f 0%,#558f61 26%,#35744a 58%,#1d5730 84%,#0f3a20 100%);
}
.panel { position:absolute; inset:22px; border-radius:56px;
  background:rgba(255,249,230,.135); border:1px solid rgba(255,249,230,.14);
  padding:46px 42px 42px; display:flex; flex-direction:column; }

.header { display:flex; align-items:flex-start; gap:28px; flex:0 0 auto; }
.logo { width:158px; height:158px; flex:0 0 auto; margin-top:4px;
  background:linear-gradient(180deg,#fff9e6 0%,#f4e8b8 100%);
  -webkit-mask:var(--logo) center/contain no-repeat; mask:var(--logo) center/contain no-repeat;
  filter:drop-shadow(11.2px 20.1px 39px rgba(30,96,55,.81)); }

/* stretch, not flex-end — autofit measures against this */
.col { flex:1 1 auto; min-width:0; display:flex; flex-direction:column;
       align-items:stretch; text-align:right; }

.cream { background:linear-gradient(180deg,#fff9e6 0%,#f4e8b8 100%);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  filter:drop-shadow(11.2px 20.1px 39px rgba(30,96,55,.81)); }

.title { font-size:100px; font-weight:700; line-height:1.0;
         letter-spacing:-.035em; white-space:nowrap; }
.sub   { margin-top:12px; font-size:56px; font-weight:700; line-height:1.06;
         letter-spacing:-.035em; white-space:nowrap; text-transform:lowercase; }

.body-row { flex:1 1 auto; min-height:0; display:flex; align-items:stretch; margin-top:34px; }
.frame { flex:0 0 640px; height:100%; min-height:0; border-radius:40px; overflow:hidden;
  border:2px solid rgba(255,243,203,.35); box-shadow:0 32px 80px rgba(8,28,16,.75);
  background:#0c2719; }
.frame img { width:100%; height:100%; object-fit:cover; display:block;
             filter:contrast(1.04) saturate(1.03); }
.side { flex:1 1 auto; min-width:0; padding-left:36px; padding-top:78px; text-align:right; }
.side p { font-size:60px; font-weight:700; line-height:1.08; letter-spacing:-.035em;
          overflow-wrap:break-word; }
</style></head>
<body>
  <div class="panel">
    <header class="header">
      <div class="logo" role="img" aria-label="AITC"></div>
      <div class="col">
        <h1 class="title cream">Joel Manuel</h1>
        <p class="sub cream">president/founder of aitc</p>
      </div>
    </header>
    <div class="body-row">
      <div class="frame"><img src="data:image/jpeg;base64,..."
           style="object-position:50% 30%;" alt="Joel Manuel"></div>
      <div class="side"><p class="cream">supporting copy, lowercase.</p></div>
    </div>
  </div>
<script>
function fitWidth(el, start, min){ if(!el) return start;
  for(var s=start; s>=min; s-=1){ el.style.fontSize=s+'px';
    if(el.scrollWidth <= el.clientWidth+1) return s; } return min; }
var n = fitWidth(document.querySelector('.title'), 100, 78);
fitWidth(document.querySelector('.sub'), Math.round(n*0.56), 38);
var side = document.querySelector('.side'), p = side && side.querySelector('p');
if(p){ var avail = side.clientHeight - parseFloat(getComputedStyle(side).paddingTop);
  for(var f=60; f>=28; f-=1){ p.style.fontSize=f+'px';
    if(p.scrollHeight<=avail && p.scrollWidth<=p.clientWidth+1) break; } }
</script>
</body></html>
```
