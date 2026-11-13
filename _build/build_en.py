# -*- coding: utf-8 -*-
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lang_detect import lang_script
from radar import radar_svg
from sample_page import sample_report
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAND = 'Zubkov Bureau'
ROLE = 'Evidence-based AI bureau'
PLAT = 'Council 7+1'
SITE = 'https://example.ru'

NAV = [('method.html','Method'),('council.html',PLAT),('cases.html','Cases'),('industries.html','Industries'),
       ('formats.html','Formats'),('bureau.html','Bureau'),('insights.html','Insights')]

def nb(s):
    s = re.sub(r'([0-9+]) ', '\\1\u00a0', s)
    return re.sub(r'(млн|млрд|тыс)\.? ', lambda m: m.group(0)[:-1] + '\u00a0', s)

def photo(name, alt, cls='', gen=True):
    return f'<figure class="photo{" gen" if gen else ""} {cls}"><img src="{{a}}assets/img/{name}" alt="{alt}" loading="lazy" decoding="async"></figure>'

def chip(z):
    m={'AI':'green','Hybrid':'amber','No AI':'red','Defer':'grey'}
    return f'<span class="chip chip-{m[z]}">{z}</span>'

def page(sub, title, desc, body, active=None):
    path = 'en/' + sub
    depth = path.count('/')
    a = '../'*depth
    r = '../'*(depth-1)
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{r}{h}"{cur if h==active else ""}>{t}</a>' for h,t in NAV)
    fnav = ''.join(f'<a href="{r}{h}">{t}</a>' for h,t in NAV) + f'<a href="{r}contact.html">Contact</a><a href="{a}{sub}" hreflang="ru">RU</a>'
    canon = sub.replace('index.html','')
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}/en/{canon}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="{SITE}/assets/img/team.jpg">
  <link rel="alternate" hreflang="ru" href="{SITE}/{canon}">
  <link rel="alternate" hreflang="en" href="{SITE}/en/{canon}">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='8' fill='%231C1B18'/%3E%3Crect x='14' y='20' width='10' height='24' fill='%232E7D4F'/%3E%3Crect x='27' y='20' width='10' height='24' fill='%23A9740F'/%3E%3Crect x='40' y='20' width='10' height='24' fill='%23B3402E'/%3E%3C/svg%3E">
  {lang_script('en', f'{a}{sub}')}
  <link rel="stylesheet" href="{a}assets/css/style.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"ProfessionalService","name":"{BRAND} — {ROLE.lower()}","url":"{SITE}/en/",
   "description":"Process diagnostics that decide where AI is justified, profitable and safe, and where conventional automation is enough.",
   "founder":{{"@type":"Person","name":"Sergey Zubkov","jobTitle":"Founder, chief designer","sameAs":["https://www.linkedin.com/in/sergey-a-zubkov"]}},
   "areaServed":"RU","knowsAbout":["AI strategy","Process diagnostics","MLOps","Maritime logistics","Mining","ESG"]}}
  </script>
</head>
<body>
<header class="site-header" id="top">
  <div class="container header-inner">
    <a class="wordmark" href="{r}index.html" aria-label="{BRAND} — home">
      <span class="wordmark-mark" aria-hidden="true"><b>?</b><i></i><i></i><i></i><i></i></span>
      <span class="wordmark-text"><span class="wordmark-name">{BRAND}</span><span class="wordmark-role">{ROLE}</span></span>
    </a>
    <nav class="site-nav" id="site-nav" aria-label="Main navigation">
      {nav}
      <a class="nav-lang" href="{a}{sub}" hreflang="ru">RU</a>
      <a class="nav-cta" href="{r}contact.html">45-minute call</a>
    </nav>
    <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span></span><span></span></button>
  </div>
</header>
<main>
{body.replace('{a}', a).replace('{r}', r)}
</main>
<footer class="site-footer">
  <div class="container footer-inner">
    <p>© <span id="year">2026</span> {BRAND} · {ROLE.lower()} · Sergey Zubkov</p>
    <nav class="footer-nav" aria-label="Sitemap">{fnav}</nav>
    <p class="footer-note">Prototype: working names; photos are AI-generated and will be replaced. Nothing on this site constitutes a public offer.</p>
  </div>
</footer>
<a class="to-top" href="#top" aria-label="Back to top">↑</a>
<script src="{a}assets/js/main.js"></script>
</body>
</html>
'''
    html = html.replace('Изображение обработано ИИ', 'AI-processed image')
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html)

def hero(crumb, eyebrow, title, sub, extra=''):
    c = f'<p class="crumbs"><a href="{{r}}index.html">Home</a> / {crumb}</p>' if crumb else ''
    return f'''<section class="page-hero"><div class="container">{c}
  <p class="eyebrow reveal">{eyebrow}</p><h1 class="hero-title reveal">{title}</h1>
  <p class="hero-sub reveal">{sub}</p>{extra}</div></section>'''

def sec(id_, eyebrow, title, inner, muted=False, lead=''):
    l = f'<p class="section-lead reveal">{lead}</p>' if lead else ''
    return f'''<section class="section{' section-muted' if muted else ''}" id="{id_}"><div class="container">
  <p class="eyebrow reveal">{eyebrow}</p><h2 class="section-title reveal">{title}</h2>{l}
  {inner}</div></section>'''

CTA = '''<section class="cta-band"><div class="container">
  <h2 class="section-title">Start with a conversation, not a budget</h2>
  <p>45 minutes on your context and questions. You leave knowing how much diagnostics you actually need.</p>
  <div class="hero-cta"><a class="btn btn-primary" href="{r}contact.html">45-minute call</a>
  <a class="btn btn-ghost" href="{r}formats.html">Formats and pricing</a></div></div></section>'''

ZONES = '''<div class="zones">
  <article class="zone zone-green reveal"><p class="zone-tag">AI is justified</p><p class="zone-text">Unstructured data, variable patterns, scale, predictive value.</p><p class="zone-example">Oil-slick detection from drone imagery: 91% accuracy where the sea area used to be patrolled by vessel.</p></article>
  <article class="zone zone-amber reveal"><p class="zone-tag">Hybrid</p><p class="zone-text">AI for some subtasks; rules and people for critical decisions.</p><p class="zone-example">A developer's document flow: LLM in 3 of 8 subtasks, only where accuracy exceeds 95%.</p></article>
  <article class="zone zone-red reveal"><p class="zone-tag">No AI</p><p class="zone-text">Stable rules, low volume, zero tolerance for error, not enough data.</p><p class="zone-example">Warning a vessel approaching an ice zone is deterministic logic: route geometry and time thresholds.</p></article>
  <article class="zone zone-grey reveal"><p class="zone-tag">Defer</p><p class="zone-text">A sound idea, but too early: little data, processes not ready, or no owner.</p><p class="zone-example">First put data and procedures in order; return to AI when there is something to learn from and someone accountable.</p></article>
