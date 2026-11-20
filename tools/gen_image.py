#!/usr/bin/env python3
"""Генерация картинок в стиле YAA через Nano Banana (gemini-3-pro-image).

Правила стиля: ILLUSTRATIONS.md. Референсы: refs/. Ключ: переменная GEMINI_API_KEY.

  python3 tools/gen_image.py --kind monkey --prompt "..." --out out.webp [--ratio 16:9] [--width 1400]

--kind: monkey | tentacle | glass3d | field | mix   (от него зависят референсы и блок промпта)
Текст, логотипы и цифры модель не рисует: добавляй их в вёрстке.
"""
import argparse, base64, glob, io, json, os, sys, urllib.request, random
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "gemini-3-pro-image"

REFS = {
    "monkey": ["refs/monkeys/*", "refs/posts/482_1030*", "refs/posts/611_2*"],
    "tentacle": ["refs/graphics/949_216*", "refs/posts/482_389*", "refs/brandbook-slides/848_378*"],
    "glass3d": ["refs/3d/*", "refs/brandbook-slides/848_468*"],
    "field": ["refs/posts/487_134*", "refs/posts/970_233*", "refs/brandbook-slides/848_797*"],
    "mix": ["refs/brandbook-slides/848_418*", "refs/brandbook-slides/848_783*", "refs/posts/662_1530*"],
}

BLOCK = {
    "monkey": "Black-and-white high-contrast photo of a monkey (chimpanzee or macaque), cleanly cut out, "
              "expressive, dressed in human clothes, holding a prop. Flat solid background. A flat vector green "
              "tentacle with black outline and suckers may pass BEHIND the subject.",
    "tentacle": "Flat 2D vector tentacles of an octopus: solid fill #00E67E, thick black outline, round suckers, "
                "bold graphic shapes, no realism. They wrap around the scene as a frame or a connecting element.",
    "glass3d": "Glossy 3D glass objects in translucent green, sharp reflections, product-render quality, on a flat "
               "black background. One hero object, simple composition.",
    "field": "Flat solid colour field composition, one hero object, bold shapes, a lot of empty space for a headline.",
    "mix": "Combine a black-and-white photo monkey with flat green vector tentacles and a glass 3D object. "
           "The tentacle passes behind the subject.",
}

COMMON = ("Use the reference images only as the brand style (do not copy their composition or text). "
          "YAA brand illustration. Colours ONLY: green #00E67E, black #0E0E0E, blue #444FC5, white. "
          "Strictly no text, no letters, no numbers, no logos, no watermarks, no gradients, no glow, no blur, "
          "no red, no yellow, no orange. Keep the top 30% of the frame empty for a headline, painted in the SAME single "
          "background colour as the rest (one continuous background, no bands, no separate stripes).")


def refs_for(kind, limit=3):
    files = []
    for pat in REFS[kind]:
        files += sorted(glob.glob(os.path.join(ROOT, pat)))
    files = [f for f in files if f.lower().endswith((".webp", ".png", ".jpg"))]
    random.Random(0).shuffle(files)
    return files[:limit]


def png_b64(path, side=1024):
    im = Image.open(path).convert("RGB")
    im.thumbnail((side, side))
    buf = io.BytesIO()
    im.save(buf, "PNG")
    return base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", required=True, choices=list(REFS))
    ap.add_argument("--prompt", required=True, help="сцена по-английски: что и где происходит")
    ap.add_argument("--out", required=True)
    ap.add_argument("--ratio", default="16:9")
    ap.add_argument("--width", type=int, default=1400)
    ap.add_argument("--bg", default=None, help="green #00E67E | black #0E0E0E | blue #444FC5 (по умолчанию: чёрный для glass3d, зелёный для остальных)")
    ap.add_argument("--refs", type=int, default=3, help="сколько референсов передать")
    a = ap.parse_args()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("Нужна переменная GEMINI_API_KEY")
    rf = refs_for(a.kind, a.refs)
    if not a.bg:
        a.bg = "black #0E0E0E" if a.kind == "glass3d" else "green #00E67E"
    parts = [{"inline_data": {"mime_type": "image/png", "data": png_b64(f)}} for f in rf]
    text = f"{COMMON} {BLOCK[a.kind]} Background: {a.bg}. Scene: {a.prompt}. Aspect ratio {a.ratio}."
    parts.append({"text": text})
    body = {"contents": [{"parts": parts}], "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": a.ratio}}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={key}",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    d = json.load(urllib.request.urlopen(req, timeout=300))
    img = next((p["inlineData"]["data"] for c in d.get("candidates", []) for p in c["content"]["parts"] if "inlineData" in p), None)
    if not img:
        sys.exit("Модель не вернула картинку: " + json.dumps(d)[:400])
    im = Image.open(io.BytesIO(base64.b64decode(img))).convert("RGB")
    h = round(a.width * im.height / im.width)
    im.resize((a.width, h), Image.LANCZOS).save(a.out, "WEBP", quality=82)
    print(f"OK {a.out} {a.width}x{h}, refs: {[os.path.basename(f) for f in rf]}")


if __name__ == "__main__":
    main()
