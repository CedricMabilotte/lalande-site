"""Génère index.html (FR) et en/index.html (EN) du site La Lande."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
BASE = (sys.argv[2] if len(sys.argv)>2 else "https://cedricmabilotte.github.io/lalande-site/").rstrip("/")+"/"
import urllib.parse as U
TEL, TEL_HREF = "06 44 87 29 37", "+33644872937"
MAIL = "lucileloup.66@gmail.com"

T = {
 "fr": dict(
  lang="fr", autre="en/", autre_txt="English", css="style.css",
  title="Ferme de La Lande — ferme bio de 94 ha à transmettre",
  desc="Ferme familiale certifiée bio depuis plus de 30 ans, 94 ha d'un seul tenant, élevage de sélection Limousine HBL, à transmettre.",
  h1="Ferme de La Lande",
  path="", og_locale="fr_FR",
  share_t="Partager l'annonce", share_intro="Vous connaissez un collectif ou un porteur de projet que ce lieu pourrait intéresser ? Faites-lui suivre l'annonce.",
  share_msg="Ferme bio de 94 ha à transmettre en Haute-Vienne : élevage Limousin inscrit, bâti, eau, bois et verger. Pour un collectif ou un porteur de projet préfinancé.",
  copier="Copier le lien", copie="Lien copié", partager="Partager…",
  vis_t="Visuels prêts à publier", vis_intro="À télécharger et publier avec le texte ci-dessus.",
  vis=[("carre","Carré 1080 × 1080","Instagram, Facebook"),("story","Story 1080 × 1920","stories Instagram, Facebook, WhatsApp"),("paysage","Paysage 1200 × 630","Facebook, LinkedIn, X, Telegram")],
  texte_t="Texte à copier",
  chiffres="94 ha d'un seul tenant · Bio depuis plus de 30 ans · Limousines inscrites HBL",
  lieu="Haute-Vienne, Limousin",
  chapo="Au cœur d'un environnement naturel préservé, une ferme familiale conduite avec exigence et respect du vivant, aujourd'hui disponible pour transmission.",
  alt=["Vue aérienne de la ferme : bâtiments, prairies, verger et haies","La cour, les dépendances en pierre et le hangar","La stabulation, les Limousines au cornadis","Une vache Limousine du troupeau au pré","Le bocage autour de la ferme, prairies et bois"],
  pour_t="Idéal pour",
  pour=["Des éleveurs souhaitant reprendre un outil structuré en AB et un cheptel de Limousines inscrites",
        "Un petit groupe de jeunes agriculteur·ices en installation",
        "Un projet d'écolieu à base productive agricole et multi-activités",
        "Une famille cherchant autonomie et viabilité économique"],
  bati_t="Le bâti",
  bati=["Maison d'habitation de 177 m² habitables, classée C, chauffage géothermique",
        "Une stabulation et une grande grange",
        "Un hangar à foin et des dépendances : poulaillers, toits à cochons, ateliers, garage tracteur",
        "Un four à pain traditionnel avec son labo de préparation"],
  elevage_t="L'élevage",
  elevage="L'exploitation repose principalement sur un élevage de sélection de vaches Limousines inscrites au Herd-Book Limousin (HBL), avec une attention particulière portée au bien-être animal et à l'équilibre des sols. Le troupeau est reconnu pour sa robustesse, sa cohésion et son comportement calme, développés au fil des ans. Il a des qualités bouchères et surtout allaitantes, et constitue un outil de production structuré et transmissible.",
  terres_t="Les terres, l'eau, le vivant",
  terres="Les prairies permanentes et temporaires assurent l'autonomie en foin. Elles sont bordées de haies anciennes, corridors écologiques qui favorisent une biodiversité riche : oiseaux, pollinisateurs, vie des sols. S'y ajoutent deux bois de 5 hectares et un verger de 70 pommiers de variétés anciennes locales, planté il y a 26 ans. L'eau est présente sur le domaine (puits, forage, étang, ruisseau) et garantit l'autonomie.",
  usages_t="Ce que le lieu permet",
  usages=["Poursuivre un élevage biologique de qualité","L'agroécologie et le pâturage tournant",
          "La diversification en polyculture et agroforesterie","La transformation : boulangerie, cuisine participative",
          "Les circuits courts","L'accueil pédagogique et l'animation culturelle",
          "L'installation d'un collectif qui expérimente un écolieu productif, fondé sur la préservation des écosystèmes"],
  prix_t="Prix",
  prix_note="Le prix sera mis à jour le jour de la vente selon l'évolution du troupeau et des stocks.",
  comprend="Il comprend :",
  compo=["la maison : 90&nbsp;000&nbsp;€","tout le bâti : 150&nbsp;000&nbsp;€","une grande partie du matériel agricole (tracteurs, équipements) : 110&nbsp;000&nbsp;€",
         "le cheptel inscrit HBL, 50 vaches mères et leurs veaux : 220&nbsp;000&nbsp;€","les stocks : 30&nbsp;000&nbsp;€","le foncier : 300&nbsp;000&nbsp;€"],
  dossier="Un dossier détaillé est disponible sur demande : détail du cheptel, données économiques, plans parcellaires, diagnostics.",
  cand_t="Pour les candidats",
  cand="La ferme est encore en activité, la reprise peut donc être immédiate. Le travail quotidien avec les animaux ne permet pas de répondre à toutes les demandes : seuls les projets préfinancés souhaitant poursuivre en agriculture biologique seront considérés. Merci de votre bienveillance et de votre compréhension.",
  contact_t="Contact",
  contact_txt="Par téléphone ou par mail, en présentant votre projet et son financement.",
  footer="Ferme de La Lande · annonce de transmission",
 ),
 "en": dict(
  lang="en", autre="../", autre_txt="Français", css="../style.css",
  title="La Lande farm — 94 ha organic farm available for transfer",
  desc="Family farm certified organic for over 30 years, 94 ha in a single block, pedigree Limousin suckler herd (HBL), available for transfer.",
  h1="La Lande farm",
  path="en/", og_locale="en_GB",
  share_t="Share this listing", share_intro="Do you know a collective or a project leader who might be interested? Please pass the listing on.",
  share_msg="94 ha organic farm available for transfer in Haute-Vienne, France: pedigree Limousin herd, buildings, water, woods and orchard. For pre-financed collectives or project leaders.",
  copier="Copy link", copie="Link copied", partager="Share…",
  vis_t="Ready-to-post images", vis_intro="Download and post them with the text above.",
  vis=[("carre","Square 1080 × 1080","Instagram, Facebook"),("story","Story 1080 × 1920","Instagram, Facebook and WhatsApp stories"),("paysage","Landscape 1200 × 630","Facebook, LinkedIn, X, Telegram")],
  texte_t="Text to copy",
  chiffres="94 ha in a single block · Organic for over 30 years · Pedigree Limousin herd (HBL)",
  lieu="Haute-Vienne, Limousin, France",
  chapo="Set in an unspoilt natural environment, a family farm managed with high standards and respect for living things, now available for transfer.",
  alt=["Aerial view of the farm: buildings, meadows, orchard and hedgerows","The farmyard, stone outbuildings and shed","The cattle shed, Limousin cows at the feeding rail","A Limousin cow from the herd in the meadow","The hedged farmland around the farm, meadows and woods"],
  pour_t="Ideal for",
  pour=["Livestock farmers wishing to take over a well-structured organic operation and a pedigree Limousin herd",
        "A small group of young farmers setting up",
        "An eco-place project with a productive, multi-activity farming base",
        "A family seeking self-sufficiency and economic viability"],
  bati_t="Buildings",
  bati=["A 177 m² farmhouse, energy rating C, geothermal heating",
        "A cattle shed (loose housing) and a large barn",
        "A hay shed and outbuildings: henhouses, pigsties, workshops, tractor garage",
        "A traditional bread oven with its bakery room"],
  elevage_t="The herd",
  elevage="The farm is mainly based on breeding pedigree Limousin cows registered in the Limousin Herd-Book (HBL), with particular attention to animal welfare and soil balance. The herd is known for its hardiness, cohesion and calm temperament, developed over the years. It has good beef and, above all, excellent maternal qualities, making it a well-structured, transferable production asset.",
  terres_t="Land, water, wildlife",
  terres="Permanent and temporary grassland provides self-sufficiency in hay. It is bordered by ancient hedgerows, ecological corridors supporting rich biodiversity: birds, pollinators, soil life. There are also two woods of 5 hectares and a 26-year-old orchard of 70 apple trees of old local varieties. Water is available on the property (well, borehole, pond, stream), ensuring self-sufficiency.",
  usages_t="What the place allows",
  usages=["Continuing high-quality organic livestock farming","Agroecology and rotational grazing",
          "Diversifying into mixed farming and agroforestry","Processing: bread-making, participatory cooking",
          "Short supply chains and direct sales","Educational visits and cultural events",
          "A collective experimenting with a productive eco-place founded on ecosystem preservation"],
  prix_t="Price",
  prix_note="The price will be adjusted on the day of sale according to changes in herd numbers and stocks.",
  comprend="It includes:",
  compo=["the house: €90,000","all buildings: €150,000","most of the farm machinery (tractors, equipment): €110,000",
         "the HBL-registered herd, 50 suckler cows and their calves: €220,000","stocks: €30,000","the land: €300,000"],
  dossier="A detailed information pack is available on request: herd details, financial data, parcel maps, surveys and diagnostics.",
  cand_t="For prospective buyers",
  cand="The farm is still operating, so it can be taken over immediately. Daily work with the animals means we cannot answer every enquiry: only pre-financed projects committed to continuing organic farming will be considered. Thank you kindly for your understanding.",
  contact_t="Contact",
  contact_txt="By phone or email, with a short presentation of your project and its financing.",
  footer="La Lande farm · transfer listing",
 ),
}

def li(xs): return "\n".join(f"      <li>{x}</li>" for x in xs)

def share(t, url):
    pre = "" if t["lang"]=="fr" else "../"
    m = U.quote(t["share_msg"]); u = U.quote(url, safe="")
    links = [("WhatsApp", f"https://wa.me/?text={m}%20{u}"),
             ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={u}"),
             ("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={u}"),
             ("Telegram", f"https://t.me/share/url?url={u}&text={m}"),
             ("X", f"https://x.com/intent/post?text={m}&url={u}"),
             ("Email", f"mailto:?subject={U.quote(t['title'])}&body={m}%0A%0A{u}")]
    btn = "".join(f'<a class="btn" href="{h}" target="_blank" rel="noopener">{n}</a>' for n,h in links)
    vis = "".join(f'<figure class="vis vis-{k}"><a href="{pre}partage/{t["lang"]}-{k}.jpg" download><img src="{pre}partage/{t["lang"]}-{k}.jpg" alt="{l}" loading="lazy"></a><figcaption><strong>{l}</strong><br>{use}</figcaption></figure>' for k,l,use in t["vis"])
    return f"""  <section class="partage" id="partager">
    <h2>{t['share_t']}</h2>
    <p>{t['share_intro']}</p>
    <div class="btns">{btn}<button type="button" class="btn" data-copier="{url}" data-ok="{t['copie']}">{t['copier']}</button><button type="button" class="btn natif" hidden data-titre="{t['title']}" data-texte="{t['share_msg']}" data-url="{url}">{t['partager']}</button></div>
    <h3>{t['texte_t']}</h3>
    <p class="texte-partage">{t['share_msg']}<br>{url}</p>
    <h3>{t['vis_t']}</h3>
    <p class="note">{t['vis_intro']}</p>
    <div class="visuels">{vis}</div>
  </section>"""

JS = """<script>
document.querySelectorAll('[data-copier]').forEach(function(b){b.addEventListener('click',function(){
  var t=b.textContent;(navigator.clipboard?navigator.clipboard.writeText(b.dataset.copier):Promise.reject()).then(function(){b.textContent=b.dataset.ok;setTimeout(function(){b.textContent=t},2000)}).catch(function(){prompt('',b.dataset.copier)})})});
