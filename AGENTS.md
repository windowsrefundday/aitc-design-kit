# AGENTS.md

Developer and AI agent guide for `aitc-parallax`.

This repository houses the visual brand system, web assets, and social post automation pipelines for **AITC (AI Technology Club at Enloe High School)**. Tagline: **"build with ai. create whats next."**

---

## 1. Repository Quick Tour & Asset Inventory

All design assets, scripts, and specifications are organized as follows:

| Path | Purpose |
|---|---|
| `generate_ig_posts.py` | Canonical Instagram 4:5 carousel generator (renders via Headless Chrome). |
| `design-kit/` | Self-contained, portable design kit for Figma, Stitch, v0, Lovable, Claude, and human designers. |
| `design-kit/tokens/` | Design tokens exported in 4 machine formats: DTCG JSON (`design_tokens.json`), CSS (`tokens.css`), Tailwind v4 (`tailwind.css`), and Tailwind v3 (`tailwind.config.json`). |
| `design-kit/fonts/` | `InterTight[wght].ttf` (Variable weight 100–900, SIL Open Font License). |
| `design-kit/logo/` | Master 1024² logo marks, alpha mask (`logo-mask-1024.png`), and flat recolors (`logo-cream-1024.png`, `logo-forest-1024.png`, `logo-deep-1024.png`). |
| `design-kit/palette/` | Visual specimen sheets (`aitc-palette.png`, `aitc-grounds.png`, `aitc-type-specimen.png`, `aitc-components.png`). |
| `design-kit/reference/` | Reference shipped assets showing canonical light/dark grounds and type scales. |
| `BRAND.md` | The authoritative engineering specification: colors, math, typography, proportion system, and render pipeline. |
| `DESIGNER.md` | Natural-language prompt pack optimized for AI generative tools (Google Stitch, v0, Midjourney, Figma Make). |
| `DESIGN.md` | Structured design token specifications and rationale (`@google/design.md` format). |
| `CONTEXT.md` | Club mission, history, and domain context. |
| `logo.png` / `logo-refined.svg` | Root logo marks (1024×1024 alpha mask source and refined SVG). |
| `instagram_board_posts/` | Shipped 1080×1350 PNG outputs produced by `generate_ig_posts.py`. |
| `temp_html_posts/` | Intermediate standalone HTML templates compiled during Instagram post generation. |
| `styles.css` / `index.html` | Live club website stylesheet and markup. |
| `.agents/skills/` | Agent skills for brand rules (`aitc-brand`) and creative taste layer (`aitc-design-brain`). |

---

## 2. AITC Design Asset & Brand Guidelines

### 2.1 The One-Paragraph Vibe
**Cream on forest green.** Confident, oversized, editorial — a blend of modern streetwear and an Apple keynote presentation. One typeface family, strictly lowercase across all UI, headlines, and captions (with specific exceptions for human and proper product nouns). Headlines and names are **massive** and **tightly tracked**. Layouts feature a rounded, translucent glass panel floating inside a 140° diagonal gradient ground. **Never pure white, never pure black, never neutral gray, and never a third hue.** Empty space is deliberate and sacred.

---

### 2.2 Color Tokens & Rules

Exact CSS custom property tokens:

```css
:root {
  --cream:        #fff3cb;  /* primary light ground + primary text on dark */
  --cream-soft:   #f4e8b8;  /* lower stop for cream gradients, secondary text on dark */
  --cream-hi:     #fff9e6;  /* top stop of cream text gradient fill */
  --forest:       #216434;  /* mid brand green, ink on light grounds */
  --forest-mid:   #174b2a;  /* deep green gradient stop */
  --forest-deep:  #0c2719;  /* darkest green — page backing, the "black" of the system */
  --forest-light: #8dad82;  /* sage transition stop, card gradients */
  --ink:          #2b7244;  /* body and headline text on cream grounds */
  --muted-ink:    rgba(33, 100, 52, 0.62);  /* secondary text on cream */
}
```

Additional exact gradient stops: `#dbe1b3` (sage bridge), `#6f9d6f`, `#558f61`, `#35744a`, `#1d5730`, `#123f22`, `#0f3a20`, `#082810`.

#### Hard Color Rules
1. **Two color families only**: Cream and Forest. No blues, reds, purples, or neutral grays.
2. **Zero pure white (`#fff`) and zero pure black (`#000`)**: `--cream` is white; `--forest-deep` (`#0c2719`) is black.
3. **Accent is contrast jump**: No tertiary accent color. To make an element pop, place `--cream` on `--forest-deep`.
4. **Borders**:
   - On dark ground: `1px solid rgba(255, 249, 230, 0.14)` (or `0.12–0.22`).
   - On light ground: `1px solid rgba(12, 39, 25, 0.12)`.
