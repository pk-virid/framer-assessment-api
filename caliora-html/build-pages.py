#!/usr/bin/env python3
"""Generate interior pages of the Caliora HTML template from a shared shell."""
import pathlib

ROOT = pathlib.Path(__file__).parent

HEAD = """<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Caliora Dental Clinic Template</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/main.css" />
</head>
<body>
"""

NAV = """<nav class="nav{navdark}">
  <div class="container nav__inner">
    <a class="nav__brand" href="index.html">
      <span class="nav__logo">Caliora</span>
      <span class="nav__slogan">Dental Clinic · Dubai</span>
    </a>
    <ul class="nav__links">
      <li class="nav__item">
        <a class="nav__link" href="#">Pages <span class="nav__caret">▾</span></a>
        <div class="dropdown dropdown--wide">
          <a href="index.html"><b>Home</b><span>Main landing page</span></a>
          <a href="about.html"><b>About</b><span>Story, values &amp; team</span></a>
          <a href="conditions.html"><b>Conditions</b><span>What we treat</span></a>
          <a href="treatments.html"><b>Treatments</b><span>All services</span></a>
          <a href="cases.html"><b>Cases</b><span>Treatment journeys</span></a>
          <a href="equipment.html"><b>Equipment</b><span>Clinic technology</span></a>
          <a href="blog.html"><b>Blog</b><span>Educational articles</span></a>
          <a href="gallery.html"><b>Gallery</b><span>Inside the clinic</span></a>
          <a href="locations.html"><b>Locations</b><span>Two Dubai clinics</span></a>
          <a href="contact.html"><b>Contact</b><span>Book a consultation</span></a>
        </div>
      </li>
      <li class="nav__item">
        <a class="nav__link" href="conditions.html">Conditions <span class="nav__caret">▾</span></a>
        <div class="dropdown">
          <a href="condition-detail.html"><b>Cosmetic Dentistry</b><span>Veneers, whitening &amp; smile design</span></a>
          <a href="condition-detail.html"><b>Restorative Dentistry</b><span>Repair and protect natural teeth</span></a>
          <a href="condition-detail.html"><b>Implantology</b><span>Replace missing teeth</span></a>
          <a href="condition-detail.html"><b>Orthodontics</b><span>Discreet alignment options</span></a>
        </div>
      </li>
      <li class="nav__item">
        <a class="nav__link" href="treatments.html">Treatments <span class="nav__caret">▾</span></a>
        <div class="dropdown dropdown--wide">
          <a href="treatment-detail.html"><b>Emergency Dental Care</b></a>
          <a href="treatment-detail.html"><b>General Dentistry &amp; Prevention</b></a>
          <a href="treatment-detail.html"><b>Veneers &amp; Smile Design</b></a>
          <a href="treatment-detail.html"><b>Teeth Whitening</b></a>
          <a href="treatment-detail.html"><b>Crowns &amp; Bridges</b></a>
          <a href="treatment-detail.html"><b>Ceramic &amp; Lingual Braces</b></a>
          <a href="treatment-detail.html"><b>Orthodontics &amp; Invisalign</b></a>
          <a href="treatment-detail.html"><b>Dental Implants</b></a>
        </div>
      </li>
      <li class="nav__item">
        <a class="nav__link" href="locations.html">Locations <span class="nav__caret">▾</span></a>
        <div class="dropdown">
          <a href="location-detail.html"><b>Jumeirah</b><span>Al Wasl Road, Dubai</span></a>
          <a href="location-detail.html"><b>Downtown Dubai</b><span>Boulevard Plaza</span></a>
        </div>
      </li>
    </ul>
    <a class="btn" href="contact.html">Book a consultation</a>
    <button class="nav__burger" aria-label="Menu"><i></i><i></i><i></i></button>
  </div>
</nav>
"""

FOOTER = """<footer class="footer">
  <div class="container">
    <div class="footer__cols">
      <div>
        <div class="footer__logo">Caliora</div>
        <p class="footer__tag">Dentist &amp; dental clinic template for Dubai practices. Replace with your clinic details.</p>
        <a class="btn" href="contact.html" style="display:inline-flex">Schedule your visit</a>
      </div>
      <div>
        <h5>Explore</h5>
        <a href="index.html">Home</a><a href="about.html">About</a><a href="conditions.html">Conditions</a>
        <a href="treatments.html">Treatments</a><a href="cases.html">Cases</a><a href="equipment.html">Equipment</a>
      </div>
      <div>
        <h5>More</h5>
        <a href="blog.html">Blog</a><a href="gallery.html">Gallery</a><a href="contact.html">Contact</a>
        <a href="locations.html">Locations</a><a href="style-guide.html">Style guide</a>
        <a href="instructions.html">Instructions</a><a href="licenses.html">Licences</a>
      </div>
      <div>
        <h5>Visit us</h5>
        <a href="location-detail.html">Jumeirah — Al Wasl Road, Dubai</a>
        <a href="location-detail.html">Downtown — Boulevard Plaza, Dubai</a>
        <a href="tel:+97140000000">+971 4 000 0000</a>
        <a href="mailto:hello@yourclinic.ae">hello@yourclinic.ae</a>
      </div>
    </div>
    <div class="footer__licence">
      <span>MOHAP Licence No. XX-0000000 · DHA Facility Licence No. 0000000 — replace with your licence numbers before publishing.</span>
      <span>© <span data-year></span> Your Clinic Name</span>
    </div>
  </div>
  <div class="marquee" aria-hidden="true">
    <div class="marquee__track"><span>Caliora — Dental Clinic Dubai —&nbsp;</span></div>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def page_hero(eyebrow, title, sub):
    return f"""<header class="page-hero">
  <div class="container">
    <span class="eyebrow" data-reveal>{eyebrow}</span>
    <h1 class="display" data-reveal-mask><span style="display:block">{title}</span></h1>
    <p class="body-lg" data-reveal>{sub}</p>
  </div>