</div>'''

MATRIX = '''<div class="matrix-wrap reveal"><table class="matrix">
  <thead><tr><th scope="col">Process</th><th scope="col">Verdict</th><th scope="col">Status</th><th scope="col">Rationale</th><th scope="col">Effect / timeline</th></tr></thead>
  <tbody>
  <tr><td>Triage of incoming hull insurance applications</td><td>%s</td><td><span class="status status-ok">Pilot eligible</span></td><td>Unstructured documents, high volume, errors are correctable by a person</td><td>−40–60%% manual review · 3 mo.</td></tr>
  <tr><td>Premium calculation under underwriting rules</td><td>%s</td><td><span class="status status-ok">Pilot eligible</span></td><td>Rules are stable and regulated; full explainability required</td><td>Rules in code · 1 mo.</td></tr>
  <tr><td>Reconciling completion certificates with ERP</td><td>%s</td><td><span class="status status-wait">Eligible after prerequisites</span></td><td>LLM extracts fields, logic reconciles, disputed items go to a person</td><td>−30%% closing cycle · 2 mo.</td></tr>
  <tr><td>Seasonal fleet utilisation forecast</td><td>%s</td><td><span class="status status-gap">Insufficient evidence</span></td><td>Less than two years of history; collect data first</td><td>Revisit in 12 mo.</td></tr>
  </tbody></table></div>
<p class="section-note reveal">Demonstration example, not client data. Figures are illustrative: in a real assessment every estimate comes with a method and assumptions.</p>''' % (chip('AI'),chip('No AI'),chip('Hybrid'),chip('Defer'))

COUNCIL = '''<div class="council">
  <div class="council-lead reveal"><span class="council-num">+1</span><h3>Lead agent</h3><p>Clarifies the context until there is enough of it, briefs the expert roles, consolidates findings and dissenting views.</p></div>
  <div class="council-grid"><ol class="council-experts">
    <li class="reveal"><span class="council-num">1</span><h3>Process</h3><p>Where the real losses and bottlenecks are</p></li>
    <li class="reveal"><span class="council-num">2</span><h3>Technology</h3><p>What to use: AI, rules, integration</p></li>
    <li class="reveal"><span class="council-num">3</span><h3>Industry</h3><p>Practice and constraints of your sector</p><p class="council-human">+ human expert</p></li>
    <li class="reveal"><span class="council-num">4</span><h3>Finance</h3><p>Payback and total cost of ownership</p><p class="council-human">+ human expert</p></li>
    <li class="reveal"><span class="council-num">5</span><h3>Legal</h3><p>Contracts, data, liability</p><p class="council-human">+ human expert</p></li>
    <li class="reveal"><span class="council-num">6</span><h3>Compliance</h3><p>Data protection law, sector rules, closed environments</p></li>
    <li class="reveal"><span class="council-num">7</span><h3>AI security</h3><p>MLSecOps: attacks, leaks, autonomy limits</p></li>
  </ol><div class="council-sign reveal"><span class="council-num">= 1 decision</span><h3>Human signature</h3><p>The bureau's chief designer reviews the findings and signs the assessment.</p></div></div>
