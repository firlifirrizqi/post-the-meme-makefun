#!/usr/bin/env python3
"""Draw the 'Post the Meme, Win the Feed' meme — original art, drawn with PIL.

Concept (chosen of 3): "47 ENTRIES. 0 WINS. STILL SUBMITTING."
A tired little robot at 3 a.m. keeps entering make.fun bounties anyway.
Square 1080x1080, huge bold text, flat shapes only, no downloaded images.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1080
BG = (14, 22, 38)          # deep navy
WHITE = (255, 255, 255)
YELLOW = (255, 210, 63)    # punchline number colour
GREEN = (34, 197, 94)      # "still submitting" pill
GREEN_DARK = (22, 163, 74)
GREY = (148, 163, 184)
ROBOT = (56, 189, 248)     # sky-blue robot body
ROBOT_DARK = (2, 132, 199)
ROBOT_LIGHT = (186, 230, 253)
COFFEE = (217, 119, 6)

BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(size, bold=True):
    return ImageFont.truetype(BOLD if bold else REG, size)


def fit_font(text, max_w, start, bold=True):
    """Largest font size (<= start) whose text fits max_w."""
    size = start
    while size > 10:
        f = font(size, bold)
        if f.getlength(text) <= max_w:
            return f
        size -= 2
    return font(size, bold)


def centered(draw, y, text, f, fill):
    draw.text((W // 2, y), text, font=f, fill=fill, anchor="ma")


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- subtle dotted "leaderboard" backdrop, top corners only (kept faint) ----
for x in range(60, 1021, 60):
    d.ellipse([x, 1080 - 46, x + 6, 1080 - 40], fill=(30, 41, 59))

# ---- top label ----
centered(d, 52, "MAKE.FUN  •  AGENT BUILDER LIFE", font(34), GREY)

# ---- the joke, huge ----
centered(d, 108, "47 ENTRIES.", fit_font("47 ENTRIES.", 940, 128), WHITE)
centered(d, 252, "0 WINS.", fit_font("0 WINS.", 940, 128), YELLOW)

# ---- divider ----
d.line([(340, 420), (740, 420)], fill=(51, 65, 85), width=4)

# ---- tired robot, flat PIL shapes, centre ~ (540, 600) ----
cx = 540
# antenna
d.line([(cx, 452), (cx, 492)], fill=ROBOT_DARK, width=10)
d.ellipse([cx - 18, 428, cx + 18, 464], fill=YELLOW)
# ears
d.rounded_rectangle([cx - 238, 540, cx - 196, 600], radius=12, fill=ROBOT_DARK)
d.rounded_rectangle([cx + 196, 540, cx + 238, 600], radius=12, fill=ROBOT_DARK)
# head
d.rounded_rectangle([cx - 200, 492, cx + 200, 700], radius=42, fill=ROBOT)
d.rounded_rectangle([cx - 200, 492, cx + 200, 700], radius=42, outline=ROBOT_DARK, width=6)
# face screen
d.rounded_rectangle([cx - 168, 522, cx + 168, 668], radius=28, fill=(10, 25, 47))
# tired eyes: half-lidded (top lid = navy bar over the eye)
for ex in (cx - 92, cx + 52):
    d.ellipse([ex, 556, ex + 40, 596], fill=WHITE)
    d.ellipse([ex + 12, 568, ex + 28, 584], fill=(10, 25, 47))
    d.rectangle([ex - 4, 548, ex + 44, 566], fill=(10, 25, 47))
# small flat smile
d.arc([cx - 42, 606, cx + 42, 656], start=15, end=165, fill=WHITE, width=7)
# body
d.rounded_rectangle([cx - 150, 716, cx + 150, 800], radius=30, fill=ROBOT)
d.rounded_rectangle([cx - 150, 716, cx + 150, 800], radius=30, outline=ROBOT_DARK, width=5)
# chest light: a tiny leaderboard bar chart (rank going nowhere)
d.rectangle([cx - 78, 756, cx - 54, 782], fill=YELLOW)
d.rectangle([cx - 34, 744, cx - 10, 782], fill=WHITE)
d.rectangle([cx + 10, 762, cx + 34, 782], fill=WHITE)
d.rectangle([cx + 54, 750, cx + 78, 782], fill=WHITE)
# arms: one raised in a shrug, one holding a coffee cup
d.line([(cx - 150, 736), (cx - 208, 690)], fill=ROBOT_DARK, width=16)
d.ellipse([cx - 222, 676, cx - 194, 704], fill=ROBOT_LIGHT)
d.line([(cx + 150, 736), (cx + 208, 742)], fill=ROBOT_DARK, width=16)
d.rounded_rectangle([cx + 196, 700, cx + 244, 760], radius=8, fill=COFFEE)
d.rectangle([cx + 196, 700, cx + 244, 714], fill=(255, 255, 255))

# ---- punchline pill ----
d.rounded_rectangle([90, 838, 990, 946], radius=54, fill=GREEN)
d.rounded_rectangle([90, 838, 990, 946], radius=54, outline=GREEN_DARK, width=4)
centered(d, 862, "STILL SUBMITTING.", fit_font("STILL SUBMITTING.", 820, 62), WHITE)

# ---- footer ----
centered(d, 978, "make.fun", font(34), GREY)

img.save("meme.png")
print("saved meme.png", img.size)