</header>
"""

def cta_band(heading="Questions? Ask a clinician.", btn="Book a consultation"):
    return f"""<section class="section theme-light-subtle section--tight">
  <div class="container">
    <h2 class="h1" style="max-width:620px" data-reveal>{heading}</h2>
    <div style="margin-top:26px" data-reveal><a class="btn" href="contact.html">{btn}</a></div>
  </div>
</section>
"""

def t_card(img, tag, title, summary):
    return f"""<a class="card" href="treatment-detail.html">
  <div class="card__media">
    <img src="{img}" alt="{title}" loading="lazy" />
    <span class="card__tag">{tag}</span>
    <div class="card__overlay"><span>View treatment →</span></div>
  </div>
  <div class="card__body">
    <h3 class="h3">{title}</h3><p class="small">{summary}</p>
    <span class="eyebrow card__more">Learn more</span>
  </div>
</a>"""

IMG = {
  "cosmetic": "https://images.unsplash.com/photo-1606811841689-23dfddce3e95",
  "resto": "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5",
  "implant": "https://images.unsplash.com/photo-1629909613654-28e377c37b09",
  "ortho": "https://images.unsplash.com/photo-1598256989800-fe5f95da9787",
  "clinic": "https://images.unsplash.com/photo-1571772996211-2f02c9727629",
  "clinic2": "https://images.unsplash.com/photo-1588771930296-88c2cb03f386",
  "white": "https://images.unsplash.com/photo-1588773846628-13fce0a32105",
  "chair": "https://images.unsplash.com/photo-1609840114035-3c981b782dfe",
  "tools": "https://images.unsplash.com/photo-1583947215259-38e31be8751f",
  "smile": "https://images.unsplash.com/photo-1607990281513-2c110a25bd8c",
  "dubai1": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c",
  "dubai2": "https://images.unsplash.com/photo-1518684079-3c830dcef090",
  "lounge": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d",
  "consult": "https://images.unsplash.com/photo-1512678080530-7760d81faba6",
}
def u(k, w=1000): return f"{IMG[k]}?w={w}&q=80&fm=jpg"

TREATMENTS = [
  (u("chair"), "Restorative", "Emergency Dental Care", "Same-day appointments for pain, swelling or broken teeth, with clear triage before you travel."),
  (u("clinic"), "Prevention", "General Dentistry & Prevention", "Check-ups, hygiene and preventive planning designed to keep treatment minimal over the long term."),
  (u("smile"), "Cosmetic", "Veneers & Smile Design", "Porcelain veneers planned digitally around your features, with a trial preview before final work."),
  (u("white"), "Cosmetic", "Teeth Whitening", "Professional whitening under clinical supervision, with realistic shade goals agreed before you start."),
  (u("tools"), "Restorative", "Crowns & Bridges", "Precision ceramic restorations that protect weakened teeth and close gaps, matched to your natural shade."),
  (u("ortho"), "Orthodontics", "Ceramic & Lingual Braces", "Low-visibility fixed braces — tooth-coloured ceramic or hidden lingual systems."),
  (u("smile"), "Orthodontics", "Orthodontics & Invisalign", "Clear aligner therapy planned from digital scans, with defined review points and retention included."),
  (u("implant"), "Implantology", "Dental Implants", "Implant-supported crowns and bridges placed after structured assessment of bone, gums and health."),
]

PAGES = {}

# ---------------- about ----------------
PAGES["about.html"] = dict(
  title="About", navdark=False,
  desc="The story, values and DHA-licensed team behind the clinic.",
  body=page_hero("About the clinic", "A clinic built around honest, unhurried dentistry",
    "Replace this story with your own: how the practice started, what it stands for, and the standards patients can expect at every visit.") + f"""
<section class="section--flush"><img src="{u('clinic',2000)}" alt="Clinic interior" style="width:100%;height:520px;object-fit:cover" data-parallax /></section>

<section class="section">
  <div class="container grid grid-4" data-stagger>
    <div class="stat" style="border-color:var(--line)"><div class="stat__value" data-count="12" data-suffix="+">0</div><div class="stat__label" style="color:var(--ink)">Years in practice</div></div>
    <div class="stat" style="border-color:var(--line)"><div class="stat__value" data-count="8">0</div><div class="stat__label" style="color:var(--ink)">DHA-licensed clinicians</div></div>
    <div class="stat" style="border-color:var(--line)"><div class="stat__value" data-count="2">0</div><div class="stat__label" style="color:var(--ink)">Dubai locations</div></div>
    <div class="stat" style="border-color:var(--line)"><div class="stat__value" data-count="6">0</div><div class="stat__label" style="color:var(--ink)">Languages spoken</div></div>
  </div>
