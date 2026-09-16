import json
from collections import deque
from pathlib import Path

from PIL import Image

ATLAS = Path(r"C:\Users\caixi\.Codex\pets\maoqiu\spritesheet.webp")
OUTPUT = Path(r"C:\Users\caixi\.Codex\pet-runs\maoqiu-v2\qa\badge-centers.json")
CELL_WIDTH = 192
CELL_HEIGHT = 208


def is_badge_pixel(pixel: tuple[int, int, int, int]) -> bool:
    red, green, blue, alpha = pixel
    return alpha > 180 and min(red, green, blue) > 138 and max(red, green, blue) - min(red, green, blue) < 55


def find_badge(cell: Image.Image) -> dict[str, float]:
    pixels = cell.load()
    visited: set[tuple[int, int]] = set()
    components: list[list[tuple[int, int]]] = []

    for y in range(95, 180):
        for x in range(55, 140):
            if (x, y) in visited or not is_badge_pixel(pixels[x, y]):
                continue
            queue = deque([(x, y)])
            visited.add((x, y))
            component: list[tuple[int, int]] = []
            while queue:
                px, py = queue.popleft()
                component.append((px, py))
                for nx, ny in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
                    if 55 <= nx < 140 and 95 <= ny < 180 and (nx, ny) not in visited and is_badge_pixel(pixels[nx, ny]):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            if len(component) >= 8:
                components.append(component)

    candidates = []
    for component in components:
        xs = [point[0] for point in component]
        ys = [point[1] for point in component]
        width = max(xs) - min(xs) + 1
        height = max(ys) - min(ys) + 1
        if 7 <= width <= 26 and 7 <= height <= 26 and 0.55 <= width / height <= 1.8:
            candidates.append(component)
    if not candidates:
        return {"x": None, "y": None, "width": 0, "height": 0, "pixels": 0}

    badge = max(candidates, key=len)
    return {
        "x": round(sum(point[0] for point in badge) / len(badge), 2),
        "y": round(sum(point[1] for point in badge) / len(badge), 2),
        "width": max(point[0] for point in badge) - min(point[0] for point in badge) + 1,
        "height": max(point[1] for point in badge) - min(point[1] for point in badge) + 1,
        "pixels": len(badge),
    }


def main() -> None:
    atlas = Image.open(ATLAS).convert("RGBA")
    result = {}
    for row in range(11):
        for column in range(8):
            cell = atlas.crop((column * CELL_WIDTH, row * CELL_HEIGHT, (column + 1) * CELL_WIDTH, (row + 1) * CELL_HEIGHT))
            result[f"{row}-{column}"] = find_badge(cell)
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
