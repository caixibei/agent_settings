import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SOURCE = Path(r"C:\Users\caixi\.Codex\pets\maoqiu\spritesheet.webp")
CENTERS = Path(r"C:\Users\caixi\.Codex\pet-runs\maoqiu-v2\qa\badge-centers.json")
OUTPUT = Path(r"C:\Users\caixi\.Codex\pet-runs\maoqiu-v2\final\spritesheet-name-badge.webp")
REPORT = Path(r"C:\Users\caixi\.Codex\pet-runs\maoqiu-v2\qa\name-badge-report.json")
FONT = Path(r"C:\Windows\Fonts\msyhbd.ttc")
CELL_WIDTH = 192
CELL_HEIGHT = 208
NAME = "毛球"


def is_safe_badge(cell: str, badge: dict[str, float]) -> bool:
    x = badge["x"]
    y = badge["y"]
    width = badge["width"]
    height = badge["height"]
    return (
        x is not None
        and 58 <= x <= 138
        and 96 <= y <= 154
        and 7 <= width <= 13
        and 7 <= height <= 12
    )


def draw_badge(atlas: Image.Image, x: float, y: float) -> None:
    scale = 4
    badge_width = 23
    badge_height = 11
    layer = Image.new("RGBA", (badge_width * scale, badge_height * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle((0, 0, badge_width * scale - 1, badge_height * scale - 1), radius=5 * scale, fill=(190, 194, 195, 255), outline=(83, 87, 89, 255), width=scale)
    draw.rounded_rectangle((2 * scale, 2 * scale, badge_width * scale - 1, badge_height * scale - 1), radius=3 * scale, outline=(230, 232, 232, 170), width=scale)
    font = ImageFont.truetype(str(FONT), 7 * scale)
    text_box = draw.textbbox((0, 0), NAME, font=font)
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]
    draw.text(((badge_width * scale - text_width) / 2, (badge_height * scale - text_height) / 2 - scale), NAME, font=font, fill=(30, 33, 35, 255))
    badge = layer.resize((badge_width, badge_height), Image.Resampling.LANCZOS)
    atlas.alpha_composite(badge, (round(x - badge_width / 2), round(y - badge_height / 2)))


def main() -> None:
    atlas = Image.open(SOURCE).convert("RGBA")
    centers = json.loads(CENTERS.read_text(encoding="utf-8"))
    applied = []
    skipped = []

    for cell, badge in centers.items():
        if not is_safe_badge(cell, badge):
            skipped.append(cell)
            continue
        row, column = (int(value) for value in cell.split("-"))
        cell_layer = Image.new("RGBA", (CELL_WIDTH, CELL_HEIGHT), (0, 0, 0, 0))
        crop = atlas.crop((column * CELL_WIDTH, row * CELL_HEIGHT, (column + 1) * CELL_WIDTH, (row + 1) * CELL_HEIGHT))
        cell_layer.alpha_composite(crop)
        draw_badge(cell_layer, badge["x"], badge["y"])
        atlas.paste(cell_layer, (column * CELL_WIDTH, row * CELL_HEIGHT), cell_layer)
        applied.append(cell)

    pixels = atlas.load()
    for y in range(atlas.height):
        for x in range(atlas.width):
            red, green, blue, alpha = pixels[x, y]
            if alpha == 0 and (red or green or blue):
                pixels[x, y] = (0, 0, 0, 0)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    atlas.save(OUTPUT, format="WEBP", lossless=True, quality=100, method=6, exact=True)
    REPORT.write_text(json.dumps({"name": NAME, "applied": applied, "skipped": skipped}, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