</section>

<section class="section theme-light-strong">
  <div class="container features">
    <div>
      <h2 class="h1" data-reveal>How we practise</h2>
      <p class="body-lg" style="margin-top:16px;max-width:440px" data-reveal>Three commitments shape every appointment. Replace them with the principles your clinic follows.</p>
    </div>
    <div data-stagger>
      <div style="padding:24px 0;border-bottom:1px solid var(--line)"><h3 class="h3">Explain before we treat</h3><p class="small" style="color:var(--muted);margin-top:6px">Findings, options, costs and limitations — in plain language, before any decision.</p></div>
      <div style="padding:24px 0;border-bottom:1px solid var(--line)"><h3 class="h3">Prevention first</h3><p class="small" style="color:var(--muted);margin-top:6px">The best treatment plan is the one that keeps future treatment minimal.</p></div>
      <div style="padding:24px 0"><h3 class="h3">Licensed and accountable</h3><p class="small" style="color:var(--muted);margin-top:6px">DHA-licensed clinicians, documented protocols, credentials available on request.</p></div>
    </div>
  </div>
</section>

<section class="section theme-dark-base">
  <div class="container">
    <h2 class="h1" style="margin-bottom:44px" data-reveal>Meet the clinicians</h2>
    <div class="grid grid-3" data-stagger>
      <div class="card"><div class="card__media" style="height:300px"><img src="{u('consult')}" alt="Clinician portrait" loading="lazy" /></div>
        <div class="card__body"><h3 class="h3">Dr. Placeholder Name</h3><span class="small" style="color:var(--gold)">Medical Director · Prosthodontist</span><span class="small">DHA Licence: 00000000</span></div></div>
      <div class="card"><div class="card__media" style="height:300px"><img src="{u('lounge')}" alt="Clinician portrait" loading="lazy" /></div>
        <div class="card__body"><h3 class="h3">Dr. Placeholder Name</h3><span class="small" style="color:var(--gold)">Orthodontist</span><span class="small">DHA Licence: 00000000</span></div></div>
      <div class="card"><div class="card__media" style="height:300px"><img src="{u('clinic2')}" alt="Clinician portrait" loading="lazy" /></div>
        <div class="card__body"><h3 class="h3">Dr. Placeholder Name</h3><span class="small" style="color:var(--gold)">General Dentist</span><span class="small">DHA Licence: 00000000</span></div></div>
    </div>
  </div>
</section>
""" + cta_band("Come and meet us"))

# ---------------- conditions ----------------
cond_slides = ""
for title, summary, img, pills in [
  ("Cosmetic Dentistry", "Veneers, whitening and smile design planned around your facial proportions — discussed openly at consultation, with realistic outcomes.", u("cosmetic",2000), ["Veneers & Smile Design","Teeth Whitening"]),
  ("Restorative Dentistry", "Crowns, bridges and fillings that repair damaged teeth and protect long-term oral health, planned with clear staging and costs.", u("resto",2000), ["Crowns & Bridges","General Dentistry & Prevention"]),
  ("Implantology", "Replacement of missing teeth with implant-supported restorations, following a structured assessment of bone, gums and overall health.", u("implant",2000), ["Dental Implants"]),
  ("Orthodontics", "Discreet alignment with clear aligners or fixed braces, chosen after a full orthodontic assessment — not one-size-fits-all.", u("ortho",2000), ["Orthodontics & Invisalign","Ceramic & Lingual Braces"]),
]:
    pill_html = "".join(f'<a class="pill" href="treatment-detail.html">{p}</a>' for p in pills)
    cond_slides += f"""
  <div class="hero-slide" style="min-height:72vh">
    <div class="hero-slide__bg" data-parallax style="background-image:url('{img}')"></div>
    <div class="container hero-slide__content">
      <h2 class="hero-slide__title" data-reveal>{title}</h2>
      <p class="hero-slide__summary" data-reveal data-delay="0.1">{summary}</p>
      <div class="hero-slide__pills" data-reveal data-delay="0.2">{pill_html}</div>
      <a class="hero-slide__explore" href="condition-detail.html" data-reveal data-delay="0.3"><span class="eyebrow">Explore this specialty →</span></a>
    </div>
  </div>"""

PAGES["conditions.html"] = dict(
  title="Conditions", navdark=False,
  desc="Four specialties: cosmetic, restorative, implantology and orthodontics.",
  body=page_hero("Conditions", "Four specialties, one standard of care",
    "Explore what we treat and how each specialty approaches diagnosis, planning and long-term maintenance.")
  + f'<section class="section--flush">{cond_slides}</section>'
  + cta_band("Not sure which specialty you need?"))

# ---------------- treatments ----------------
cards = "".join(t_card(*t) for t in TREATMENTS)
PAGES["treatments.html"] = dict(
  title="Treatments", navdark=True,
  desc="Eight core dental services with clear scope, staging and aftercare.",
  body=f"""<div class="theme-dark-base">{page_hero("Treatments", "Every treatment, explained before it begins",
    "Eight core services across cosmetic, restorative, implant and orthodontic care — each with clear scope, staging and aftercare.")}