</div>'''

FUNCS = {'caio':'AI strategy and portfolio','caito':'Transformation toward AI',
         'impl':'Architecture and implementation','bsm':'Diagnostics and business case','ops':'Operations and AI-agent autonomy control'}
def funcs(*ks): return ' · '.join(FUNCS[k] for k in ks)

CASES = [
 dict(slug='vizard', img='arctic.jpg', tags='Maritime safety · Arctic and the Far East', card_tags='Maritime safety · Arctic & Far East', draft=False,
      title='+13% Northern Sea Route voyages and +14.5% speed in ice',
      short='A navigational-safety platform for oil and gas groups and the national shipping operator: ice conditions, routing, autonomy bounds.',
      facts=[('Functions', funcs('caio','ops')),('Deployment & stack','Safety runtime, 7 modules in production'),('Metric','<1% of agent actions outside permitted bounds'),('Markets & languages','Russia · China · Norway · Japan — Russian, Chinese, English')],
      task='The clients — oil and gas groups and the shipping operator — needed safer, more efficient ice navigation without losing control: every agent decision must stay within permitted bounds.',
      verdict=[('Ice conditions from satellite data','AI','Variable patterns, high image volume'),('Warning of approach to an ice zone','No AI','Errors are unacceptable: route geometry and time thresholds'),('Route recommendations','Hybrid','The model suggests, the captain decides')],
      result='−65% fishing-gear losses over 5+ years. Hard prohibitions live in the runtime; critical decisions keep a human in the loop.'),
 dict(slug='shipping', img='shipping.png', tags='Marine insurance and shipowners · international track', card_tags='Marine insurance and shipowners', draft=False, intl=True,
      title='>RUB 2 bn saved for shipowners and operators · 2025–2029',
      short='Meteo bulletins and insurance-cover control for insurers; fleet-anomaly detection for fishing shipowners. In-house development and deployment of the service in seven countries.',
      facts=[('Functions', funcs('bsm','ops')),('Markets & languages','Russia · China · MENA · Latin America · Japan — Russian, English, Chinese, Spanish'),('Data','AIS tracks + satellite imagery + anonymized telecom data'),('Metric','≈22% of voyages covered by the service · up to $9.7–16.6M/yr of prevented losses (estimate)')],
      task='Insurers needed control of fleet risk and insurance cover; fishing shipowners needed fleet control and prevention of illegal catch unloading.',
      verdict=[('Meteo and situational bulletins','AI','Multi-source data assembly, personalised per vessel and voyage'),('Insurance-cover control','No AI','Deterministic rules and thresholds — errors are unacceptable'),('Fleet-anomaly detection','Hybrid','The model flags AIS-vs-activity mismatches; conclusions go to the client after human review')],
      result='Clients received a working commercial module in production; for a Chinese shipowner, hidden catch overloading by individual vessels was uncovered in La Pérouse Strait.'),
 dict(slug='morspas', img='oil_spills.png', tags='Federal maritime rescue service · sea area monitoring', card_tags='Sea area monitoring', draft=False,
      title='−38% vessel-days for sea area monitoring',
      short='From continuous visual patrolling to targeted drone monitoring: ice conditions and oil pollution.',
      facts=[('Functions', funcs('impl','ops')),('Metric','91% accuracy · ≤10% false positives · natural look-alikes — 86%'),('Effect','monitoring costs down ~×1.7'),('Data','Drone aerial imagery: multispectral + IR, ≤5 s latency')],
      task='The client needed to cut expensive vessel patrols without losing completeness in detecting ice and oil pollution.',
      verdict=[('Slick detection from drone imagery','AI','Unstructured images, scale'),('Flight planning','No AI','Procedures and weather thresholds are rules'),('Incident confirmation','Hybrid','The model flags, the operator confirms')],
      result='Metrics verified on an independent sample. Drones added to the permanent MFACC toolset.'),
 dict(slug='geodesy', img='land_cadastre_remote.jpg', tags='Geodesy and cadastre · closed government environment', card_tags='Geodesy and cadastre · closed env.', draft=False, nda=True,
      title='+18% branch workload with reduced headcount',
      short='An agent that allocates and prioritises branch work in a closed government environment, with a governance standard on top.',
      facts=[('Functions', funcs('caio','impl')),('Deployment & stack','On-prem, no external SaaS · sovereign and national LLMs · Evaluation Framework'),('Roadmap','25 measures · 6 directions — from methodology and data through GeoAI to production adoption'),('Effect','30% fewer staff with higher efficiency')],
      task='Branch output had to be preserved while headcount shrank, under closed-environment requirements.',
      verdict=[('Branch workload planning','AI','Many non-formalised factors'),('Accounting and reporting','No AI','Rules and integration are enough'),('Allocating urgent requests','Hybrid','The agent proposes, the manager approves')],
      result='The agent was handed to the project team; on top of it — an autonomy boundary matrix, key risk indicators and an evaluation framework.'),
 dict(slug='developer', img='construction.jpg', tags='Real estate development · Moscow top-3', draft=False, nda=True,
      title='LLM in 3 of 8 subtasks — and that is the right call',
      short='An initiatives portfolio for a Moscow top-3 developer: where AI is justified and where plain rules suffice.',
      facts=[('Functions', funcs('caio','bsm')),('Roadmap','15 measures across the asset life cycle'),('Metric','LLM accuracy >95%'),('Effect','RUB 14M+/yr of manual work freed up — savings on routine operations')],
      task='The portfolio of initiatives across the project life cycle required sorting — without spending budget on what conventional automation solves.',
      verdict=[('Extracting fields from primary documents','AI','Unstructured documents'),('Reconciliation with ERP','No AI','Deterministic rules'),('Disputed discrepancies','Hybrid','A person decides')],
      result='A hybrid Excel → 1C:ERP agent: LLM only where it delivers measurable accuracy gains; the rest is deterministic logic and a human in the loop.'),
 dict(slug='egip', img='city.jpg', tags='Moscow unified geo-information space · urban policy', draft=False, card_tags='Moscow UGIS · urban policy',
      title='37 systems, 60+ agencies, ~RUB 1 bn programme',
      short='Moscow unified geo-information space: from fragmented agency data to a manageable system.',
      award='Best work at the 3rd International GIS-Forum',
      facts=[('Functions','Programme architecture and inter-agency integration'),('Data','1000+ data sets · 3D, LiDAR, stereo imagery, online telemetry'),('Processes','B2G · B2B · B2C: sector analytics, mobile inspections, citizen feedback'),('Effect','GIS support cost down ×6.3 · 800k+ residents in the feedback loop')],
      task='Fragmented data from dozens of agencies had to be consolidated into a single geo-information space for the city.',
      verdict=[('System integration','No AI','Standards and data buses are required, not models'),('Spatial data quality','Hybrid','Automated checks plus an expert'),('City analytics','Defer','Unified data first')],
      result='A unified space operating as a manageable system: standards, inter-agency integration, ML analysis of laser-scanning data.'),
 dict(slug='agro', img='agro.jpg', tags='Agriculture · geo-ML on aerial imagery', draft=False,
      title='From drone image to inspector case in 2 hours',
      short='ML detection of weed and quarantine plants for state oversight: from image to a ready case for the inspector.',
      facts=[('Functions', funcs('impl','ops')),('Metric','accuracy ≥85% at mAP ≥0.70 · MVP: 65 weed classes, 43.6 images/min'),('Data','Drones (RGB + multispectral) · tractor cameras · satellite · agronomist tablets'),('Effect','empty site visits down 40% · coverage ≥80% of target areas per season · detection classes ×3 · accuracy +9%')],
      task='The oversight authority required a verifiable picture of field conditions at industrial scale: replacing selective walkthroughs and manual image review with an auditable evidence base for enforcement orders.',
      verdict=[('Weed detection on imagery','AI','Variable patterns, large imagery volume'),('Survey routes and reporting','No AI','Rules and templates are enough'),('Field treatment decision','Hybrid','The model labels, the agronomist decides')],
      result='A computer-vision platform hands the inspector a ready case with a geo-referenced evidence base for enforcement orders.'),
 dict(slug='shelf', img='shelf.jpg', tags='Drilling and pumping equipment · reliability', card_tags='Drilling equipment · reliability', draft=False,
      title='+RUB 17.8 mln per semi-sub season · payback from ~13 h',
      short='An assessment of drilling rig processes: where AI is justified and where only deterministic automation belongs.',
      facts=[('Functions', funcs('caio','ops')),('Processes','15 drilling-work scenarios — from maintenance and supply to alerting and reporting'),('Roadmap','budget spread across seasons and technologies, payback from year one'),('Boundary','AI outside the critical-infrastructure perimeter · models on board · to shore — events only')],
      task='A shelf drilling operator needs to determine where AI delivers measurable value on the rigs and where it is barred by industrial safety and critical-infrastructure rules.',
      verdict=[('Predictive maintenance: mud pumps, drawworks, top drive','Hybrid','ML flags early degradation signs; OEM thresholds and the decision stay with the mechanic'),('Video analytics for hazardous zones, PPE control','AI','Impossible without computer vision; the response runs through certified systems, not directly from the model'),('ESD, BOP control, fire & gas, alerting','No AI','Compliance and security veto: provable, certifiable behaviour; AI acts only as a parallel adviser')],
      result='The launch order is set: the first maintenance pilot goes to semi-submersibles, where returns are positive already in the first season; jack-ups join at rollout. The verdict matrix contains a risk register under security and compliance vetoes.'),
 dict(slug='medtech', img='dental.jpg', tags='MedTech · dental visualisation', card_tags='MedTech · dentistry',
      title='First AI microscope for dentistry — an open niche',
      short='A three-wave program bringing AI into a digital dental microscope: from quick wins to the world’s first endodontic AI assistant.', card_short='An AI adoption program for a dental microscope: three feature waves toward an endodontic AI assistant.',
      facts=[('Functions', funcs('caio','ops')),('Architecture','AI on a separate module by the microscope; device software unchanged'),('Metric','canal orifice detection ~91% · MB2 sens 80–100% · cracks up to 97.8%'),('Effect','patient treatment acceptance +15–37% · clinic revenue grows')],
      task='A digital dental microscope manufacturer needs an AI adoption program that raises device value and sales — without changing the optics.',
      verdict=[('Image enhancement, voice control, auto-protocols','AI','Unstructured video and speech input; outside diagnostic claims — no medical-device registration needed'),('Real-time detection of canal orifices and cracks','Hybrid','The model highlights on a separate module beside the microscope, the doctor confirms; the device software stays unchanged'),('Autonomous diagnosis','Defer','The cost of error demands clinical validation first — the decision stays with the doctor')],
      result='A rollout sequence is defined: non-diagnostic features in 6–12 months, the clinical assistant after dataset collection and validation, then AR overlay and telementoring. The client receives a go-to-market strategy for the AI modules.'),
]

def case_card(c):
    ph = photo(c['img'], c['tags'])
    if c.get('award'):
        ph = ph.replace('</figure>', '<span class="award-star" data-tip="Award-winning case"><svg viewBox="0 0 24 24"><path d="M8 13l-2.5 8L12 18l6.5 3L16 13"/><circle cx="12" cy="9" r="6"/><path d="M12 6l1.1 2.2 2.4.3-1.8 1.7.5 2.4L12 11.5 9.8 12.6l.5-2.4-1.8-1.7 2.4-.3z"/></svg></span></figure>')
    if c.get('intl') == 'badge':
        ph = ph.replace('</figure>', '<span class="intl-badge" data-tip="International case"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.6 3 14.4 0 18M12 3c-3 3.6-3 14.4 0 18"/></svg></span></figure>')
    elif c.get('intl') == 'tag':
        ph = ph.replace('</figure>', '<span class="intl-tag">INTL</span></figure>')
    elif c.get('intl'):
        ph = ph.replace('</figure>', '<span class="ribbon-intl">International</span></figure>')
    return f'''<a class="card reveal" href="{{r}}cases/{c['slug']}.html">{ph}
  <p class="card-tags">{c.get('card_tags', c['tags'])}</p><h3>{c['title']}</h3><p>{c.get('card_short', c['short'])}</p><span class="more">Read the case →</span></a>'''

INDUSTRIES = [
 ('mining.jpg','Mining and hydrocarbons','Oil, gas and ores. Safety and logistics in harsh environments: offshore, ice, remoteness.','Typical: AI in video analytics and failure prediction; no AI in safety permits and procedures.'),
 ('city.jpg','Urban infrastructure','Inter-agency integration and city data: 60+ agencies, closed environments, public procurement rules.','Typical: unified data and integration first; AI in citizen requests and Earth observation analysis.'),
 ('construction.jpg','Construction and development','The whole project life cycle: surveys, design, construction, operation, sales.','Typical: hybrid in document flow; no AI in cost estimates and reconciliations.'),
 ('arctic.jpg','Maritime logistics and insurance','Fleet and risk: weather support, insurance coverage control, economics of rare but large events.','Typical: AI in ice conditions and application triage; no AI in premiums and warnings.'),
 ('agro.jpg','Agriculture','Geo-ML field monitoring: from aerial imagery to results for the inspector in 2 hours instead of 3 days.','Typical: AI in image detection (mAP@0.5 > 80%); defer where there is no yield history.'),
 ('esg.jpg','Environment and ESG','CO₂/CH₄ emissions monitoring, climate risks, nature-based solutions on Earth observation and AIS data.','Typical: hybrid — the model estimates, the methodology and auditor confirm.'),
]

FORMATS = [
 ('Step 1','Express screening','A short questionnaire and an initial map: where AI is worth considering and where it is definitely not. Online via '+PLAT+'.','free · coming soon'),
 ('Step 2','Diagnostics','Fixed scope: process audit, decision matrix, business case, roadmap. 2–4 weeks.','from RUB 500,000 per phase · revenue share possible'),
 ('Step 3','Fractional CAIO','A part-time external Chief AI Officer: strategy, governance, oversight of implementations. From 3 months.','from RUB 200,000/mo · one day a week from RUB 350,000/mo'),
 ('Step 4','Implementation','The bureau team builds what passed diagnostics. Production standard, on-prem where needed.','estimated after diagnostics'),
 ('Step 4 · or','Design supervision','Your developers or contractors implement; the bureau checks conformity with the assessment and architecture and accepts each phase.','based on implementation scope'),
]
def formats_html():
    return '<div class="formats formats-4 formats-5">' + ''.join(f'<div class="format reveal"><p class="format-step">{a}</p><h3 class="format-name">{b}</h3><p class="format-text">{c}</p><p class="format-price">{d}</p></div>' for a,b,c,d in FORMATS) + '</div>'

FAQ = [
 ('How much does it cost?','Diagnostics is a fixed price per scope. Implementation is estimated once the truly necessary scope is clear. If you do not need AI, you learn it during diagnostics, not at the end of the budget.'),
 ('What if you decide we do not need AI?','That is a normal and frequent outcome. You get a decision matrix and a roadmap for conventional automation and save budget on what you do not need. For the bureau it is as successful a project as an implementation.'),
 ('Do you work with closed environments?','Yes: on-prem MLOps, sovereign LLM stacks, personal data law compliance, isolated environments without external SaaS. Our key implementations are exactly there.'),
 ('Who does the work?',PLAT+' prepares the analysis. Legal, financial and industry findings are reviewed by invited experts: a lawyer, a finance specialist/economist and an industry specialist. Sergey Zubkov leads diagnostics and architecture and signs the assessment. The bureau\'s DS/ML engineers implement, with no anonymous subcontractors.'),
 ('Can we implement in-house or with another contractor?','Yes. Then the bureau provides design supervision: it checks that the solution matches the assessment and architecture, accepts phases and tracks metrics.'),
 ('How are you different from a systems integrator?','An integrator earns on implementation, so it is interested in implementing. The bureau earns on the assessment and is accountable for it, so it can honestly say “not needed”.'),
]
def faq_html(items):
    return '<div class="container-narrow" style="margin:0">' + ''.join(f'<details class="faq-item reveal"{" open" if i==0 else ""}><summary>{q}</summary><div class="faq-body"><p>{a}</p></div></details>' for i,(q,a) in enumerate(items)) + '</div>'

# ================= INDEX =================
index = f'''<section class="hero"><div class="container hero-grid">
  <div class="hero-copy">
    <p class="eyebrow reveal">{ROLE} · Diagnostics before deployment</p>
    <h1 class="hero-title reveal">We make businesses more resilient and&nbsp;manageable.<br><em>AI only where it truly belongs.</em></h1>
    <p class="hero-sub reveal">Every process gets one of four verdicts: AI, hybrid, conventional automation or “not yet”. Diagnostics and a signed assessment first, then work.</p>
    <div class="hero-cta reveal"><a class="btn btn-primary" href="{{r}}contact.html">45-minute call</a><a class="btn btn-ghost" href="{{r}}sample.html">Sample assessment</a></div>
    <p class="hero-meta reveal">Led by Sergey Zubkov, founder and chief designer · 20+ years in IT and data · RU / EN</p>
  </div>
  <figure class="verdict-card reveal" aria-label="Assessment excerpt: verdicts by process">
    <figcaption class="verdict-head"><span>Assessment · excerpt</span><span>7 / 7 checks</span></figcaption>
    <ul class="verdict-list">
      <li><span class="v-proc">Pollution detection from drone imagery</span>{chip('AI')}</li>
      <li><span class="v-proc">Primary documents Excel → ERP</span>{chip('Hybrid')}</li>
      <li><span class="v-proc">Ice zone warning</span>{chip('No AI')}</li>
      <li><span class="v-proc">Branch service demand forecast</span>{chip('Defer')}</li>
    </ul>
    <p class="verdict-foot">A person signs the decision · expert dissenting views are kept</p>
  </figure>
