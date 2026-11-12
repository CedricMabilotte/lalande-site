"""Visuels de partage : partage/{fr,en}-{carre,story,paysage}.jpg"""
import pathlib, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

SITE = pathlib.Path(sys.argv[1]); URL = sys.argv[2].replace("https://", "").rstrip("/")
SRC = Image.open(SITE / "photos/vue-aerienne-ferme.jpg").convert("RGB")
OUT = SITE / "partage"; OUT.mkdir(exist_ok=True)
F = "/usr/share/fonts/truetype/"
serif = lambda n: ImageFont.truetype(F + "dejavu/DejaVuSerif.ttf", n)
sans = lambda n: ImageFont.truetype(F + "liberation/LiberationSans-Regular.ttf", n)
sansb = lambda n: ImageFont.truetype(F + "liberation/LiberationSans-Bold.ttf", n)
NOIR, DOUX, VERT = (31, 31, 28), (102, 100, 92), (61, 90, 42)

TX = {
 "fr": dict(sur="À TRANSMETTRE · HAUTE-VIENNE", titre=["Ferme bio", "de 94 ha"],
            l=["Élevage Limousin inscrit HBL", "Bio depuis plus de 30 ans", "Bâti, eau, bois, verger"],
            prix="900 000 €", cible="Pour un collectif ou un porteur de projet préfinancé"),
 "en": dict(sur="FOR TRANSFER · HAUTE-VIENNE, FRANCE", titre=["94 ha", "organic farm"],
            l=["Pedigree Limousin herd (HBL)", "Organic for over 30 years", "Buildings, water, woods, orchard"],
            prix="€900,000", cible="For a pre-financed collective or project leader"),
}

def bloc(d, x, y, w, t, k):
    """Écrit le bloc de texte ; k = échelle."""
    d.text((x, y), t["sur"], font=sansb(int(22*k)), fill=VERT); y += int(48*k)
    for ligne in t["titre"]:
        d.text((x, y), ligne, font=serif(int(64*k)), fill=NOIR); y += int(76*k)
    y += int(14*k)
    for ligne in t["l"]:
        d.text((x, y), ligne, font=sans(int(28*k)), fill=NOIR); y += int(40*k)
    y += int(18*k)
    d.text((x, y), t["prix"], font=sansb(int(40*k)), fill=NOIR); y += int(60*k)
    d.text((x, y), t["cible"], font=sans(int(22*k)), fill=DOUX); y += int(36*k)
    d.line((x, y + int(8*k), x + w, y + int(8*k)), fill=(230, 228, 222), width=2); y += int(26*k)
    d.text((x, y), URL, font=sans(int(22*k)), fill=VERT)
    return y + int(30*k)

def vertical(t, W, H, photo_h, k, pad):
    im = Image.new("RGB", (W, H), "white")
    im.paste(ImageOps.fit(SRC, (W, photo_h), centering=(.5, .5)), (0, 0))
    bloc(ImageDraw.Draw(im), pad, photo_h + pad, W - 2*pad, t, k)
    return im

def paysage(t):
    W, H = 1200, 630; pw = 600
    im = Image.new("RGB", (W, H), "white")
    im.paste(ImageOps.fit(SRC, (pw, H)), (0, 0))
    bloc(ImageDraw.Draw(im), pw + 48, 44, W - pw - 96, t, .8)
    return im

for lang, t in TX.items():
    vertical(t, 1080, 1080, 440, 1.08, 60).save(OUT / f"{lang}-carre.jpg", quality=86)
    vertical(t, 1080, 1920, 940, 1.7, 80).save(OUT / f"{lang}-story.jpg", quality=86)
    paysage(t).save(OUT / f"{lang}-paysage.jpg", quality=86)
print(sorted(p.name for p in OUT.iterdir()))