<section class="section section--tight" style="padding-top:0">
  <div class="container grid grid-4" data-stagger>{cards}</div>
</section></div>
<section class="section theme-light-strong">
  <div class="container split">
    <div>
      <h2 class="h1" data-reveal>Fees, staging and what to expect</h2>
      <p class="body-lg" style="margin:16px 0 26px;max-width:480px" data-reveal>Every plan is written, staged and priced before treatment starts. Fees depend on clinical findings, so we discuss ranges at consultation rather than advertising fixed prices.</p>
      <a class="btn" href="contact.html" data-reveal>Ask about a treatment</a>
    </div>
    <img src="{u('resto',1400)}" alt="Treatment room" style="border-radius:18px;height:380px;width:100%;object-fit:cover" data-reveal loading="lazy" />
  </div>
</section>
""")

# ---------------- cases ----------------
def case_card(img, tag, dur, title, body):
    return f"""<div class="card">
  <div class="card__media" style="height:300px"><img src="{img}" alt="{title}" loading="lazy" /></div>
  <div class="card__body">
    <div style="display:flex;gap:10px;align-items:center">
      <span class="card__tag" style="position:static">{tag}</span><span class="small" style="color:var(--muted)">{dur}</span>
    </div>
    <h3 class="h2">{title}</h3><p class="small">{body}</p>
  </div>
</div>"""

PAGES["cases.html"] = dict(
  title="Cases", navdark=False,
  desc="Anonymised treatment journeys shared with patient consent.",
  body=page_hero("Cases", "Real treatment journeys, shared with consent",
    "Each case shows process and staging — not promised outcomes. Individual results vary and depend on clinical findings.") + f"""
<section class="section section--tight" style="padding-top:0">
  <div class="container grid grid-2" data-stagger>
    {case_card(u('smile',1200), "Cosmetic", "6 weeks · 4 visits", "Smile refresh with veneers", "Digital smile design, trial preview, then eight porcelain veneers. Shown with consent as an example of process, not a promised outcome.")}
    {case_card(u('implant',1200), "Implantology", "4 months · staged", "Single implant, back molar", "Assessment with 3D imaging, implant placement, healing period, then a ceramic crown. Timelines depend on healing and vary per patient.")}
    {case_card(u('white',1200), "Cosmetic", "2 visits", "Whitening with edge bonding", "Supervised whitening followed by composite edge bonding to even worn edges. Shown with consent; outcomes differ case by case.")}
    {case_card(u('ortho',1200), "Orthodontics", "9 months", "Aligners for mild crowding", "Clear aligner therapy with scheduled reviews and fixed retention afterwards. Duration reflects this case only.")}
  </div>
</section>
""" + cta_band("Curious what is possible for your case?"))

# ---------------- equipment ----------------
def eq_row(img, title, body):
    return f"""<div class="card" style="flex-direction:row;align-items:center;padding:20px;gap:20px">
  <img src="{img}" alt="{title}" style="width:180px;height:180px;object-fit:cover;border-radius:14px;flex:none" loading="lazy" />
  <div><h3 class="h3">{title}</h3><p class="small" style="color:var(--muted);margin-top:8px">{body}</p></div>
</div>"""

PAGES["equipment.html"] = dict(
  title="Equipment", navdark=False,
  desc="Clinic technology used for diagnosis and treatment.",
  body=page_hero("Equipment", "Technology in service of judgement",
    "The tools we use for diagnosis and treatment — and why each one earns its place in the clinic.") + f"""
<section class="section section--tight" style="padding-top:0">
  <div class="container grid grid-2" data-stagger>
    {eq_row(u('chair'), "3D CBCT imaging", "Cone-beam CT provides three-dimensional views of teeth and bone, used when clinically justified for implant planning and complex root canal cases.")}
    {eq_row(u('tools'), "Intraoral scanning", "Digital scans replace conventional impression trays for most cases, improving comfort and accuracy for aligners, crowns and veneers.")}
    {eq_row(u('resto'), "Operating microscope", "High magnification helps clinicians see fine detail during root canal treatment and precision restorative work.")}
    {eq_row(u('implant'), "Sterilisation suite", "Dedicated decontamination room with validated autoclave cycles and full instrument tracking, in line with DHA infection-control requirements.")}
  </div>
