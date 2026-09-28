# AITC Design Kit & Social Post Generator

Official brand system, portable design assets, and automated 4:5 Instagram carousel post generator for **AITC (AI Technology Club at Enloe High School)**.

> **Tagline:** *"build with ai. create whats next."*

---

## 1. Quickstart (Under 30 Seconds)

Generate the complete 8-slide Instagram carousel immediately:

```bash
# 1. Clone this repository
git clone https://github.com/WindowsRefundDay/aitc-design-kit.git
cd aitc-design-kit

# 2. Run the post generator (uses Python standard library + Google Chrome)
python3 generate_ig_posts.py

# 3. Check rendered images
open instagram_board_posts/
```

Pixel-perfect 1080×1350 PNG images will be rendered in `instagram_board_posts/`.

---

## 2. Prerequisites & Environment Setup

1. **Python 3.8+**: Uses standard libraries only (`base64`, `subprocess`, `pathlib`). No `pip install` required!
2. **Google Chrome**:
   - **macOS** (default configured in script):
     ```python
     CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
     ```
   - **Linux**: Set `CHROME = "/usr/bin/google-chrome"` or `"/usr/bin/chromium-browser"`.
   - **Windows**: Set `CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"`.
3. **Fonts**:
   - Headless Chrome on macOS defaults to `"SF Pro Display"`.
   - The open-source brand font `Inter Tight` is included under `design-kit/fonts/InterTight[wght].ttf`.

---

## 3. How to Use `generate_ig_posts.py`

### 3.1 Pipeline Architecture

```
  [Data: officers list] ──► [build_html()] ──► [temp_html_posts/*.html]
                                                        │
                                                        ▼
                                           [Headless Google Chrome]
                                           (1080x1350 @ 1x screenshot)
                                                        │
                                                        ▼
                                          [instagram_board_posts/*.png]
```

### 3.2 Slide Types & Data Schema

The `officers` list in `generate_ig_posts.py` configures the slides. It supports three slide archetypes:

#### A. Cover Slide (`kind: "cover"`)
```python
{
    "filename": "00_cover.png",
    "kind": "cover",
}
```
*Features*: Inverted light ground, large dark headline (`"board\nannouncement!!"`), hero masked logo, cream kicker (`"meet the team"`).

#### B. Member / Officer Profile Slide (Default)
```python
{
    "filename": "01_joel.png",
    "name": "Joel Manuel",                        # True case (Human Name)
    "role": "president/founder of aitc",          # All lowercase
    "fact": "i spend my free time clicking...",   # Lowercase except proper nouns
    "image_file": BASE_DIR / "joel.jpg",          # Path to JPG/PNG portrait
    "object_position": "50% 30%",                 # Crop focus (X% Y%)
    "zoom": (1.55, "50% 56%"),                    # Optional: (scale, "origin_x origin_y")
    "year": None,                                 # Optional: e.g. "junior year"
}
```

#### C. Outro Slide (`kind: "outro"`)
```python
{
    "filename": "07_outro.png",
    "kind": "outro",
    "outro": "so much more to expect in the coming weeks, stay tuned!!",
}
```
*Features*: Deep dark forest ground, masked logo top-left, massive right-aligned statement text.

---

### 3.3 Framing & Cropping Controls

The portrait frame is locked to `640px` wide with a `40px` border-radius and deep shadow.

- **Adjusting Focal Point (`object_position`)**:
  - Centered eye level: `"50% 35%"` to `"50% 40%"`
  - High crop / tall shoulders: `"50% 6%"`
  - Full torso / low crop: `"50% 100%"`
- **Zooming In On Faces (`zoom`)**:
  - Format: `(scale_factor, "origin_x origin_y")`
  - Example: `(1.42, "50% 62%")` scales the photo by 1.42× anchored at 50% horizontal and 62% vertical.

---

### 3.4 Dynamic Autofit Engine (`AUTOFIT_JS`)

Each slide automatically balances typography in the browser before taking the screenshot:
- **Names** start at `100px` and dynamically shrink down to `78px` until they fit exactly on a single line.
- **Roles** scale proportionally to `0.56 × nameSize` down to a floor of `38px`.
- **Facts** scale between `60px` and `28px` to fill the right column without overflowing.
- **Outro statements** scale between `170px` and `60px`.

---

### 3.5 Step-by-Step: Adding a New Person

