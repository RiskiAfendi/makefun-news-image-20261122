from pathlib import Path
import json
import sys

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "stories_2026-11-22.json"
OUTPUT = ROOT / "assets" / "entry.png"
PREVIEW300 = ROOT / "assets" / "previews" / "entry-300.png"

SIZE = 1024
IVORY = "#F7F3E9"
INK = "#14213C"
RED = "#A9322D"
TEAL = "#23767A"
OCHRE = "#C89034"
GREEN = "#497A56"
WHITE = "#FFFFFF"

SANS = "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def centered(draw, xy, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    w = box[2] - box[0]
    x = xy[0] - w / 2
    draw.text((x, xy[1]), text, font=fnt, fill=fill)


def draw_icon(draw, cx, cy, kind, color):
    if kind == "cop31-gavel":
        draw.ellipse((cx - 62, cy - 62, cx + 62, cy + 62), fill=WHITE, outline=TEAL, width=5)
        draw.arc((cx - 44, cy - 44, cx + 44, cy + 44), 20, 160, fill=TEAL, width=6)
        draw.rectangle((cx - 38, cy - 8, cx + 38, cy + 12), fill=INK)
        draw.rectangle((cx - 12, cy + 12, cx + 12, cy + 58), fill=OCHRE)
        draw.line((cx - 48, cy - 14, cx + 48, cy - 14), fill=RED, width=5)
    elif kind == "kyiv-rescue":
        draw.polygon([(cx - 68, cy + 48), (cx - 46, cy - 30), (cx - 12, cy - 48),
                      (cx + 16, cy - 18), (cx + 66, cy + 48)], fill="#D8E2E8", outline=INK)
        draw.rectangle((cx - 54, cy - 18, cx - 18, cy + 42), fill=RED)
        draw.rectangle((cx + 12, cy - 8, cx + 48, cy + 42), fill=OCHRE)
        draw.polygon([(cx - 80, cy - 52), (cx - 20, cy - 52), (cx - 44, cy - 8)],
                     fill=INK)
        draw.line((cx - 82, cy + 48, cx + 82, cy + 48), fill=INK, width=5)
    else:
        draw.ellipse((cx - 70, cy - 46, cx + 70, cy + 46), fill="#D8E2E8", outline=INK, width=4)
        draw.polygon([(cx - 58, cy - 12), (cx - 8, cy - 22), (cx + 58, cy + 8),
                      (cx + 38, cy + 36), (cx - 42, cy + 28)], fill=INK)
        draw.polygon([(cx - 12, cy - 55), (cx + 8, cy - 42), (cx + 28, cy - 55),
                      (cx + 18, cy - 24)], fill=RED)
        draw.line((cx - 72, cy + 58, cx + 72, cy + 58), fill=TEAL, width=5)


def draw_secondary_icon(draw, cx, cy, index):
    colors = [RED, TEAL, GREEN, OCHRE, INK, TEAL, OCHRE]
    color = colors[index % len(colors)]
    if index == 0:
        draw.rectangle((cx - 24, cy - 24, cx + 24, cy + 24), fill="#D8E2E8", outline=INK, width=3)
        draw.rectangle((cx - 18, cy - 16, cx - 8, cy - 6), outline=INK)
        draw.rectangle((cx + 8, cy - 16, cx + 18, cy - 6), outline=INK)
        draw.line((cx - 18, cy + 8, cx + 18, cy + 8), fill=RED, width=4)
    elif index == 1:
        draw.polygon([(cx - 28, cy + 24), (cx - 20, cy - 14), (cx, cy - 28),
                      (cx + 20, cy - 14), (cx + 28, cy + 24)], fill="#D8E2E8", outline=INK)
        draw.rectangle((cx - 8, cy - 4, cx + 8, cy + 24), fill=color)
    elif index == 2:
        draw.rectangle((cx - 30, cy - 22, cx + 30, cy + 22), fill=WHITE, outline=INK, width=3)
        draw.line((cx, cy - 14, cx, cy + 14), fill=RED, width=5)
        draw.line((cx - 14, cy, cx + 14, cy), fill=RED, width=5)
    elif index == 3:
        draw.rectangle((cx - 32, cy - 20, cx + 32, cy + 20), fill=OCHRE, outline=INK, width=3)
        for x in (cx - 18, cx, cx + 18):
            draw.ellipse((x - 5, cy - 5, x + 5, cy + 5), fill=WHITE)
    elif index == 4:
        draw.polygon([(cx - 30, cy + 22), (cx - 18, cy - 22), (cx + 18, cy - 22),
                      (cx + 30, cy + 22)], fill=INK)
        draw.rectangle((cx - 20, cy - 8, cx + 20, cy + 6), fill=WHITE)
    elif index == 5:
        draw.line((cx - 32, cy + 22, cx - 32, cy - 20), fill=INK, width=4)
        draw.polygon([(cx - 32, cy - 18), (cx + 24, cy - 18), (cx + 32, cy + 20),
                      (cx - 24, cy + 20)], fill="#D8E2E8", outline=INK)
    else:
        draw.rectangle((cx - 34, cy - 22, cx + 34, cy + 22), fill=WHITE, outline=INK, width=3)
        draw.polygon([(cx - 26, cy + 12), (cx - 10, cy - 12), (cx + 4, cy + 12)],
                     fill=TEAL)
        draw.polygon([(cx - 4, cy + 12), (cx + 12, cy - 12), (cx + 26, cy + 12)],
                     fill=OCHRE)