</section>
""" + cta_band("Want to see the clinic in person?", "Book a visit"))

# ---------------- gallery ----------------
gal = ""
for img, cap in [(u('clinic',1200),"Reception"),(u('clinic2',1200),"Treatment room"),(u('lounge',1200),"Patient lounge"),
                 (u('consult',1200),"Consultation room"),(u('chair',1200),"Surgery"),(u('tools',1200),"Instrument bench")]:
    gal += f"""<figure data-reveal><img src="{img}" alt="{cap}" style="border-radius:16px;height:320px;width:100%;object-fit:cover" loading="lazy" /><figcaption class="small" style="color:var(--muted);padding:12px 4px 0">{cap}</figcaption></figure>"""

PAGES["gallery.html"] = dict(
  title="Gallery", navdark=False,
  desc="Inside the clinic — rooms, equipment and spaces.",
  body=page_hero("Gallery", "Inside the clinic", "Rooms, equipment and the spaces where your care happens.")
  + f'<section class="section section--tight" style="padding-top:0"><div class="container grid grid-3">{gal}</div></section>')

# ---------------- blog ----------------
def post_card(img, mins, title, summary):
    return f"""<a class="card" href="blog-post.html">
  <div class="card__media" style="height:200px"><img src="{img}" alt="{title}" loading="lazy" /><div class="card__overlay"><span>Read article →</span></div></div>
  <div class="card__body"><span class="eyebrow">{mins} min read</span><h3 class="h3">{title}</h3><p class="small">{summary}</p></div>
</a>"""

PAGES["blog.html"] = dict(
  title="Blog", navdark=False,
  desc="Educational dental articles from our clinicians.",
  body=page_hero("Blog", "Educational notes from our clinicians",
    "Plain-language guides to common questions. Educational only — not a substitute for clinical examination.") + f"""
<section class="section section--tight" style="padding-top:0">
  <div class="container grid grid-3" data-stagger>
    {post_card(u('clinic2'), 4, "Why preventive care keeps dentistry minimal", "Regular reviews and hygiene visits reduce the need for complex treatment later.")}
    {post_card(u('tools'), 6, "Dental crowns: when they help and what to expect", "Why a dentist may recommend a crown, how visits are staged, and how to care for it.")}
    {post_card(u('ortho'), 5, "Clear aligners vs fixed braces: an honest comparison", "Which option suits which case, and the questions to ask at assessment.")}
    {post_card(u('implant'), 7, "What to expect from a dental implant assessment", "Bone, gums and general health — how suitability is judged before any plan.")}
    {post_card(u('white'), 4, "Tooth sensitivity: causes and calm next steps", "What sensitivity usually means, and when it deserves a clinical look.")}
    {post_card(u('cosmetic'), 5, "Bleeding gums: what your body is telling you", "Early gum inflammation is reversible — here is how hygiene care works.")}
  </div>
</section>
""" + cta_band("Prefer answers about your own teeth?"))

# ---------------- locations ----------------
PAGES["locations.html"] = dict(
  title="Locations", navdark=False,
  desc="Two clinics across Dubai — Jumeirah and Downtown.",
  body=page_hero("Locations", "Two clinics across Dubai",
    "Same clinical standards, same records, one team — choose the location that suits you.") + f"""
<section class="section section--tight" style="padding-top:0">
  <div class="container grid grid-2" data-stagger>
    <a class="card" href="location-detail.html">
      <div class="card__media" style="height:280px"><img src="{u('dubai1',1400)}" alt="Jumeirah clinic" loading="lazy" /></div>
      <div class="card__body"><h3 class="h2">Jumeirah</h3><p class="small">Al Wasl Road, Jumeirah 1, Dubai, UAE</p>
      <span class="small" style="color:var(--gold)">Sat–Thu 9:00–21:00 · Fri 14:00–20:00</span><span class="small" style="color:var(--brand)">+971 4 000 0000</span></div>
    </a>
    <a class="card" href="location-detail.html">
      <div class="card__media" style="height:280px"><img src="{u('dubai2',1400)}" alt="Downtown clinic" loading="lazy" /></div>
      <div class="card__body"><h3 class="h2">Downtown Dubai</h3><p class="small">Boulevard Plaza Tower 1, Downtown Dubai, UAE</p>
      <span class="small" style="color:var(--gold)">Sat–Thu 8:00–20:00 · Fri closed</span><span class="small" style="color:var(--brand)">+971 4 000 0001</span></div>
    </a>
  </div>
</section>
""" + cta_band("Ready to visit?", "Schedule your visit"))

# ---------------- contact ----------------
PAGES["contact.html"] = dict(
  title="Contact", navdark=False,
  desc="Book a consultation at either Dubai clinic.",
  body=f"""<section class="page-hero" style="padding-bottom:110px">
  <div class="container detail-split" style="grid-template-columns:1fr 1.1fr">
    <div>
      <span class="eyebrow" data-reveal>Contact</span>
      <h1 class="display" data-reveal-mask><span style="display:block">Schedule your visit</span></h1>
      <p class="body-lg" data-reveal>Send the form or call either clinic. We reply within one working day.</p>
      <div style="margin-top:34px" data-stagger>
        <div style="padding:18px 0;border-top:1px solid var(--line)"><span class="eyebrow">Phone</span><div class="h3" style="margin-top:4px"><a href="tel:+97140000000">+971 4 000 0000</a></div></div>
        <div style="padding:18px 0;border-top:1px solid var(--line)"><span class="eyebrow">Email</span><div class="h3" style="margin-top:4px"><a href="mailto:hello@yourclinic.ae">hello@yourclinic.ae</a></div></div>
        <div style="padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><span class="eyebrow">Hours</span><div style="margin-top:4px">Sat–Thu 9:00–21:00 · Fri 14:00–20:00</div></div>
      </div>
    </div>
    <form class="form-card" action="#" method="post" data-reveal>
      <h2 class="h2">Request an appointment</h2>
      <input class="field" type="text" name="name" placeholder="Full name" required />
      <input class="field" type="tel" name="phone" placeholder="Phone (+971...)" required />
      <input class="field" type="email" name="email" placeholder="Email" required />
      <select class="field" name="topic">
        <option>General consultation</option><option>Cosmetic dentistry</option>
        <option>Implants</option><option>Orthodontics</option><option>Emergency</option>
      </select>
      <textarea class="field" name="message" placeholder="How can we help?"></textarea>
      <button class="btn" type="submit" style="justify-content:center">Send request</button>
      <p class="small" style="color:var(--muted)">By sending this form you consent to us contacting you about your enquiry. This form is not for medical emergencies — call the clinic directly.</p>
    </form>
  </div>