5. **Shadows are always green-black**: `rgba(4, 28, 15, ·)` or `rgba(8, 28, 16, ·)`, never neutral black or gray.

---

### 2.3 The Three Canonical Grounds

Every visual surface in the system belongs to one of these three grounds:

#### A. Light Ground (Hero & Cover Slides)
```css
background:
  radial-gradient(circle at 102% 103%,
    rgba(8, 28, 16, 1) 0%,
    rgba(12, 39, 25, 0.94) 16%,
    rgba(33, 100, 52, 0.62) 34%,
    rgba(255, 243, 203, 0) 72%),
  linear-gradient(135deg,
    #fff3cb 0%,
    #fff3cb 50%,
    #dbe1b3 76%,
    #174b2a 100%);
```
- Cream covers the top-left 50%, transitioning through sage into forest green in the bottom-right corner.
- **Two-tone text split**: Dark type (`#0c2719`) sits top-left; cream type sits bottom-right over the deep-forest gradient corner.

#### B. Dark Ground (Closing Slides, Narrative Blocks, Main Site Backing)
```css
background:
  radial-gradient(120% 78% at 14% 6%,
    rgba(45, 110, 66, 0.58) 0%,
    rgba(12, 39, 25, 0) 62%),
  linear-gradient(140deg, #1d5730 0%, #123f22 44%, #0c2719 100%);
```

#### C. Mid-Green Ground (Repetitive Series Items & Profile Cards)
```css
background: linear-gradient(140deg,
  #6f9d6f 0%,
  #558f61 26%,
  #35744a 58%,
  #1d5730 84%,
  #0f3a20 100%);
```
- **140° is the house angle**: Light top-left to dark bottom-right.
- Carousel sequence formula: **Light Cover → Mid-Green Body Slides → Dark Outro/Closer.**

---

### 2.4 Proportion System (`S = min(width, height)`)

All spatial values scale off the canvas short edge **`S`** (e.g., `S = 1080` for 1080×1350 Instagram posts or 1920×1080 slides):

| UI Component | % of S | Exact Pixel @ S=1080 |
|---|---|---|
| Floating panel inset | 2.0% | `22px` |
| Floating panel corner radius | 5.2% | `56px` |
| Panel padding (top / x / bottom) | 4.3% / 3.9% / 3.9% | `46px 42px 42px` |
| Header logo mark | 14.6% | `158px × 158px` |
| Logo-to-text header gap | 2.6% | `28px` |
| Header-to-body margin | 3.1% | `34px` |
| Portrait card radius | 3.7% | `40px` |
| Column gutter | 3.3% | `36px` |
| Workhorse two-column split | Image: `640px` (flex `0 0 640px`) | Fact column: remaining flex space |

---

### 2.5 Typography & The Lowercase Rule

#### Family & Weights
- Primary font: `'SF Pro Display'` (macOS headless rasterization) or `'Inter Tight'` (web/cross-platform).
- Fallback stack: `-apple-system, BlinkMacSystemFont, "Inter Tight", "Helvetica Neue", sans-serif`.
- Weights:
  - **700 (Bold)**: Rasterized social posts, print, and display.
  - **600 (Semi-bold)**: Web headlines, titles, and interactive elements.
  - **500 (Medium)**: Long-form body copy.
  - **No italics anywhere.** No extra light (300) or ultra black (900).

#### The Lowercase Rule
**Everything is lowercase by default:** headlines, roles, nav links, buttons, eyebrows, facts, and captions.
- *Examples*: `"build with ai."`, `"president/founder of aitc"`, `"fun fact: my favorite video game is kingdom hearts."`

**Exceptions (Preserve True Title/Mixed Casing):**
1. **Human names**: `Joel Manuel`, `Vihaan Patel`, `Yash Bafna`, `Aarit Srivastava`, `Siddarth Yetukuri`, `Nishaanth Jay`.
2. **Proper product / brand / game nouns**: `Face ID`, `iPhone`, `Kingdom Hearts`, `Ken Carson`, `Wikipedia`, `AlphaFold`, `3D`.
3. `AITC` in accessibility labels/alt text (visually rendered as the mark or lowercase `aitc`).

