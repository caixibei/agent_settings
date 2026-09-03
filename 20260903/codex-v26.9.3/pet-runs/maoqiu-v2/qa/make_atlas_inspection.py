from pathlib import Path

from PIL import Image

ATLAS = Path(r"C:\Users\caixi\.Codex\pet-runs\maoqiu-v2\final\spritesheet-name-badge.webp")
OUTPUT = Path(r"C:\Users\caixi\.Codex\pet-runs\maoqiu-v2\qa\atlas-name-badge-inspection.png")


def main() -> None:
    atlas = Image.open(ATLAS).convert("RGBA")
    background = Image.new("RGBA", atlas.size, (44, 48, 54, 255))
    background.alpha_composite(atlas)
    background.resize((atlas.width * 2, atlas.height * 2), Image.Resampling.NEAREST).save(OUTPUT)


if __name__ == "__main__":
    main()