</section>

<section class="section theme-light-strong">
  <div class="container" style="max-width:900px">
    <h2 class="h1" style="margin-bottom:36px" data-reveal>Common questions</h2>
    <div class="accordion" data-accordion-open-first>
      <div class="accordion__item"><button class="accordion__toggle"><span class="accordion__num">01</span><span class="accordion__title h3">What happens at my first visit?</span><span class="accordion__icon">+</span></button>
        <div class="accordion__panel"><div class="accordion__panel-inner">Your first visit includes a full examination, any imaging that is clinically needed, and a discussion of findings. You receive a written plan with staged costs before any treatment starts.</div></div></div>
      <div class="accordion__item"><button class="accordion__toggle"><span class="accordion__num">02</span><span class="accordion__title h3">Do you work with insurance?</span><span class="accordion__icon">+</span></button>
        <div class="accordion__panel"><div class="accordion__panel-inner">We can provide itemised invoices and reports for reimbursement. Coverage depends on your policy — our front desk will help you check what applies before treatment.</div></div></div>
      <div class="accordion__item"><button class="accordion__toggle"><span class="accordion__num">03</span><span class="accordion__title h3">Will treatment hurt?</span><span class="accordion__icon">+</span></button>
        <div class="accordion__panel"><div class="accordion__panel-inner">Modern local anaesthesia makes most procedures comfortable. Your clinician explains what to expect at each stage and adapts the pace to you.</div></div></div>
      <div class="accordion__item"><button class="accordion__toggle"><span class="accordion__num">04</span><span class="accordion__title h3">How often should I have a check-up?</span><span class="accordion__icon">+</span></button>
        <div class="accordion__panel"><div class="accordion__panel-inner">Most patients benefit from a review every six months, though your dentist may suggest a different interval based on your oral health.</div></div></div>
    </div>
  </div>
</section>
""")

# ---------------- treatment detail ----------------
PAGES["treatment-detail.html"] = dict(
  title="Dental Implants", navdark=True,
  desc="Implant-supported restorations after structured assessment.",
  body=f"""<section class="detail-hero">
  <div class="detail-hero__bg" data-parallax style="background-image:url('{u('implant',2000)}')"></div>
  <div class="container">
    <span class="eyebrow" data-reveal>Treatment</span>
    <h1 class="display" data-reveal-mask><span style="display:block">Dental Implants</span></h1>
    <p class="body-lg" style="color:rgba(255,250,245,0.85)" data-reveal>Implant-supported crowns and bridges placed after structured assessment of bone, gums and general health.</p>
  </div>
</section>

<section class="section">
  <div class="container detail-split">
    <article class="prose" data-reveal>
      <p>Implants replace missing teeth with titanium fixtures supporting ceramic restorations. Treatment begins with a full assessment including imaging, followed by staged placement, healing and restoration.</p>
      <h2>The process</h2>
      <ul>
        <li><b>Assessment</b> — examination, 3D imaging and a written plan with staged costs.</li>
        <li><b>Placement</b> — the implant is positioned under local anaesthesia.</li>
        <li><b>Healing</b> — integration typically takes several weeks; timelines vary per patient.</li>
        <li><b>Restoration</b> — a ceramic crown or bridge is fitted and adjusted.</li>
      </ul>
      <h2>Limitations and considerations</h2>
      <p>Suitability depends on bone volume, gum health and general health. Risks, timelines and maintenance are explained clearly before you commit. Implants require the same daily hygiene and review schedule as natural teeth.</p>
      <div class="disclaimer">Educational content — not a substitute for clinical examination by a DHA-licensed dentist.</div>
    </article>
    <aside class="sticky-side" data-reveal>
      <div class="side-card">
        <span class="eyebrow">At a glance</span>
        <p class="small" style="color:var(--muted)">Scope, visits and fees are confirmed at consultation after examination. Ask for the written plan before deciding.</p>
        <a class="btn" href="contact.html" style="justify-content:center">Ask about this treatment</a>
      </div>
    </aside>
  </div>