#### Tracking & Leading Scale
| Type Level | Font Size (% of S) | @ S=1080 | Line Height | Letter Spacing |
|---|---|---|---|---|
| Outro / Mega Statement | 14–16% | `150–170px` | `0.94–0.98` | `-0.04em` |
| Cover Headline | 10–11% | `108–118px` | `0.92` | `-0.045em` |
| Person Name | 8.5–9.5% | `92–100px` | `1.00` | `-0.035em` |
| Person Role | 5.0–5.5% | `54–56px` | `1.06` | `-0.035em` |
| Fun Fact Body | 4.5–5.6% | `48–60px` | `1.08` | `-0.035em` |
| Eyebrow / Tag | 1.3–1.8% | `14–20px` | `1.10` | `+0.04em` to `+0.14em` |

---

### 2.6 Signature Cream Text Treatment

Every prominent cream text element on dark or mid-green grounds uses this exact two-part CSS treatment:

```css
/* 1. Cream Gradient Text Fill */
background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;

/* 2. Signature Forest Green Glow (never change these constants) */
filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
```

> **Why `filter: drop-shadow` instead of `text-shadow`?**
> Standard `text-shadow` is disabled when `-webkit-text-fill-color: transparent` is active. `filter: drop-shadow` traces the alpha contours of the clipped text glyphs and renders the deep forest glow.

On **light grounds** (e.g. cover header), use dark ink:
```css
color: #0c2719;
filter: drop-shadow(7px 13px 28px rgba(12, 39, 25, 0.22));
```

---

### 2.7 Logo Mark Masking

The AITC mark (`logo.png` or `design-kit/logo/logo-mask-1024.png`) is an **alpha silhouette mask**:
- **Always mask** via CSS mask:
  ```css
  .aitc-logo {
      width: 158px;
      height: 158px;
      background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
      -webkit-mask: url("logo.png") center / contain no-repeat;
      mask: url("logo.png") center / contain no-repeat;
      filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
  }
  ```
- **Never tint, never use `filter: invert()`, and never place the raw PNG directly without a mask.**
- The glyph bounding box is asymmetrical within the 1024² canvas (x: 162–848, y: 232–935). Maintain clear space equal to at least 0.25× mark width on all sides.

---

## 3. Instagram Post Generator (`generate_ig_posts.py`)

The script `generate_ig_posts.py` automates the generation of 4:5 (1080×1350) carousel announcement slides for Instagram.

### 3.1 Architecture & Pipeline

```
  [Data Config: officers list]
             │
             ▼
   [build_html() Generator]
             │ (Base64 encodes images & logo, injects CSS & Autofit JS)
             ▼
    [temp_html_posts/*.html]
             │
             ▼
[Headless Google Chrome Screenshot Process]
  --headless=new
  --window-size=1080,1350
  --force-device-scale-factor=1
  --virtual-time-budget=3000
             │
             ▼
[instagram_board_posts/*.png] (Pixel-perfect 1080x1350 ready to publish)
```

---

### 3.2 Prerequisites & Setup

1. **Python 3.8+**: Uses standard libraries only (`base64`, `subprocess`, `pathlib`). No `pip install` required.
2. **Google Chrome**:
   - macOS default configured in script:
     ```python
     CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
     ```
   - *Linux*: Change `CHROME` to `"/usr/bin/google-chrome"` or `"/usr/bin/chromium-browser"`.
   - *Windows*: Change `CHROME` to `"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"`.
3. **Assets**: Verify `logo.png` is in the repository root and officer headshots are available.

---

### 3.3 Running the Generator

Execute from the repository root:

```bash
python3 generate_ig_posts.py
```

Console output:
```text
rendering 00_cover.png @ 1080x1350 ...
rendering 01_joel.png @ 1080x1350 ...
rendering 02_vihaan.png @ 1080x1350 ...
...
done -> instagram_board_posts/
```

- Rendered PNGs are written to `instagram_board_posts/`.
- Intermediate HTML files are written to `temp_html_posts/`.

---

### 3.4 Data Configuration Schema (`officers` list)

The `officers` list in `generate_ig_posts.py` defines the carousel slides. It supports three distinct slide archetypes:

#### 1. Cover Slide (`kind: "cover"`)
```python
{
    "filename": "00_cover.png",
    "kind": "cover",
}
```
*Layout*: Inverted light ground, large dark display title (`"board\nannouncement!!"`), hero masked logo, cream kicker (`"meet the team"`).

#### 2. Officer Profile Slide (Default)
```python
{
    "filename": "01_joel.png",
    "name": "Joel Manuel",                        # True case (Human Name)
    "role": "president/founder of aitc",          # All lowercase
    "fact": "i spend my free time clicking...",   # All lowercase except proper nouns
    "image_file": BASE_DIR / "joel.jpg",          # Path object or Path / "filename"
    "object_position": "50% 30%",                 # CSS object-position for photo crop
    "zoom": (1.55, "50% 56%"),                    # Optional tuple: (scale_factor, transform_origin)
    "year": None,                                 # Optional string, e.g. "junior year"
}
```

