from PIL import Image, ImageDraw
from pathlib import Path
import math

asset = Path("assets/coder-room.gif")
source = Image.open(asset)
source.seek(0)
base = source.convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
frames = []
count = 16

for i in range(count):
    frame = base.copy().convert("RGBA")
    overlay = Image.new("RGBA", frame.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    phase = 2 * math.pi * i / count

    # CRT refresh line and blinking terminal cursor. The camera never moves.
    scan_y = 181 + ((i * 5) % 67)
    draw.rectangle((400, scan_y, 476, scan_y + 1), fill=(118, 244, 236, 120))
    if (i // 2) % 2 == 0:
        draw.rectangle((460, 236, 463, 239), fill=(133, 255, 226, 230))

    # Slow cup steam movement.
    for k, x0 in enumerate((519, 528, 537)):
        rise = (i * 2 + k * 5) % 25
        sway = int(3 * math.sin(phase + k * 1.5))
        alpha = 110 + int(45 * (0.5 + 0.5 * math.sin(phase + k)))
        points = [
            (x0 + sway, 279 - rise),
            (x0 + 2 + sway, 273 - rise),
            (x0 - 2 + sway, 267 - rise),
            (x0 + 2 + sway, 260 - rise),
        ]
        draw.line(points, fill=(204, 231, 229, alpha), width=1)

    # Light rain outside the window.
    for k in range(10):
        x = 18 + (k * 13) % 103
        y = 148 + ((k * 17 + i * 4) % 75)
        draw.line((x, y, x - 1, y + 4 + (k % 2)), fill=(105, 226, 226, 70), width=1)

    led = 110 + int(110 * (0.5 + 0.5 * math.sin(phase * 2)))
    draw.ellipse((593, 248, 596, 251), fill=(93, 239, 212, led))
    frames.append(Image.alpha_composite(frame, overlay).convert("RGB"))

palette = frames[0].quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
indexed[0].save(
    asset,
    save_all=True,
    append_images=indexed[1:],
    duration=135,
    loop=0,
    optimize=True,
    disposal=1,
)
print(f"Regenerated {asset} as a fixed-camera {count}-frame ambient loop.")