</section>
""" + cta_band())

# ---------------- condition detail ----------------
PAGES["condition-detail.html"] = dict(
  title="Implantology", navdark=True,
  desc="Replacement of missing teeth with implant-supported restorations.",
  body=f"""<section class="detail-hero">
  <div class="detail-hero__bg" data-parallax style="background-image:url('{u('implant',2000)}')"></div>
  <div class="container">
    <span class="eyebrow" data-reveal>Condition</span>
    <h1 class="display" data-reveal-mask><span style="display:block">Implantology</span></h1>
    <p class="body-lg" style="color:rgba(255,250,245,0.85)" data-reveal>Replacement of missing teeth with implant-supported restorations, following a structured assessment.</p>
  </div>
</section>

<section class="section">
  <div class="container detail-split">
    <article class="prose" data-reveal>
      <p>Implant treatment replaces missing teeth with titanium fixtures that support crowns or bridges. Suitability depends on bone volume, gum health and general health, which are assessed before any plan is confirmed.</p>
      <h2>When to seek care</h2>
      <p>Consider an assessment if you have a missing tooth, a failing tooth that may need extraction, or a loose denture you would like to stabilise. Early assessment preserves more options.</p>
      <div class="disclaimer">Educational content — not a substitute for clinical examination by a DHA-licensed dentist.</div>
    </article>
    <aside class="sticky-side" data-reveal>
      <div class="side-card">
        <span class="eyebrow">Related treatments</span>
        <a class="pill" style="border-color:var(--line);background:var(--bg);color:var(--ink)" href="treatment-detail.html">Dental Implants</a>
        <a class="btn" href="contact.html" style="justify-content:center">Book a consultation</a>
      </div>
    </aside>
  </div>
</section>
""" + cta_band())

# ---------------- blog post ----------------
PAGES["blog-post.html"] = dict(
  title="Dental crowns: when they help", navdark=False,
  desc="When a dentist may recommend a crown and what to expect.",
  body=f"""<header class="page-hero" style="text-align:center;padding-bottom:40px">
  <div class="container" style="max-width:800px">
    <span class="eyebrow" data-reveal>6 min read</span>
    <h1 class="h1" data-reveal-mask style="margin-top:14px"><span style="display:block">Dental crowns: when they help and what to expect</span></h1>
    <p class="body-lg" data-reveal style="margin:18px auto 0">Why a dentist may recommend a crown, how visits are staged, and how to care for the restoration.</p>
  </div>
</header>
<div class="container" style="max-width:1000px" data-reveal>
  <img src="{u('tools',1600)}" alt="Ceramic dental crowns" style="border-radius:20px;height:480px;width:100%;object-fit:cover" />
</div>
<section class="section section--tight">
  <div class="container" style="max-width:760px">
    <article class="prose" data-reveal>
      <p>A crown is recommended when a tooth is too weakened for a filling to protect it reliably — after root canal treatment, a large fracture, or extensive decay.</p>
      <h2>How visits are staged</h2>
      <p>Assessment and preparation come first, usually with a temporary crown fitted while the final ceramic restoration is made. At the fit appointment your dentist checks shade, contact points and bite before cementing.</p>
      <h2>Caring for a crown</h2>
      <p>Crowns need the same daily hygiene as natural teeth and benefit from regular reviews. With good care, restorations typically serve for many years — your dentist will explain what to expect for your case.</p>
      <div class="disclaimer">This article is educational and does not replace a clinical examination by a DHA-licensed dentist.</div>
    </article>
  </div>
</section>
""" + cta_band("Questions about a recommended crown?"))

# ---------------- location detail ----------------
PAGES["location-detail.html"] = dict(
  title="Jumeirah", navdark=True,
  desc="Our Jumeirah clinic on Al Wasl Road, Dubai.",
  body=f"""<section class="detail-hero" style="min-height:55vh">
  <div class="detail-hero__bg" data-parallax style="background-image:url('{u('dubai1',2000)}')"></div>
  <div class="container">
    <span class="eyebrow" data-reveal>Location</span>
    <h1 class="display" data-reveal-mask><span style="display:block">Jumeirah</span></h1>
    <p class="body-lg" style="color:rgba(255,250,245,0.85)" data-reveal>Al Wasl Road, Jumeirah 1, Dubai, UAE</p>
  </div>
</section>
<section class="section">
  <div class="container detail-split">
    <article class="prose" data-reveal>
      <p>Our Jumeirah clinic offers the full range of services including cosmetic consultations, implant assessment and hygiene. Free parking is available on site. Replace these details with your DHA-licensed facility information.</p>
    </article>
    <aside data-reveal>
      <div style="padding:18px 0;border-bottom:1px solid var(--line)"><span class="eyebrow">Hours</span><p style="margin-top:4px">Sat–Thu 9:00–21:00 · Fri 14:00–20:00</p></div>
      <div style="padding:18px 0;border-bottom:1px solid var(--line)"><span class="eyebrow">Phone</span><p style="margin-top:4px"><a href="tel:+97140000000">+971 4 000 0000</a></p></div>
      <div style="padding:18px 0"><span class="eyebrow">Address</span><p style="margin-top:4px">Al Wasl Road, Jumeirah 1, Dubai, UAE</p></div>
    </aside>
  </div>
</section>
""" + cta_band("Ready to visit Jumeirah?", "Schedule your visit"))

# ---------------- style guide / instructions / licenses ----------------
PAGES["style-guide.html"] = dict(
  title="Style guide", navdark=False,
  desc="Design system of the Caliora template.",
  body=page_hero("Style guide", "Design system", "Tokens, type and components used across the template.") + """
