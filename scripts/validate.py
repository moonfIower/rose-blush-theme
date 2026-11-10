"""Check release metadata, local assets, and core palette contrast."""
import json
from pathlib import Path
import re
import struct

ROOT = Path(__file__).resolve().parents[1]
VERSION = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)")


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def luminance(color):
    channels = [int(color[index:index + 2], 16) / 255 for index in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    return sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))


def check_contrast(label, fg, bg, minimum=4.5):
    low, high = sorted((luminance(fg), luminance(bg)))
    ratio = (high + 0.05) / (low + 0.05)
    if minimum is None:
        print(f"{label}: {ratio:.2f}:1 (informational)")
        return
    require(ratio >= minimum, f"{label} contrast {ratio:.2f}:1 is below {minimum}:1")
    print(f"{label}: {ratio:.2f}:1")


manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
require(manifest.get("name") == "Rose Blush", "Unexpected theme name")
require(isinstance(manifest.get("author"), str) and manifest["author"].strip(),
        "Missing author")
for key in ("version", "minAppVersion"):
    require(VERSION.fullmatch(manifest.get(key, "")), f"Invalid {key}")

for name in ("README.md", "LICENSE", "theme.css"):
    require((ROOT / name).is_file() and (ROOT / name).stat().st_size, f"Missing {name}")

css = (ROOT / "theme.css").read_text(encoding="utf-8")
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
require(not re.search(r"@import\b", css, re.I), "CSS imports are disallowed")
for url in re.findall(r"url\(\s*(.*?)\s*\)", css, flags=re.I | re.S):
    require(url.strip("\"'").startswith("data:image/"), "Asset must be an inline image")

for mode in ("light", "dark"):
    block = re.search(r"\.theme-" + mode + r"\s*\{([^}]+)\}", css).group(1)
    colors = dict(re.findall(r"--([\w-]+):\s*#([0-9a-fA-F]{6});", block))
    # The original muted light palette includes intentional low-contrast pairs.
    text_minimum = None if mode == "light" else 4.5
    for surface in ("background-primary", "background-primary-alt", "background-secondary"):
        for text in ("text-normal", "text-muted", "text-faint", "text-accent", "blush-heading", "blush-code"):
            check_contrast(f"{mode} {text} on {surface}", colors[text], colors[surface],
                           text_minimum)
    for token in ("rose-control-accent", "rose-control-accent-hover"):
        check_contrast(f"{mode} warm-white on {token}", "fffdfc", colors[token])
    check_contrast(f"{mode} keyboard focus", colors["background-modifier-border-focus"],
                   colors["background-primary"], 3)

store = ROOT / "screenshots/light.png"
if store.exists():
    with store.open("rb") as file:
        header = file.read(24)
    require(header.startswith(b"\x89PNG\r\n\x1a\n") and
            struct.unpack(">II", header[16:24]) == (512, 288),
            "Store PNG must be 512 × 288")
else:
    print("Store screenshot pending (screenshots/light.png)")
print("Static release checks passed.")