var n=document.querySelector('.natif');if(n&&navigator.share){n.hidden=false;n.addEventListener('click',function(){navigator.share({title:n.dataset.titre,text:n.dataset.texte,url:n.dataset.url}).catch(function(){})})}
</script>"""

def page(t):
    url = BASE + t["path"]
    pre = "" if t["lang"]=="fr" else "../"
    def ph(f, alt): return f'<div class="photo"><img src="{pre}photos/{f}" alt="{alt}" loading="lazy"></div>'
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="alternate" hreflang="{'en' if t['lang']=='fr' else 'fr'}" href="{t['autre']}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['desc']}">
<meta property="og:image" content="{BASE}partage/{t['lang']}-paysage.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{t['alt'][0]}">
<meta property="og:locale" content="{t['og_locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{t['css']}">
</head>
<body>
<div class="wrap">
<header class="top"><span>{t['lieu']}</span><a href="{t['autre']}" lang="{'en' if t['lang']=='fr' else 'fr'}">{t['autre_txt']}</a></header>
<main>
  <div class="hero">
    <h1>{t['h1']}</h1>
    <div class="chiffres">{t['chiffres']}</div>
    <p class="chapo">{t['chapo']}</p>
  </div>
  <div class="photo grande">{ph('vue-aerienne-ferme.jpg', t['alt'][0]).split('>',1)[1].rsplit('</div>',1)[0].replace('loading="lazy"','fetchpriority="high"')}</div>

  <section>
    <h2>{t['pour_t']}</h2>
    <ul class="pour">
{li(t['pour'])}
    </ul>
  </section>
  <section>
    <h2>{t['bati_t']}</h2>
    <ul>
{li(t['bati'])}
    </ul>
    <div class="galerie">{ph('cour.jpg', t['alt'][1])}{ph('stabulation.jpg', t['alt'][2])}</div>
  </section>
  <section>
    <h2>{t['elevage_t']}</h2>
    <p>{t['elevage']}</p>
    <div class="galerie">{ph('limousines.jpg', t['alt'][3])}</div>
  </section>
  <section>
    <h2>{t['terres_t']}</h2>
    <p>{t['terres']}</p>
    <div class="galerie">{ph('paysage-bocage.jpg', t['alt'][4])}</div>
  </section>
  <section>
    <h2>{t['usages_t']}</h2>
    <ul>
{li(t['usages'])}
    </ul>
  </section>
  <section>
    <h2>{t['prix_t']}</h2>
    <div class="prix">
      <div class="montant">{"900&nbsp;000&nbsp;€" if t["lang"]=="fr" else "€900,000"}</div>
      <p>{t['comprend']}</p>
      <ul>
{li(t['compo'])}
      </ul>
      <p class="note">{t['prix_note']}</p>
      <p class="note">{t['dossier']}</p>
    </div>
  </section>
  <section>
    <h2>{t['cand_t']}</h2>
    <p>{t['cand']}</p>
  </section>
  <div class="contact" id="contact">
    <h2>{t['contact_t']}</h2>
    <p>{t['contact_txt']}</p>
    <a href="tel:{TEL_HREF}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a>
  </div>
{share(t, url)}
</main>
<footer>{t['footer']}</footer>
</div>
{JS}
</body>
</html>
"""

(OUT / "index.html").write_text(page(T["fr"]), encoding="utf-8")
(OUT / "en" / "index.html").write_text(page(T["en"]), encoding="utf-8")
print("ok")