<section class="section theme-light-strong section--tight">
  <div class="container" data-stagger>
    <span class="eyebrow">Typography</span>
    <p class="display">Display — Fraunces</p>
    <p class="h1">Heading 1 — Fraunces</p>
    <p class="h2">Heading 2 — Fraunces</p>
    <p class="h3">Heading 3 — Fraunces</p>
    <p class="body-lg" style="max-width:640px">Body — Instrument Sans. Used for paragraphs and long-form content across the template.</p>
    <p class="small" style="color:var(--muted)">Small — captions and metadata.</p>
    <p class="eyebrow">Eyebrow — labels</p>
  </div>
</section>
<section class="section section--tight">
  <div class="container">
    <span class="eyebrow" style="display:block;margin-bottom:20px">Color tokens</span>
    <div class="grid" style="grid-template-columns:repeat(5,1fr)" data-stagger>
      <div style="background:var(--bg);border:1px solid var(--line);border-radius:14px;height:120px;display:flex;align-items:flex-end;padding:12px"><span class="small">Background</span></div>
      <div style="background:var(--surface);border:1px solid var(--line);border-radius:14px;height:120px;display:flex;align-items:flex-end;padding:12px"><span class="small">Surface</span></div>
      <div style="background:var(--brand);border-radius:14px;height:120px;display:flex;align-items:flex-end;padding:12px"><span class="small" style="color:var(--cream)">Brand</span></div>
      <div style="background:var(--gold);border-radius:14px;height:120px;display:flex;align-items:flex-end;padding:12px"><span class="small" style="color:var(--cream)">Accent Gold</span></div>
      <div style="background:var(--deep);border-radius:14px;height:120px;display:flex;align-items:flex-end;padding:12px"><span class="small" style="color:var(--cream)">Deep</span></div>
    </div>
    <span class="eyebrow" style="display:block;margin:50px 0 20px">Buttons</span>
    <div style="display:flex;gap:16px;flex-wrap:wrap">
      <a class="btn" href="#">Primary button</a>
      <a class="btn btn--outline" href="#">Secondary button</a>
      <a class="large-link" href="#">Large link <span class="arrow">→</span></a>
    </div>
  </div>
</section>
""")

PAGES["instructions.html"] = dict(
  title="Instructions", navdark=False,
  desc="How to customise this template.",
  body=page_hero("Template instructions", "Customising this template", "Everything is plain HTML, CSS variables and one JS file.") + """
<section class="section section--tight" style="padding-top:0">
  <div class="container"><article class="prose" data-reveal>
    <h2>1. Branding</h2>
    <p>Rename the brand in the nav and footer of each page, and change the color tokens at the top of <code>assets/css/main.css</code>. Every component uses tokens, so updating <code>--brand</code>, <code>--gold</code> and <code>--deep</code> restyles the whole site.</p>
    <h2>2. Content</h2>
    <p>Replace the placeholder copy, images and statistics with your clinic's real, verifiable information. Placeholder images are hot-linked from Unsplash — swap in your own photography before launch.</p>
    <h2>3. Compliance (UAE)</h2>
    <p>Replace the MOHAP/DHA licence placeholders in the footer with your facility's real licence numbers. Have your Medical Director approve all marketing copy. Avoid guarantees, superlatives and unverifiable claims — the template copy is written to stay within DHA advertising guidelines.</p>
    <h2>4. Forms</h2>
    <p>Point the contact and newsletter forms at your endpoint (Formspark, Basin, your backend) by setting each form's <code>action</code> attribute.</p>
    <h2>5. Animations</h2>
    <p>All motion lives in <code>assets/js/main.js</code> (GSAP + ScrollTrigger). Add <code>data-reveal</code>, <code>data-stagger</code>, <code>data-parallax</code>, <code>data-count</code> or <code>data-reveal-mask</code> to any element to opt in. Reduced-motion preferences are respected automatically.</p>
  </article></div>
</section>
""")

PAGES["licenses.html"] = dict(
  title="Licences", navdark=False,
  desc="Asset and font licences for this template.",
  body=page_hero("Licences", "Assets and licences", "What ships with the template and under which terms.") + """
<section class="section section--tight" style="padding-top:0">
  <div class="container"><article class="prose" data-reveal>
    <p>Placeholder photography is hot-linked from Unsplash under the Unsplash License; replace with your own clinic photography before launch for best results.</p>
    <p>Fonts: Fraunces and Instrument Sans, both available under the SIL Open Font License via Google Fonts. Animations use GSAP via CDN under its standard license.</p>
    <p>All copy in this template is original and written for DHA/MOHAP advertising compliance. Update licence numbers, clinic details and any statistics with your own verified information.</p>
  </article></div>
</section>
""")

for fname, cfg in PAGES.items():
    navdark = " nav--dark" if cfg.get("navdark") else ""
    html = HEAD.format(title=cfg["title"], desc=cfg["desc"]) + NAV.format(navdark=navdark) + cfg["body"] + FOOTER
    (ROOT / fname).write_text(html, encoding="utf-8")
    print("wrote", fname)
