# aitc design kit

Everything needed to design something new for AITC, in one folder. No portraits —
brand assets only.

Drop the whole folder into a design tool (OpenDesign, Stitch, Figma Make, v0,
Claude, Lovable) or hand it to a person. Nothing here depends on the rest of the
repo.

```
design-kit/
├── DESIGN.md            ← start here. tokens + rationale, DESIGN.md spec format
├── BRAND.md             ← the authority: exact math, render pipeline, hard rules
├── DESIGNER.md          ← prose prompt pack for AI design tools
├── tokens/              ← the same tokens in four machine formats
├── fonts/               ← Inter Tight variable font + license
├── logo/                ← the mark, as mask + flat recolors
├── palette/             ← rendered palette, grounds, type, component sheets
├── reference/           ← shipped output, the look you are matching
└── source/              ← real site CSS/HTML + the post generator + a starter file
```

## Upload order for a design tool

1. **`DESIGN.md`** — paste into the DESIGN.md field, or upload as a file.
2. **`palette/*.png`** — upload as reference images. Tools weight uploaded images
   heavily; this is the single biggest quality lever.
3. **`reference/*.png`** — shipped output. Upload at least the cover and the
   statement post so the tool sees the two-tone split and the type scale.
4. **`fonts/InterTight[wght].ttf`** — if the tool takes a font upload.
5. **`logo/logo-mask-1024.png`** — if it takes a logo. If it insists on a colored
   file, give it `logo-cream-1024.png` on dark or `logo-deep-1024.png` on light.
6. For brand voice, paste §1 of `DESIGNER.md`.

Then run the fix list in `DESIGNER.md` §6 — a generator gets the same four things
wrong every time.

## tokens/

Generated from `DESIGN.md` with `npx @google/design.md export`. Regenerate after
any token change rather than hand-editing these.

| File | Format | Use |
|---|---|---|
| `design_tokens.json` | DTCG 2025.10 | Figma variables, Style Dictionary, most token pipelines |
| `tokens.css` | plain `:root` custom properties | drop into any stylesheet |
| `tailwind.css` | Tailwind v4 `@theme` block | Tailwind v4 projects |
| `tailwind.config.json` | Tailwind v3 theme object | paste into `tailwind.config.js` |

```bash
npx @google/design.md lint DESIGN.md      # validate + WCAG check
npx @google/design.md export DESIGN.md --format dtcg > tokens/design_tokens.json
```

## fonts/

`InterTight[wght].ttf` — variable, weight axis 100–900, from Google Fonts (SIL
Open Font License, `OFL.txt`). The system uses **600** on web, **700** for
rasterized social and print, **500** for long body copy. No italic ships here on
purpose: the brand has no italics.

Web fallback stack, in order: `'Inter Tight', -apple-system, BlinkMacSystemFont,
"SF Pro Display", "SF Pro Text", "Helvetica Neue", Helvetica, Arial, sans-serif`.
For local rasterizing on macOS put `"SF Pro Display"` first — that is the metric
the reference posts were built on.

Always set `font-synthesis: none` so a missing weight fails loudly instead of
faking.

## logo/

| File | What it is |
|---|---|
| `logo-master-1024.png` | the original 1024² RGBA source |
| `logo-mask-1024.png` | white-on-transparent — **use this as the CSS mask** |
| `logo-cream-*.png` | flat `#fff3cb`, for tools that cannot mask. On dark only. |
| `logo-forest-*.png` | flat `#216434`, on cream only |
| `logo-deep-*.png` | flat `#0c2719`, on cream only |

The correct way to place the mark is a mask, never a tint and never
`filter: invert`:

```css
.logo {
  -webkit-mask: url("logo-mask-1024.png") center / contain no-repeat;
          mask: url("logo-mask-1024.png") center / contain no-repeat;
  background: linear-gradient(180deg, #fff9e6 0%, #f4e8b8 100%);  /* on dark */
  filter: drop-shadow(11.2px 20.1px 39px rgba(30, 96, 55, 0.81));
}
```

Two things to know about the art: it is **not centered in its canvas** — the glyph
occupies x 162–848, y 232–935 of 1024², so center it by its own bounding box, not
by the file. And clear space is at least 0.25× the mark's width on every side.

There is no vector version yet. Everything here is raster at 1024². If a tool
needs SVG, the mark has to be redrawn or traced — do not let a generator invent
its own version of it.

## palette/

Rendered sheets, made with the same headless-Chrome pipeline as every AITC asset.
Upload these as reference images.

- `aitc-palette.png` — all eight named colors with token names, hex, and usage,
  plus the seven gradient stops
- `aitc-grounds.png` — the three canonical grounds side by side
- `aitc-type-specimen.png` — the type scale at S = 1080 with tracking and leading
- `aitc-components.png` — panel, content card, pills, image frame, eyebrow +
  headline, logo lockup

## reference/

Shipped work, all face-free. This is the look being matched.

| File | Archetype |
|---|---|
| `post-cover-light-ground.png` | cover — light ground, dark type top-left, cream type on the forest corner |
| `post-statement-dark-ground.png` | statement — dark ground, one huge right-aligned block |
| `campaign-cover-light-ground.png` | cover with a centered hero mark |
| `campaign-details-mid-green.png` | mid-green ground, left-aligned detail stack |
| `campaign-details-2.png` | same ground, second variation |
| `poster-a4-noqr.png` | print, 2480×3508 at 300 dpi |

## source/

- `aitc-starter-post.html` — a working 1080×1350 canvas wired to the real font and
  logo in this folder. Swap the content, render, done. Render command is in the
  file's header comment; **it needs `--allow-file-access-from-files`** or Chrome
  silently drops the logo mask.
- `generate_ig_posts.py` — the canonical implementation of the whole system
- `aitc-site-styles.css` / `aitc-site-index.html` — the live site, as the copy-voice
  and web-scale reference

## The five-second version

Cream on forest green. One typeface, everything lowercase except human names.
Type enormous and tightly tracked — that is the whole personality. One rounded
translucent panel floating in a 140° gradient, light top-left. Nothing centered,
nothing decorated, nothing nested more than two deep. Never pure white, never pure
black, never a third color.