</div></section>
<section class="numbers" aria-label="Client results"><div class="container numbers-grid">
  <div class="number-item reveal"><div class="number-value">−38%</div><div class="number-caption">vessel-days for sea area monitoring: drones instead of patrols</div></div>
  <div class="number-item reveal"><div class="number-value">+18%</div><div class="number-caption">branch workload with 30% fewer staff, closed environment</div></div>
  <div class="number-item reveal"><div class="number-value">+13%</div><div class="number-caption">Northern Sea Route voyages with the platform's AI modules</div></div>
  <div class="number-item reveal"><div class="number-value accent">3&nbsp;of&nbsp;8</div><div class="number-caption">document-flow subtasks got an LLM. The rest do not need AI</div></div>
</div></section>
{sec('verdicts','Method · four verdicts','Everyone sells AI implementation.<br>We sell the decision on whether you need it.', ZONES + '<p class="section-note reveal"><a href="{r}method.html">How we decide →</a></p>')}
{sec('council', PLAT, 'The platform analyses. Experts review. The chief designer signs.', COUNCIL + '<p class="section-note reveal"><a href="{r}council.html">How the platform works →</a></p>', muted=True, lead='A lead agent gathers context and briefs seven expert AI roles. Legal, financial and industry findings are reviewed by invited human experts; Sergey Zubkov signs the assessment.')}
{sec('cases','Cases','Results backed by numbers, not promises', '<div class="card-grid">'+''.join(case_card(c) for c in CASES[:3])+'</div><p class="section-note reveal"><a href="{r}cases.html">All cases →</a></p>')}
{sec('industries','Industries','We work where we know the context from the inside', '<div class="card-grid">'+''.join(f'<a class="card reveal" href="{{r}}industries.html">{photo(i,n)}<h3>{n}</h3><p>{t}</p></a>' for i,n,t,_ in INDUSTRIES)+'</div>', muted=True)}
{sec('formats','Formats','From free screening to implementation, step by step', formats_html() + '<p class="section-note reveal"><a href="{r}formats.html">More on formats and pricing →</a></p>')}
<section class="section section-muted" id="bureau"><div class="container split">
  <div><p class="eyebrow reveal">Bureau</p><h2 class="section-title reveal">Like a design bureau: a chief designer, calculations, execution</h2>
  <div class="prose reveal"><p>Sergey Zubkov personally leads diagnostics and architecture and signs every assessment. {PLAT} prepares the analysis; legal, financial and industry findings are reviewed by invited experts. The bureau's engineering team implements — or your contractors do, under our design supervision.</p></div>
  <p class="reveal"><a class="btn btn-ghost" href="{{r}}bureau.html">About the bureau and team</a></p></div>
  {photo('team.jpg','The bureau team reviewing a decision matrix','photo-32 reveal')}
