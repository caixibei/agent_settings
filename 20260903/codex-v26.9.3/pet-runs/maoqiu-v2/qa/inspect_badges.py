from pathlib import Path

from PIL import Image

ATLAS = Path(r"C:\Users\caixi\.Codex\pets\maoqiu\spritesheet.webp")
OUTPUT = Path(r"C:\Users\caixi\.Codex\pet-runs\maoqiu-v2\qa\badge-name-inspection.png")
CELL_WIDTH = 192
CELL_HEIGHT = 208


def main() -> None:
    atlas = Image.open(ATLAS).convert("RGBA")
    canvas = Image.new("RGBA", (CELL_WIDTH * 6, CELL_HEIGHT * 4), (44, 48, 54, 255))
    samples = ((0, 0), (0, 3), (4, 0), (9, 0), (10, 4), (10, 7))

    for index, (row, column) in enumerate(samples):
        cell = atlas.crop((column * CELL_WIDTH, row * CELL_HEIGHT, (column + 1) * CELL_WIDTH, (row + 1) * CELL_HEIGHT))
        enlarged = cell.resize((CELL_WIDTH * 2, CELL_HEIGHT * 2), Image.Resampling.NEAREST)
        x = (index % 3) * CELL_WIDTH * 2
        y = (index // 3) * CELL_HEIGHT * 2
        canvas.alpha_composite(enlarged, (x, y))

    canvas.save(OUTPUT)


if __name__ == "__main__":
    main()