def render():
    data = json.loads(CONTENT.read_text(encoding="utf-8"))
    image = Image.new("RGB", (SIZE, SIZE), IVORY)
    draw = ImageDraw.Draw(image)

    masthead = font(SERIF_BOLD, 54)
    date_font = font(SANS_BOLD, 30)
    deck_font = font(SANS_BOLD, 18)
    label_font = font(SANS_BOLD, 12)
    headline_font = font(SERIF_BOLD, 27)
    detail_font = font(SANS, 14)
    secondary_head = font(SANS_BOLD, 15)
    brief_font = font(SANS, 13)

    draw.rectangle((0, 0, 1024, 126), fill=IVORY)
    centered(draw, (512, 8), data["title"], masthead, INK)
    draw.rectangle((16, 70, 1008, 112), fill=RED)
    centered(draw, (512, 74), data["date"], date_font, WHITE)
    centered(draw, (512, 122), data["deck"], deck_font, INK)

    region_y = 158
    draw.rectangle((16, region_y, 1008, region_y + 28), fill=INK)
    centered(draw, (512, region_y + 4), "GLOBAL  ·  AFRICA  ·  EUROPE  ·  AMERICAS  ·  ASIA  ·  MIDDLE EAST", font(SANS_BOLD, 14), WHITE)

    y1 = 198
    h1 = 290
    lead_widths = [456, 268, 268]
    x_positions = [16, 472, 740]
    leads = data["leads"]
    for i, (lead, x, w) in enumerate(zip(leads, x_positions, lead_widths)):
        right = x + w
        fill = WHITE
        draw.rectangle((x, y1, right, y1 + h1), fill=fill, outline=INK, width=3)
        accent = RED if i == 0 else (TEAL if i == 1 else OCHRE)
        draw.rectangle((x, y1, right, y1 + 30), fill=accent)
        draw.text((x + 10, y1 + 7), lead["region"], font=label_font, fill=WHITE)
        draw.text((x + 10, y1 + 42), lead["location"], font=label_font, fill=INK)
        lines = wrap(draw, lead["headline"], headline_font, w - 20)
        ty = y1 + 68
        for line in lines[:3]:
            draw.text((x + 10, ty), line, font=headline_font, fill=INK)
            ty += 29
        icon_y = y1 + 188
        draw_icon(draw, x + w / 2, icon_y, lead["illustration"], accent)
        detail_lines = wrap(draw, lead["detail"], detail_font, w - 20)
        dy = y1 + 236
        for line in detail_lines[:2]:
            draw.text((x + 10, dy), line, font=detail_font, fill=INK)
            dy += 17
        draw.rectangle((x + 10, y1 + 270, x + 96, y1 + 286), fill=RED if lead["status"] == "REPORTED" else TEAL)
        draw.text((x + 14, y1 + 270), lead["status"], font=label_font, fill=WHITE)

    secondary_y = 500
    secondary_h = 260
    card_w = (992 - 6 * 7) // 7
    secondary = data["secondary"]
    for i, card in enumerate(secondary[:7]):
        x = 16 + i * (card_w + 7)
        draw.rectangle((x, secondary_y, x + card_w, secondary_y + secondary_h),
                       fill=WHITE, outline=INK, width=2)
        draw.rectangle((x, secondary_y, x + card_w, secondary_y + 24), fill=INK)
        loc_font = font(SANS_BOLD, 9)
        location = card["location"]
        if len(location) > 16:
            location = location[:15] + "..."
        centered(draw, (x + card_w / 2, secondary_y + 5), location, loc_font, WHITE)
        draw_secondary_icon(draw, x + card_w / 2, secondary_y + 66, i)
        lines = wrap(draw, card["headline"], secondary_head, card_w - 12)
        hy = secondary_y + 104
        for line in lines[:4]:
            draw.text((x + 6, hy), line, font=secondary_head, fill=INK)
            hy += 17
        detail_lines = wrap(draw, card["detail"], font(SANS, 11), card_w - 12)
        dy = secondary_y + 182
        for line in detail_lines[:3]:
            draw.text((x + 6, dy), line, font=font(SANS, 11), fill=INK)
            dy += 13
        status = card["status"]
        draw.rectangle((x + 6, secondary_y + 238, x + 58, secondary_y + 254), fill=TEAL)
        draw.text((x + 10, secondary_y + 239), status, font=label_font, fill=WHITE)

    brief_y = 772
    draw.rectangle((16, brief_y, 1008, 944), fill=WHITE, outline=INK, width=2)
    draw.rectangle((16, brief_y, 1008, brief_y + 38), fill=INK)
    draw.text((28, brief_y + 8), "ALSO ON SUNDAY", font=font(SANS_BOLD, 18), fill=WHITE)
    brief_font = font(SANS, 14)
    for i, brief in enumerate(data["briefs"][:3]):
        col = i % 2
        row = i // 2
        bx = 28 + col * 488
        by = brief_y + 52 + row * 34
        draw.ellipse((bx, by + 5, bx + 8, by + 13), fill=RED)
        draw.text((bx + 16, by), brief, font=brief_font, fill=INK)

    draw.rectangle((16, 956, 1008, 1008), fill=INK)
    footer_font = font(SANS, 11)
    draw.text((28, 966), "SUNDAY 22 NOVEMBER 2026 · EVENTS / FIRST REPORTS", font=footer_font, fill=WHITE)
    draw.text((28, 984), "STATUS: QUALIFIED · REPORTED · PRELIMINARY · ESTIMATE", font=footer_font, fill=WHITE)
    draw.text((606, 966), "19:00 WIB FACT BASELINE", font=footer_font, fill=WHITE)
    draw.text((606, 984), "PROVISIONAL · 23:00 DELTA PENDING", font=footer_font, fill=WHITE)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    PREVIEW300.parent.mkdir(parents=True, exist_ok=True)
    image.resize((300, 300), Image.Resampling.LANCZOS).save(PREVIEW300, format="PNG", optimize=True)
    print(OUTPUT)
    print(PREVIEW300)


if __name__ == "__main__":
    render()