#### 3. Outro Slide (`kind: "outro"`)
```python
{
    "filename": "07_outro.png",
    "kind": "outro",
    "outro": "so much more to expect in the coming weeks, stay tuned!!",
}
```
*Layout*: Deep dark ground, masked logo top-left, massive right-aligned statement text.

---

### 3.5 Photo Cropping & Framing Controls

Headshots are rendered inside a rigid container:
- Width: `640px` (flex `0 0 640px`)
- Height: `100%` of remaining panel space
- Border: `2px solid rgba(255, 243, 203, 0.35)`
- Shadow: `0 32px 80px rgba(8, 28, 16, 0.75)`
- Object fit: `object-fit: cover`

#### Adjusting Head Position & Zoom
- **`object_position`**: Sets horizontal and vertical focus within the frame.
  - Centered eye line: `"50% 30%"` to `"50% 40%"`.
  - High crop / tall torso: `"50% 6%"`.
  - Low crop: `"50% 100%"`.
- **`zoom`**: Tuple `(scale_factor, transform_origin)`.
  - Default: Omit if the raw image framing is already tight.
  - Zoom in on face: `(1.42, "50% 62%")` scales by 1.42× anchored at 50% X and 62% Y.

---

### 3.6 Dynamic Autofit Engine (`AUTOFIT_JS`)

The generator injects client-side JavaScript into each HTML canvas before rendering:
1. **Name fitting (`fitWidth`)**: Starts at `100px` and steps down to `78px` until `el.scrollWidth <= el.clientWidth + 1` (guarantees names never wrap to two lines).
2. **Role fitting**: Dynamically scales the role font size to `Math.round(nameSize * 0.56)` down to a floor of `38px`.
3. **Fun Fact fitting**: Dynamically scales the fact font size between `60px` and `28px` to maximize space without overflowing column height.
4. **Outro fitting**: Scales large statement text between `170px` and `60px`.

---

### 3.7 Step-by-Step Recipe: Adding a New Slide

To add a new officer or profile card:

1. Place the portrait image in the repository root or `new asset/` folder (e.g. `alex.jpg`).
2. Open `generate_ig_posts.py`.
3. Insert a new dictionary into the `officers` list before the outro slide:

```python
    {
        "filename": "07_alex.png",
        "name": "Alex Rivera",
        "role": "ai research lead of aitc",
        "fact": "i trained my first neural network to recognize cereal boxes.",
        "image_file": BASE_DIR / "alex.jpg",
        "object_position": "50% 35%",
        "zoom": (1.20, "50% 50%"),
        "year": "senior year",
    },
```

4. Run `python3 generate_ig_posts.py`.
5. Open `instagram_board_posts/07_alex.png` and verify visual balance.

---

## 4. Pre-Ship Visual Quality Checklist

Before publishing any visual asset or social card:

- [ ] **Lowercase Check**: Is every headline, role, and label lowercase? Are human names (`Joel Manuel`) and proper product nouns (`Face ID`, `iPhone`) properly capitalized?
- [ ] **No Neutral Shadows**: Do all cream text elements use `filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81))`?
- [ ] **Logo Integrity**: Is the logo masked via CSS? Is it free of color clipping, inversions, or tint artifacts?
- [ ] **Photo Balance**: Is the headshot well-framed with comfortable headroom inside the 640px card?
- [ ] **Autofit Verification**: Did the person's name stay on a single line? Does the role remain roughly ~0.56× the name size?
- [ ] **Resolution**: Is the output image exactly 1080×1350 at 72/144 DPI with zero scrollbars or rendering glitches?

---

## 5. Agent Development & Governance Rules

When operating in this codebase:

- **Do NOT touch existing automation scripts** unless explicitly requested.
- **Maintain design consistency**: Adhere strictly to the color, typography, and proportion tokens documented in `BRAND.md` and `DESIGN.md`.
- **For AI design tool generation**: Refer to `DESIGNER.md` for pre-crafted prompt packs.
- **Taste layer**: Follow `.agents/skills/aitc-design-brain/SKILL.md` (Joel's personal aesthetic layer: space first, softness over sharpness, lowercase informal tone).
- **Issue tracker & triage**:
  - Issue tracker: `.scratch/` (see `docs/agents/issue-tracker.md`).
  - Canonical triage labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix` (see `docs/agents/triage-labels.md`).
  - Domain documentation: `CONTEXT.md` and `docs/adr/` (see `docs/agents/domain.md`).
