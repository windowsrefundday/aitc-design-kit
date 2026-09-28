---
name: aitc-brand
description: The AITC design system (BRAND.md spec + DESIGNER.md prompt pack). Load before producing ANY visual output for AITC — Instagram posts, slides, web pages, flyers, thumbnails, email headers, merch. Defines exact colors, gradients, typography, the short-edge proportion system, the signature cream-fill + forest-glow text treatment, logo masking, photo framing, copy voice, and the headless-Chrome render pipeline. Non-negotiable specs; do not improvise brand values.
---

# AITC brand

Two files at the repository root:

- **`BRAND.md`** — the spec. Exact colors, the short-edge proportion math, the signature text treatment, logo masking, photo framing, hard rules, pre-ship checklist. **Read it in full before designing anything.** Single source of truth.
- **`DESIGNER.md`** — paste-ready natural-language prompts for AI design tools (Google Stitch, Figma Make, v0, Lovable, image generators). Use when driving another tool rather than writing code yourself.

Fastest path for a new static asset (post, slide, flyer, thumbnail):
1. Read `BRAND.md`.
2. Copy the starter template in `BRAND.md` §14, or copy `generate_ig_posts.py` and change the data list.
3. Derive every size from `S = min(width, height)` using the §3 table.
4. Render with headless Chrome (§11), then **open the PNG and look at it** before shipping.

Non-negotiables you will get wrong if you skip the file: the exact drop-shadow, the lowercase rule and its proper-noun exception, the ≤0.60× supporting-text ratio, the no-nested-cards rule, and the fact that AITC type is roughly twice as large as an agent's default instinct.