</div></section>
{CTA}'''
page('index.html', f'{BRAND} — {ROLE.lower()} · Sergey Zubkov', 'Process diagnostics before AI deployment: where AI is justified, where a hybrid fits, and where conventional automation is enough. Mining, maritime, cities, agriculture, ESG.', index)

# ================= METHOD =================
RESP = '<ul class="tick-list reveal">' + ''.join(f'<li><b>{a}</b> — {b}</li>' for a,b in [
 ('Assessment','the soundness of every verdict: technology, economics, law, industry'),
 ('Architecture','the target solution design and the limits of AI autonomy'),
 ('Numbers','the method and assumptions behind every effect estimate'),
 ('Design supervision','conformity of the implementation with the assessment — whether by our team or by external developers and contractors'),
 ('Governance','monitoring, KRIs and a human in the loop on critical decisions')]) + '</ul>'
crit = [('Strategic value','Goals and KPIs, expected benefits, total cost of ownership, funding, non-AI alternatives','Finance'),
        ('Process suitability','Variability, unstructured inputs, volume, exceptions, cost of error, process stability: AI or rules','Process'),
        ('Data readiness','Availability, quality, representativeness, provenance, rights and access, evaluation datasets','Technology'),
        ('Technology and integration','APIs, infrastructure, identity integration, hosting constraints, vendor dependencies','Technology'),
        ('People and change','Sponsor, process owner, acceptance, skills and training, workflow redesign, incentives','Process'),
        ('Governance, legal and compliance','Permitted purpose, data-use rights, privacy, sector rules, contracts and IP, accountability, auditability','Compliance + Legal'),
        ('Security and resilience','Threat model, sensitive-data exposure, injection, tool permissions, supply chain, incident response','AI security'),
        ('Operational assurance','Acceptance tests, evaluations, monitoring, escalation, rollback, ownership, change control, running costs','Technology')]
crit_html = '<div class="matrix-wrap reveal"><table class="matrix criteria"><thead><tr><th>Factor</th><th>What we assess</th><th>Analytical lead</th></tr></thead><tbody>' + ''.join(f'<tr><td>{i}. {a}</td><td>{b}</td><td><span class="factor-lead">{c}</span></td></tr>' for i,(a,b,c) in enumerate(crit,1)) + '</tbody></table></div><p class="section-note reveal">The factors describe your process, not how the platform is built: each factor has a lead role, and other roles contribute. The industry expert takes part in all eight. Legal, financial and industry findings are reviewed by human experts.</p>'
RADAR = radar_svg(['Value','Process','Data','Technology','People','Governance','Security','Operations'],
    [3,2,1,3,2,None,2,1], [3,3,3,2,2,3,3,2], 'not assessed', 'Demonstration readiness radar across eight factors')
SCORING = '<div class="split"><figure class="radar-fig reveal">' + RADAR + '<div class="radar-legend"><span class="lg-cur">current profile</span><span class="lg-req">required for a supervised pilot</span></div><figcaption>Demonstration example. Status: “insufficient evidence” — governance is not assessed; data and operations are below the required level.</figcaption></figure><div class="reveal"><ol class="scale">' + ''.join(f'<li><span class="scale-num">{n}</span><span>{t}</span></li>' for n,t in [
 ('0','Absent or unsuitable — and demonstrably so'),('1','Ad hoc, substantial gaps'),('2','Partially established, material gaps'),('3','Adequate for the stated deployment stage'),('4','Established, tested, monitored')]) + '</ol><ul class="tick-list">' + ''.join(f'<li><b>{a}</b> — {b}</li>' for a,b in [
 ('“Not assessed” is not zero','an evidence gap shows as a break in the radar line, not a dip to the centre'),
 ('No average score','a weak factor cannot be offset by a strong one; we do not compute radar area'),
 ('Targets depend on the stage','a human-supervised pilot and production use need different profiles'),
 ('Every score has evidence','sources, assumptions, confidence and evidence coverage — kept separate from the score'),
 ('A working rubric','the scale is calibrated on reference cases and versioned')]) + '</ul></div></div>'
def st(k):
    m={'ok':'Pilot eligible','wait':'Eligible after prerequisites','block':'Blocked','gap':'Insufficient evidence'}
    return f'<span class="status status-{k}">{m[k]}</span>'
DECISION = '<div class="split decision"><div class="reveal"><h3>Recommendation — what to use</h3><ul class="decision-list">' + ''.join(f'<li>{chip(c)}{t}</li>' for c,t in [
 ('AI','a model where rules cannot describe the task'),('Hybrid','AI for some subtasks; rules and people for critical decisions'),('No AI','deterministic automation: rules, integrations, reporting'),('Defer','data, procedures or a process owner come first')]) + '</ul></div><div class="reveal"><h3>Deployment status — can it go ahead now</h3><ul class="decision-list">' + ''.join(f'<li>{st(k)}{t}</li>' for k,t in [
 ('ok','sufficient evidence, no binding block, all prerequisites met — a human-supervised pilot can start'),('wait','close the prerequisites in the roadmap first'),('block','a verified legal, compliance or security block'),('gap','critical evidence gaps — more information is needed')]) + '</ul></div></div><div class="precedence reveal"><p><b>Order of checks.</b> A legal, compliance or security block means “blocked” regardless of scores. Otherwise, critical gaps mean “insufficient evidence”. Otherwise, unmet prerequisites mean “eligible after prerequisites”.</p><p>An “AI” recommendation is not permission to deploy. Pilot eligibility is not production approval: production needs its own required profile and sign-off.</p></div>'
steps = '<ol class="steps steps-5">' + ''.join(f'<li class="step reveal"><span class="step-num">{n}</span><h3 class="step-title">{t}</h3><p class="step-meta">{m}</p><p class="step-text">{d}</p></li>' for n,t,m,d in [
 ('01','Diagnostics','2–4 weeks','Processes, data, systems, maturity. Analysis from seven angles.'),
 ('02','Decision','Matrix by process','A verdict and deployment status for every process, with risks, assumptions, confidence and evidence coverage.'),
 ('03','Roadmap','≈1 week','Priorities by value and feasibility. First results in 6–8 weeks.'),
 ('04','Implementation','Production standard','Monitoring, KRIs, autonomy limits, a human in the loop on critical decisions.'),
 ('05','Design supervision','Throughout implementation','If your developers or contractors implement: we check conformity with the assessment, accept phases and track metrics.')]) + '</ol>'
deliver = '<h3 class="section-title" style="font-size:1.4rem;margin-top:48px">What the assessment contains</h3><div class="split deliver-levels"><div class="reveal"><h4 class="level-title">Baseline diagnostics</h4><p class="level-sub">From open data and your materials, without access to internal systems</p>' + '<ul class="tick-list">' + ''.join(f'<li><b>{a}</b> — {b}</li>' for a,b in [('Key findings', 'the decision on one page and urgent measures'), ('Scope and inputs', 'what the findings rest on; all figures are hypotheses'), ('Profile and maturity', 'what you already have, so nothing is rebuilt'), ('Information sufficiency', 'for every process: sufficient, partial, insufficient'), ('Decision matrix', 'recommendation, conditions and rationale for every subtask'), ('Key trade-offs', 'why the contested choices were made'), ('Target process', 'where AI works, where rules do, where a person decides'), ('Risk register', 'security, legal and compliance: basis, consequence, mitigation'), ('Roadmap options', 'A/B/C and when to choose each'), ('Effect model', 'formula and assumptions as a range'), ('Questions and dissent', 'what to clarify and where experts disagreed')]) + '</ul>' + '</div><div class="reveal"><h4 class="level-title">Extended diagnostics</h4><p class="level-sub">With access to data and people. Everything in the baseline, plus:</p>' + '<ul class="tick-list">' + ''.join(f'<li><b>{a}</b> — {b}</li>' for a,b in [('Readiness radar', 'eight factors: current and required profile; for broad audits, a heatmap'), ('Evidence table', 'score, sources, confidence and coverage for every factor'), ('Deployment status', 'for every process: pilot, prerequisites, blocked or insufficient evidence'), ('Environment architecture', 'data categorisation and infrastructure options with 3-year TCO'), ('Business case', 'on a measured baseline'), ('Implementation phases', 'transition criteria and continue / stop points'), ('Signature', 'the chief designer and the experts who reviewed the findings')]) + '</ul>' + '</div></div><p class="section-note reveal"><a class="btn btn-primary" href="{r}sample.html">Open a sample assessment →</a></p>'
method = hero('Method','Method · decision before deployment','First decide whether AI is needed. Then work.','We do not sell implementation. We issue a comprehensive expert assessment of every process — technological, economic, legal and industry-specific. And the bureau has the right to say “AI is not needed here”.') + \
 sec('verdicts','Four verdicts','A verdict for every process', ZONES) + \
 sec('criteria','Eight factors','Eight readiness factors — for each process separately', crit_html, muted=True) + \
 sec('scoring','Scoring','A 0–4 scale and a radar: current profile against the required one', SCORING) + \
 sec('decision','Decision','Recommendation and deployment status are two separate decisions', DECISION, muted=True) + \
 sec('process','Process','Diagnostics before deployment', steps) + \
 sec('sample','What you get','An assessment, not a presentation on AI possibilities', MATRIX + deliver, muted=True) + \
 sec('responsibility','Accountability','What the bureau is accountable for', RESP) + \
 sec('faq','FAQ','The method in brief', faq_html(FAQ[1:3]+FAQ[4:])) + CTA
page('method.html', f'Method — {BRAND}', 'Eight readiness factors, four verdicts, deployment status and the contents of the assessment: how the bureau decides where AI is needed and where conventional automation is enough.', method, 'method.html')

# ================= COUNCIL =================
flow = '<ol class="steps steps-5">' + ''.join(f'<li class="step reveal"><span class="step-num">{n}</span><h3 class="step-title">{t}</h3><p class="step-text">{d}</p></li>' for n,t,d in [
 ('01','Clarification','The lead agent asks questions until context completeness reaches the sufficiency threshold.'),
 ('02','Briefs','A deterministic orchestrator sends briefs to the seven expert roles. It is code, not another model.'),
 ('03','Cross-check','Findings of the AI roles are compared; contradictions are not smoothed over but recorded as dissenting views.'),
 ('04','Expert review','A lawyer, a finance specialist/economist and an industry expert review and complement the findings in their fields.'),
 ('05','Signature','The bureau\'s chief designer consolidates the assessment, signs it and is accountable for it.')]) + '</ol>'
security = '<div class="card-grid">' + ''.join(f'<div class="card reveal"><p class="card-tags">{a}</p><h3>{b}</h3><p>{c}</p></div>' for a,b,c in [
 ('Data','Your data stays yours','On-prem or a domestic cloud; client data is not used to train models.'),
 ('Limits','Agents do not make decisions','Each role works within its limits; the outcome requires a human signature.'),
 ('Audit','Every finding is traceable','Briefs, answers and sources are stored: you can see where each finding came from.')]) + '</div>'
inds = ''.join(f'<option>{n}</option>' for _,n,_,_ in INDUSTRIES)
screen = f'''<div class="split"><div class="prose reveal"><p>Express screening via {PLAT}: 15 minutes for the questionnaire, and you get an initial process map with verdicts. It is not an assessment but a reason to talk.</p>
<p class="draft-note">Form prototype · platform in development</p></div>
<form class="form reveal" action="#" onsubmit="return false">
 <label>Industry<select>{inds}</select></label>
 <label>Process you want checked<textarea placeholder="For example: triage of incoming hull insurance applications"></textarea></label>
 <button class="btn btn-primary" type="button" disabled>Coming soon: take the screening</button></form></div>'''
council = hero(PLAT, f'{PLAT} · AI diagnostics platform','The platform analyses. Experts review. The chief designer signs.','The platform makes analysis fast and thorough. Legal, financial and industry specifics are additionally reviewed by invited experts: a lawyer, a finance specialist/economist and an industry specialist. The bureau\'s chief designer signs the assessment.', photo('team.jpg','The bureau working on an assessment','photo-wide reveal')) + \
 sec('roles','Composition','A lead agent, seven expert roles and humans in the loop', COUNCIL + '<p class="section-note reveal">Why humans: the platform is evolving, and the market needs time to trust AI-native assessments. That is why in three roles the agents\' findings are reviewed by invited experts. As verified assessments accumulate, the agents\' share of the work grows, but the signature and accountability remain with the bureau.</p>') + \
 sec('flow','How it works','From the first question to the signature', flow, muted=True) + \
 sec('security','Security','Control built into the architecture', security) + \
 sec('screening','Coming soon','Free express screening', screen, muted=True) + CTA
page('council.html', f'{PLAT} — diagnostics platform · {BRAND}', 'AI diagnostics platform: a lead agent, seven expert roles, a deterministic orchestrator and a human signature.', council, 'council.html')

# ================= CASES =================
cases = hero('Cases','Cases','Where AI was needed — and where we did not use it','Every case follows the same structure: task → verdicts by process → result.') + \
 sec('list','All cases','Verified results', '<div class="card-grid">'+''.join(case_card(c) for c in CASES)+'</div>') + CTA
page('cases.html', f'Cases — {BRAND}', 'Bureau cases: maritime safety, sea area monitoring, closed government environment, development, Moscow geo-information space, agriculture, ESG, EdTech.', cases, 'cases.html')
for i,c in enumerate(CASES):
    nxt = CASES[(i+1)%len(CASES)]
    facts = '<dl class="facts reveal">' + ''.join(f'<div><dt>{a}</dt><dd>{nb(b)}</dd></div>' for a,b in c['facts']) + '</dl>'
    vt = '<div class="matrix-wrap reveal"><table class="matrix"><thead><tr><th>Process</th><th>Verdict</th><th>Rationale</th></tr></thead><tbody>' + ''.join(f'<tr><td>{a}</td><td>{chip(b)}</td><td>{d}</td></tr>' for a,b,d in c['verdict']) + '</tbody></table></div>'
    body = f'''<section class="page-hero"><div class="container"><p class="crumbs"><a href="{{r}}index.html">Home</a> / <a href="{{r}}cases.html">Cases</a></p>
  <p class="eyebrow reveal">{c['tags']}{' <span class="nda-tag">details under NDA</span>' if c.get('nda') else ''}{' <span class="nda-tag award-chip">' + c['award'] + '</span>' if c.get('award') else ''}</p><h1 class="hero-title reveal">{nb(c['title'])}</h1><p class="hero-sub reveal">{nb(c['short'])}</p>
  {photo(c['img'],c['tags'],'photo-wide reveal',c.get('gen',True)).replace('</figure>', f'<span class="award-tag">{c["award"]}</span></figure>') + f'<p class="award-cap">{c["award"]}</p>' if c.get('award') else photo(c['img'],c['tags'],'photo-wide reveal',c.get('gen',True))}{facts}</div></section>