1. Add their portrait photo to the repository root (e.g. `alex.jpg`).
2. Open `generate_ig_posts.py`.
3. Add a new dictionary to the `officers` list before the outro slide:

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
5. Check `instagram_board_posts/07_alex.png`.

---

## 4. Design Asset & Brand Guidelines

### 4.1 The Vibe
**Cream on forest green.** Confident, oversized, editorial — modern streetwear meets Apple keynote. Generous negative space, rounded translucent floating panels, and tight tracking.

### 4.2 Exact Color Tokens

```css
:root {
  --cream:        #fff3cb;  /* primary light ground + primary text on dark */
  --cream-soft:   #f4e8b8;  /* lower stop for cream gradients, secondary text */
  --cream-hi:     #fff9e6;  /* top stop of cream text gradient fill */
  --forest:       #216434;  /* mid brand green, ink on light grounds */
  --forest-mid:   #174b2a;  /* deep green gradient stop */
  --forest-deep:  #0c2719;  /* darkest green — page backing, the "black" */
  --forest-light: #8dad82;  /* sage transition stop, card gradients */
  --ink:          #2b7244;  /* body and headline text on cream grounds */
  --muted-ink:    rgba(33, 100, 52, 0.62);  /* secondary text on cream */
}
```

- **No pure white (`#fff`) and no pure black (`#000`)**.
- **No neutral gray or third hue**.
- **Shadows are always green-black**: `rgba(4, 28, 15, ·)` or `rgba(8, 28, 16, ·)`.

---

### 4.3 Typography & The Lowercase Rule

- **Family**: `'SF Pro Display'` or `'Inter Tight'`.
- **Weights**: `700` (Bold) for rasterized social/print, `600` (Semi-bold) for web, `500` (Medium) for long body copy. No italics.
- **The Lowercase Rule**: Everything is strictly lowercase (`"build with ai."`, `"vice president of aitc"`, `"fun fact: ..."`).
  - **Exceptions**: Human names (`Joel Manuel`, `Aarit Srivastava`) and proper product/brand nouns (`Face ID`, `iPhone`, `Kingdom Hearts`, `Ken Carson`, `Wikipedia`, `AlphaFold`, `3D`).

---

### 4.4 Signature Cream Text Treatment

Every prominent cream text element on dark or mid-green grounds uses this exact two-part CSS treatment:

```css
/* 1. Cream Gradient Text Fill */
background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;

/* 2. Signature Forest Green Glow */
filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
```

---

### 4.5 Logo Mark Masking

The AITC mark (`logo.png` or `design-kit/logo/logo-mask-1024.png`) is an **alpha silhouette mask**:
- Mask using CSS `mask`:
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

---

## 5. The `design-kit/` Folder

The `design-kit/` directory is self-contained and ready to import into Figma, Google Stitch, v0, Lovable, or Claude:

```
design-kit/
├── tokens/              ← design_tokens.json (DTCG), tokens.css, tailwind.css, tailwind.config.json
├── fonts/               ← InterTight[wght].ttf (variable weight 100–900, SIL Open Font License)
├── logo/                ← 1024² master mask (logo-mask-1024.png) and flat recolors
├── palette/             ← specimen sheets (aitc-palette.png, aitc-grounds.png, etc.)
├── reference/           ← shipped 1080x1350 visual reference cards
├── source/              ← standalone HTML/CSS starter templates
├── BRAND.md             ← full engineering brand specification
├── DESIGNER.md          ← AI prompt pack for generative tools
└── DESIGN.md            ← design tokens & rationale
```

---

## 6. Pre-Ship Quality Checklist

Before sharing or posting slides:

- [ ] **Lowercase Check**: Are all roles, facts, and captions lowercase? Are human names and proper nouns preserved in true mixed casing?
- [ ] **Drop-Shadow Verification**: Do cream titles use `filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81))`?
- [ ] **Logo Integrity**: Is the logo rendered via CSS alpha mask without clipping or invert artifacts?
- [ ] **Portrait Framing**: Is the person's face well-centered with comfortable headroom inside the 640px card?
- [ ] **Autofit Verification**: Did the person's name stay on one line? Does the role remain ~0.56× the name size?
- [ ] **Resolution**: Is the output image exactly 1080×1350?

---

## 7. License & Credits

Created by Joel Manuel for **AITC (AI Technology Club at Enloe High School)**.
Designed with modern web standards and automated with headless browser graphics.
