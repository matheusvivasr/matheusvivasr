#!/usr/bin/env python3
"""Sincroniza partes do README com o perfil público do Gravatar.

- Texto (localização + links de contas verificadas): reescrito a cada execução,
  entre os marcadores <!-- gravatar:location --> e <!-- gravatar:links -->.
- Imagens (banner + quadrada do cabeçalho): só refeitas quando a foto muda no
  Gravatar (comparando o image_id salvo em assets/.gravatar-state.json), para
  não sobrescrever recortes bons enquanto a foto for a mesma.

O hash é público (é o mesmo que aparece na URL do avatar), então não há segredo aqui.
Rodado pelo workflow .github/workflows/gravatar-sync.yml.
"""
from __future__ import annotations
import json, os, re, sys, urllib.request

HASH = "1afa0bc66f32532d62ebac1f0f55adfa"   # md5 do e-mail do Gravatar (público)
SLUG = "matheusvivasr"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
ASSETS = os.path.join(ROOT, "assets")
STATE = os.path.join(ASSETS, ".gravatar-state.json")
BANNER_RATIO = 2.5          # largura/altura do banner
UA = {"User-Agent": "Mozilla/5.0 (gravatar-sync)"}

# contas do Gravatar que viram badge (github é omitido: redundante aqui)
BADGE = {
    "linkedin":  ("LinkedIn",  "0A66C2", "linkedin"),
    "twitter":   ("X",         "000000", "x"),
    "x":         ("X",         "000000", "x"),
    "spotify":   ("Spotify",   "1DB954", "spotify"),
    "instagram": ("Instagram", "E4405F", "instagram"),
    "mastodon":  ("Mastodon",  "6364FF", "mastodon"),
    "youtube":   ("YouTube",   "FF0000", "youtube"),
}


def get(url: str, binary: bool = False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")


def fetch_profile() -> dict:
    raw = get(f"https://gravatar.com/{HASH}.json")
    return json.loads(raw)["entry"][0]


def replace_between(text: str, tag: str, new: str) -> str:
    pat = re.compile(rf"(<!-- gravatar:{tag} -->).*?(<!-- /gravatar:{tag} -->)", re.S)
    if not pat.search(text):
        print(f"  aviso: marcador '{tag}' não encontrado no README")
        return text
    return pat.sub(lambda m: m.group(1) + new + m.group(2), text)


def build_links(accounts: list[dict]) -> str:
    badges = []
    for a in accounts:
        if a.get("is_hidden"):
            continue
        short = (a.get("shortname") or "").lower()
        url = a.get("url", "")
        if short == "github" or short not in BADGE:
            continue
        if not url.startswith("https") or not url.isascii():
            continue  # descarta link malformado (ex.: spotify com caractere estranho)
        label, color, logo = BADGE[short]
        disp = (a.get("display") or a.get("username") or label).replace("-", "--").replace("_", "__")
        badges.append(f"[![{label}](https://img.shields.io/badge/{label}-{disp}-{color}"
                      f"?style=flat&logo={logo}&logoColor=white)]({url})")
    return "\n" + "\n".join(badges) + "\n" if badges else "\n"


def crop_images(entry: dict) -> bool:
    """Refaz banner+quadrada se o image_id do cabeçalho mudou. Retorna True se mexeu."""
    hdr = entry.get("header_image") or {}
    image_id = hdr.get("image_id")
    state = {}
    if os.path.exists(STATE):
        try: state = json.load(open(STATE, encoding="utf-8"))
        except Exception: state = {}
    have = os.path.exists(os.path.join(ASSETS, "banner-jabuti.jpg"))
    if image_id and image_id == state.get("header_image_id") and have:
        return False  # mesma foto, recortes atuais preservados
    if not image_id:
        return False
    try:
        from PIL import Image
        import io
        # a URL da imagem do cabeçalho só está no HTML do perfil
        html = get(f"https://gravatar.com/{SLUG}")
        m = re.search(rf"https://\d\.gravatar\.com/userimage/\d+/{image_id}", html)
        if not m:
            print("  aviso: URL do header não encontrada no HTML; imagens mantidas")
            return False
        img = Image.open(io.BytesIO(get(m.group(0) + "?size=2048", binary=True))).convert("RGB")
        w, h = img.size
        fx = float(hdr.get("position_x", 50)) / 100.0
        fy = float(hdr.get("position_y", 50)) / 100.0
        # banner: largura cheia, altura = w/ratio, centrado no ponto focal vertical
        bh = min(h, round(w / BANNER_RATIO))
        top = max(0, min(h - bh, round(h * fy - bh / 2)))
        img.crop((0, top, w, top + bh)).save(os.path.join(ASSETS, "banner-jabuti.jpg"),
                                              quality=88, optimize=True)
        # quadrada: lado = menor dimensão, centrada no ponto focal
        side = min(w, h, 900)
        cx, cy = round(w * fx), round(h * fy)
        l = max(0, min(w - side, cx - side // 2))
        t = max(0, min(h - side, cy - side // 2))
        img.crop((l, t, l + side, t + side)).save(os.path.join(ASSETS, "jabuti.jpg"),
                                                   quality=88, optimize=True)
        json.dump({"header_image_id": image_id}, open(STATE, "w", encoding="utf-8"))
        print(f"  imagens refeitas (novo header_image_id={image_id})")
        return True
    except Exception as e:
        print(f"  aviso: falha ao refazer imagens ({e}); texto sincronizado mesmo assim")
        return False


def main() -> int:
    entry = fetch_profile()
    location = (entry.get("currentLocation") or "").strip()
    text = open(README, encoding="utf-8").read()
    before = text
    if location:
        text = replace_between(text, "location", location)
    text = replace_between(text, "links", build_links(entry.get("accounts", [])))
    changed_txt = text != before
    if changed_txt:
        open(README, "w", encoding="utf-8", newline="\n").write(text)
        print("README (texto) atualizado")
    else:
        print("README (texto) já estava em dia")
    crop_images(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