<section class="section"><div class="container split split-fill">
  <div class="prose reveal"><div><p class="eyebrow">Task</p><p>{nb(c['task'])}</p></div>
  <div><p class="eyebrow">Result</p><p>{nb(c['result'])}</p>
  {'<p class="draft-note">Draft case write-up: details to be confirmed with the founder, NDA limits to be checked</p>' if c.get('draft', True) else ''}</div></div>
  <div><p class="eyebrow reveal">Verdicts by process</p>{vt}</div>
</div></section>
<section class="section section-muted"><div class="container"><p class="eyebrow">Next case</p><div class="card-grid card-grid-2">{case_card(nxt)}</div></div></section>
{CTA}'''
    page(f"cases/{c['slug']}.html", f"{c['title']} — {BRAND} case", c['short'], body, 'cases.html')

# ================= INDUSTRIES =================
ind = '<div class="card-grid">' + ''.join(f'<article class="card reveal">{photo(i,n)}<h3>{n}</h3><p>{t}</p><p class="card-tags" style="text-transform:none">{v}</p></article>' for i,n,t,v in INDUSTRIES) + '</div>'
nogo = '<aside class="no-go reveal"><p class="no-go-title">Where we do not go</p><p class="no-go-text">FinTech, iGaming and industries where we lack years of practice. Advising where you do not know the ground is dishonest: those industries have their own specialists.</p></aside>'
industries = hero('Industries','Industries','Six industries where we know the context from the inside','The industry expert is one of the seven diagnostic roles. So we only take industries where the bureau has its own practice.') + \
 sec('list','Industries','Where we work and which verdicts are most common', ind) + \
 sec('nogo','Boundaries','Honestly about what we do not do', nogo, muted=True) + CTA
page('industries.html', f'Industries — {BRAND}', 'Mining, urban infrastructure, development, maritime logistics and insurance, agriculture, environment and ESG.', industries, 'industries.html')

# ================= FORMATS =================
cmp_rows = [('Outcome','Initial map','Signed assessment','AI portfolio management','Working system','Implementation per assessment'),
            ('Timeline','15 minutes','2–4 weeks','from 3 months','per roadmap','throughout implementation'),
            ('Led by',PLAT,'Sergey Zubkov, platform, experts','Sergey Zubkov','Bureau team','Sergey Zubkov'),
            ('Price','free','from RUB 500,000','from RUB 200,000/mo','after diagnostics','based on implementation scope')]
cmp = '<div class="matrix-wrap reveal"><table class="matrix"><thead><tr><th></th>' + ''.join(f'<th>{f[1]}</th>' for f in FORMATS) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join(f'<td>{x}</td>' for x in row)+'</tr>' for row in cmp_rows) + '</tbody></table></div>'
formats = hero('Formats','Formats and pricing','Open pricing. Every step is a separate decision.','You can stop after any step. If diagnostics shows AI is not needed, there will be no implementation.') + \
 sec('ladder','Ladder','Four steps and design supervision', formats_html()) + \
 sec('compare','Comparison','What each format includes', cmp, muted=True) + \
 sec('faq','FAQ','On money and boundaries', faq_html([FAQ[0],FAQ[1],FAQ[3],FAQ[4]])) + CTA
page('formats.html', f'Formats and pricing — {BRAND}', 'Express screening, diagnostics from RUB 500,000, Fractional CAIO from RUB 200,000/mo, implementation after diagnostics, design supervision.', formats, 'formats.html')

# ================= BUREAU =================
principles = '<ul class="tick-list reveal">' + ''.join(f'<li><b>{a}</b> — {b}</li>' for a,b in [
 ('The right to say “no”','a “no AI” verdict is as valid an outcome as an implementation'),('Signature','every assessment has an accountable person'),
 ('No subcontracting','our own team implements, no anonymous contractors'),('Only familiar industries','we do not advise where we have no practice'),
 ('Verifiable numbers','every metric has a method and assumptions'),
 ('Design supervision','we stay accountable for the result even when your contractors implement')]) + '</ul>'
pubs = '<ul class="pubs"><li class="pub reveal"><span class="pub-year">2020</span><span class="pub-title">A method for ice reconnaissance using drones</span><span class="pub-meta">NGN journal, No. 9/2020, pp. 21–26 · sole author</span></li><li class="pub reveal"><span class="pub-year">2025</span><span class="pub-title">Nature-based solutions in the Russian Arctic</span><span class="pub-meta">Sustainability (MDPI), 17, 10409 · consulting contribution</span></li></ul>'
bureau = hero('Bureau','Bureau','Like a design bureau: a chief designer, calculations, execution','A compact senior team with its own method. We are not intermediaries between you and contractors: we diagnose the processes ourselves, design the solution and are accountable for the outcome — from the assessment to acceptance of the implementation.') + \
 f'''<section class="section" id="founder"><div class="container split-rev split">
  {photo('founder.jpg','Sergey Zubkov, founder of the bureau','photo-34 reveal', gen=False)}
  <div class="prose reveal"><p class="eyebrow">Founder · chief designer</p><h2 class="section-title">Sergey Zubkov</h2>
  <p>Personally leads diagnostics, architecture and governance and signs every assessment. 20+ years in IT and data, 8+ years in AI projects, 3 AI products on the market.</p>
  <p>Keeps hands-on skills: designs and writes code himself with Cursor + Devin + GitHub.</p>
  <p><a href="https://www.linkedin.com/in/sergey-a-zubkov" target="_blank" rel="noopener">LinkedIn →</a></p></div>
 </div></section>''' + \
 sec('team','Team','Engineers who implement what passed diagnostics', f'<div class="split"><div class="prose reveal"><p>4–5 DS/ML engineers and developers: ML and computer vision, geo-ML, sovereign LLM environments, on-prem MLOps.</p><p>{PLAT}, the bureau\'s platform with a lead agent and seven expert roles, prepares the analysis.</p><p><b>Invited experts.</b> A lawyer, a finance specialist/economist and industry specialists review the platform\'s findings in their fields.</p></div>{photo("team.jpg","The bureau team","photo-32 reveal")}</div>', muted=True) + \
 sec('principles','Principles','Six rules of the bureau', principles) + \
 sec('responsibility','Accountability','What we are accountable for', RESP, muted=True) + \
 sec('pubs','Publications','Peer-reviewed means verifiable', pubs) + CTA
page('bureau.html', f'About the bureau — {BRAND}', 'Founder Sergey Zubkov, engineering team, invited experts, the Council 7+1 platform and the bureau\'s principles.', bureau, 'bureau.html')

# ================= INSIGHTS =================
notes = [('Case study','Why the core of ice warnings works without a neural network','Where the cost of error decides the technology.'),
         ('Method','Eight factors of AI readiness','A checklist for the CEO.'),
         ('Industry','AI in marine insurance: what to automate and what not to','Application triage, premiums, claims.'),
         ('Case study','“3 of 8”: how we dropped LLM in five subtasks','A developer case.'),
         ('Architecture','A deterministic orchestrator instead of yet another agent','How '+PLAT+' is built.'),
         ('Governance','Agent autonomy limits in production','Evaluation Framework and KRIs.')]
notes_html = '<div class="card-grid">' + ''.join(f'<article class="card reveal"><p class="card-tags">{a} · coming soon</p><h3>{b}</h3><p>{c}</p></article>' for a,b,c in notes) + '</div>'
lead = '<div class="split"><div class="prose reveal"><p>An annual review: where AI paid off in our industries, where it did not, and why. No marketing, with the method.</p><p class="draft-note">Lead magnet · in preparation</p></div><form class="form reveal" action="#" onsubmit="return false"><label>Email<input type="email" placeholder="you@company.com"></label><button class="btn btn-primary" type="button" disabled>Coming soon: get the report</button></form></div>'
insights = hero('Insights','Insights','Decision breakdowns: where AI is needed and where it is not','The same columns appear on the founder\'s and the bureau\'s LinkedIn.') + \
 sec('notes','Columns','Upcoming publications', notes_html) + \
 sec('report','Report','“Evidence-based AI” — annual review', lead, muted=True) + \
 sec('pubs','Publications','Peer-reviewed papers', pubs) + CTA
page('insights.html', f'Insights — {BRAND}', 'Decision breakdowns: where AI is needed and where it is not. Columns, annual review and peer-reviewed publications.', insights, 'insights.html')

# ================= SAMPLE =================
page('sample.html', f'Sample assessment — {BRAND}', 'A baseline diagnostic on synthetic data: findings, information sufficiency, a decision matrix with conditions. The full version in exchange for a work email.', hero('Sample assessment','Sample assessment','What a bureau assessment looks like','Baseline diagnostics on synthetic data: a fictional energy-sector design institute. The first four sections are open; the full report is yours in exchange for a work email.') + sample_report('en', chip) + CTA)

# ================= CONTACT =================
contact = hero('Contact','Contact','Start with a conversation, not a budget','45 minutes: your context, your questions, and a clear view of how much diagnostics you actually need. No presentations “about the possibilities of AI”.') + \
 f'''<section class="section"><div class="container split">
 <div><div class="contact-links reveal">
  <a class="contact-link" href="mailto:zubkovfpk@gmail.com"><span class="contact-label">Email</span><span class="contact-value">zubkovfpk@gmail.com</span></a>
  <a class="contact-link" href="https://t.me/SergeyAZubkov" target="_blank" rel="noopener"><span class="contact-label">Telegram</span><span class="contact-value">@SergeyAZubkov</span></a>
  <a class="contact-link" href="https://www.linkedin.com/in/sergey-a-zubkov" target="_blank" rel="noopener"><span class="contact-label">LinkedIn</span><span class="contact-value">sergey-a-zubkov</span></a></div>
  <p class="contact-note reveal">Sergey replies personally. Correspondence is not shared with third parties or used for mailings.</p></div>
 <form class="form reveal" action="mailto:zubkovfpk@gmail.com" method="post" enctype="text/plain">
  <label>Name<input name="name" required></label>
  <label>Company and role<input name="company"></label>
  <label>Industry<select name="industry">{inds}<option>Other</option></select></label>
  <label>What would you like to discuss<textarea name="message"></textarea></label>
  <button class="btn btn-primary" type="submit">Send</button>
  <p class="contact-note">Prototype: the form opens your email client. In production it will submit to a server.</p>
 </form></div></section>'''
page('contact.html', f'Contact — {BRAND}', 'A 45-minute call with Sergey Zubkov: context, questions and the scope of diagnostics you need.', contact, 'contact.html')

page('404.html', f'Page not found — {BRAND}', 'Page not found.', hero('','404','No such page. Verdict: “defer”.','<a href="{r}index.html">Back to home →</a>'))
print('built EN', 11 + len(CASES), 'pages')
