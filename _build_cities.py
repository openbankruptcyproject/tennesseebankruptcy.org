#!/usr/bin/env python3
"""Build Tennessee city subpaths for tennesseebankruptcy.org"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "tennesseebankruptcy.org"
GA4 = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-CSBPNV4NKL"></script>\n<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag(\'js\',new Date());gtag(\'config\',\'G-CSBPNV4NKL\');gtag(\'config\',\'G-053Z64N82F\');gtag(\'config\',\'G-FTWLM223G7\');</script>'
BTN_NAV = '{"@context":"https://schema.org","@graph":[{"@type":"SiteNavigationElement","name":"BTN Network","url":["https://1328f.com","https://1328f.org","https://automaticstay.org","https://341meeting.org","https://523a.org","https://109g.org","https://727a8.com","https://meanstest.org","https://chapter7vs13.org","https://howtofilebankruptcy.org"]}]}'

STYLE = """<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0d1117;color:#c9d1d9;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;line-height:1.6}
a{color:#58a6ff;text-decoration:none}a:hover{text-decoration:underline}
.container{max-width:1100px;margin:0 auto;padding:0 20px}
nav{background:#161b22;border-bottom:1px solid #30363d;padding:12px 0;position:sticky;top:0;z-index:100}
nav .container{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
nav .brand{color:#f0f6fc;font-weight:700;font-size:1.1rem}
nav .links{display:flex;gap:16px;flex-wrap:wrap}
nav .links a{color:#8b949e;font-size:0.9rem}nav .links a:hover{color:#58a6ff}
.hero{padding:60px 0 40px;text-align:center;border-bottom:1px solid #30363d}
.hero h1{color:#f0f6fc;font-size:2.4rem;margin-bottom:12px}
.hero .subtitle{color:#8b949e;font-size:1.15rem;max-width:700px;margin:0 auto 24px}
.hero .alert{background:#f8514920;border:1px solid #f85149;border-radius:8px;padding:16px 24px;display:inline-block;color:#f85149;font-weight:600;font-size:1.05rem}
.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;padding:32px 0}
.stat-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;text-align:center}
.stat-card .number{color:#58a6ff;font-size:2.2rem;font-weight:700}
.stat-card .label{color:#8b949e;font-size:0.9rem;margin-top:4px}
.stat-card.danger .number{color:#f85149}
section{padding:40px 0;border-bottom:1px solid #21262d}
h2{color:#f0f6fc;font-size:1.8rem;margin-bottom:16px}
h3{color:#f0f6fc;font-size:1.3rem;margin-bottom:12px}
p{margin-bottom:16px}
.card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;margin-bottom:20px}
.faq-item{background:#161b22;border:1px solid #30363d;border-radius:8px;margin-bottom:12px;overflow:hidden}
.faq-item summary{padding:16px 20px;cursor:pointer;color:#f0f6fc;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faq-item summary::after{content:"+";color:#58a6ff;font-size:1.3rem;font-weight:700}
.faq-item[open] summary::after{content:"-"}
.faq-item .answer{padding:0 20px 16px;color:#c9d1d9}
.network{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;margin:32px 0}
.network h3{margin-bottom:12px}
.network-links{display:flex;flex-wrap:wrap;gap:8px}
.network-links a{background:#21262d;padding:6px 14px;border-radius:16px;font-size:0.85rem;border:1px solid #30363d}
.network-links a:hover{border-color:#58a6ff;background:#161b22}
footer{background:#161b22;border-top:1px solid #30363d;padding:32px 0;text-align:center;color:#8b949e;font-size:0.85rem}
footer a{color:#58a6ff}footer p{margin-bottom:8px}
.cta{display:inline-block;background:#238636;color:#fff;padding:12px 28px;border-radius:6px;font-weight:600;margin-top:12px;font-size:1rem}
.cta:hover{background:#2ea043;text-decoration:none}
ul,ol{margin:12px 0 12px 24px}li{margin-bottom:6px}
table{width:100%;border-collapse:collapse;margin:16px 0}
th,td{padding:10px 14px;text-align:left;border-bottom:1px solid #30363d}
th{color:#f0f6fc;background:#161b22;font-weight:600}
td{color:#c9d1d9}
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:20px 0}
.compare-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:20px}
.compare-card h3{font-size:1.1rem;margin-bottom:10px}
.district-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px}
.district-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:20px}
.district-card h3{margin-bottom:8px;font-size:1.15rem}
.district-card .rate{font-size:1.8rem;font-weight:700;color:#f85149}
.district-card .meta{color:#8b949e;font-size:0.85rem;margin-top:8px}
.quick-answer{background:#238636;border-radius:8px;padding:20px 24px;margin:24px 0;color:#fff;font-size:1.1rem;font-weight:600}
.disclaimer{background:#f8514920;border:1px solid #f85149;border-radius:8px;padding:16px 24px;margin:24px 0;color:#f85149;font-size:0.9rem}
.step-number{display:inline-block;background:#238636;color:#fff;width:32px;height:32px;border-radius:50%;text-align:center;line-height:32px;font-weight:700;margin-right:10px;font-size:0.95rem}
.step{margin-bottom:24px}
.city-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin:20px 0}
.city-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:24px;text-align:center}
.city-card h3{margin-bottom:8px}
.city-card .pop{color:#58a6ff;font-size:1.4rem;font-weight:700}
@media(max-width:768px){.hero h1{font-size:1.7rem}.stats-row{grid-template-columns:1fr 1fr}.stat-card .number{font-size:1.6rem}.compare-grid{grid-template-columns:1fr}}
@media(max-width:480px){.stats-row{grid-template-columns:1fr}}
</style>"""

FOOTER = """<footer><div class="container">
<p>An <a href="https://openbankruptcyproject.org">Open Bankruptcy Project</a> resource</p>
<p>Data sourced from the Federal Judicial Center Integrated Database (2008--2024).</p>
<p>This site provides general information, not legal advice. Consult a qualified attorney for your specific situation.</p>
<p>&copy; 2026 Open Bankruptcy Project. <a href="https://github.com/openbankruptcyproject">GitHub</a></p>
</div></footer>
<script src="/btn-engage.js"></script>"""

OBP_NETWORK = """<div class="network">
<h3>Open Bankruptcy Project Network</h3>
<div class="network-links">
<a href="https://openbankruptcyproject.org">OBP Home</a>
<a href="https://1328f.com">1328(f) Screener</a>
<a href="https://chapter7vs13.org">Ch. 7 vs 13</a>
<a href="https://automaticstay.org">Automatic Stay</a>
<a href="https://341meeting.org">341 Meeting</a>
<a href="https://bankruptcymeanstest.org">Means Test</a>
<a href="https://howmuchdoesbankruptcycost.com">Cost Guide</a>
<a href="https://bankruptcydismissed.com">Dismissed?</a>
<a href="https://filebankruptcyagain.com">File Again?</a>
<a href="https://howtofilebankruptcy.org">How to File</a>
</div>
</div>"""

CTA_SECTION = """<div style="text-align:center;padding:40px 0">
<h2>Check Your Eligibility</h2>
<p>Use the free 1328(f) screener to check whether a prior discharge affects your eligibility for a new discharge.</p>
<a href="https://1328f.com" class="cta">Free Discharge Screener</a>
</div>"""

DISCLAIMER = '<div class="disclaimer">This site provides general educational information about bankruptcy law, not legal advice. Every situation is different. Consult with a qualified bankruptcy attorney licensed in Tennessee before making any decisions about filing.</div>'

def nav(city_slug):
    return f'''<nav><div class="container"><a href="/" class="brand">Tennessee Bankruptcy Guide</a><div class="links"><a href="/{city_slug}/">Home</a><a href="/{city_slug}/chapter-7.html">Ch. 7</a><a href="/{city_slug}/chapter-13.html">Ch. 13</a><a href="/{city_slug}/exemptions.html">Exemptions</a><a href="/{city_slug}/faq.html">FAQ</a><a href="/memphis/">Memphis</a><a href="/nashville/">Nashville</a><a href="/knoxville/">Knoxville</a><a href="/chattanooga/">Chattanooga</a><a href="https://openbankruptcyproject.org">OBP</a></div></div></nav>'''

def faq_schema(pairs):
    items = ','.join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}' for q,a in pairs)
    return f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}'

def article_schema(title, desc, url, crumbs):
    bc = ','.join(f'{{"@type":"ListItem","position":{i+1},"name":"{n}","item":"{u}"}}' for i,(n,u) in enumerate(crumbs))
    return f'{{"@context":"https://schema.org","@graph":[{{"@type":"Article","headline":"{title}","description":"{desc}","author":{{"@type":"Organization","name":"Open Bankruptcy Project"}},"publisher":{{"@type":"Organization","name":"Open Bankruptcy Project","url":"https://1328f.org"}},"datePublished":"2026-04-05","dateModified":"2026-04-05","mainEntityOfPage":"{url}"}},{{"@type":"BreadcrumbList","itemListElement":[{bc}]}},{{"@type":"WebPage","name":"{title}","url":"{url}","speakable":{{"@type":"SpeakableSpecification","cssSelector":[".quick-answer","h1",".summary","p:first-of-type"]}}}}]}}'

def head(title, desc, url, faq_pairs, crumbs):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{url}">
{GA4}
<script type="application/ld+json">{faq_schema(faq_pairs)}</script>
<script type="application/ld+json">{article_schema(title.split(" | ")[0], desc, url, crumbs)}</script>
<script type="application/ld+json">{BTN_NAV}</script>
{STYLE}
</head>'''

def write_page(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  wrote {path}")

def exemption_table():
    return """<table>
<tr><th>Property</th><th>Tennessee Exemption</th><th>Federal Alternative</th></tr>
<tr><td>Homestead</td><td>$5,000 individual / $7,500 family</td><td>$27,900</td></tr>
<tr><td>Vehicle</td><td>$10,000 (wildcard)</td><td>$4,450</td></tr>
<tr><td>Household goods</td><td>$4,000 total</td><td>$700 per item / $14,875 total</td></tr>
<tr><td>Wildcard</td><td>$10,000</td><td>$1,475 + up to $13,950 unused homestead</td></tr>
<tr><td>Retirement (IRA/401k)</td><td>Fully exempt</td><td>Fully exempt</td></tr>
<tr><td>Social Security</td><td>Fully exempt</td><td>Fully exempt</td></tr>
</table>"""

# =============================================================================
# MEMPHIS (15 pages + 8 suburbs)
# =============================================================================
city = "memphis"
CITY = "Memphis"
district = "W.D. Tenn."
courthouse = "200 Jefferson Ave, Suite 413, Memphis, TN 38103"
phone = "(901) 328-3500"
court_url = "tnwb.uscourts.gov"
legal_aid = "Memphis Area Legal Services"
legal_aid_phone = "(901) 523-8822"

memphis_suburb_links = """<div class="card">
<h3>Memphis Suburb Guides</h3>
<p>Find bankruptcy information for your community in the Memphis metro area:</p>
<div class="network-links" style="margin-top:8px">
<a href="/memphis/suburbs/germantown.html">Germantown</a>
<a href="/memphis/suburbs/collierville.html">Collierville</a>
<a href="/memphis/suburbs/bartlett.html">Bartlett</a>
<a href="/memphis/suburbs/southaven-ms.html">Southaven, MS</a>
<a href="/memphis/suburbs/olive-branch-ms.html">Olive Branch, MS</a>
<a href="/memphis/suburbs/lakeland.html">Lakeland</a>
<a href="/memphis/suburbs/arlington.html">Arlington</a>
<a href="/memphis/suburbs/millington.html">Millington</a>
</div>
</div>"""

# Memphis index
write_page("memphis/index.html", f"""{head(
    "Bankruptcy in Memphis, Tennessee -- Complete Guide | Tennessee Bankruptcy Guide",
    "Free 2026 guide to filing bankruptcy in Memphis, TN. Covers Chapter 7, Chapter 13, W.D. Tenn. courthouse, Tennessee exemptions, costs, and Memphis suburb guides.",
    f"https://{DOMAIN}/memphis/",
    [("How much does bankruptcy cost in Memphis?","Chapter 7 filing fees are $338 and Chapter 13 filing fees are $313. Attorney fees in Memphis typically range from $900-$1,800 for Chapter 7 and $2,500-$4,000 for Chapter 13."),
     ("Will I lose my house filing bankruptcy in Memphis?","Tennessee offers a $5,000/$7,500 homestead exemption under state law, but Memphis filers can choose federal exemptions ($27,900 homestead) instead -- which is often a better deal."),
     ("Where do Memphis residents file for bankruptcy?","Western District of Tennessee at 200 Jefferson Ave, Suite 413, Memphis, TN 38103."),
     ("What is the dismissal rate in Western Tennessee?","W.D. Tenn. has a 79.6% Chapter 13 dismissal rate -- the worst in the nation. More than 3 out of 4 Chapter 13 cases filed in Memphis end in dismissal rather than discharge.")],
    [("Home",f"https://{DOMAIN}"),("Memphis",f"https://{DOMAIN}/memphis/")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Bankruptcy in Memphis, Tennessee</h1>
<p class="subtitle">Memphis residents file in the Western District of Tennessee. With a staggering 79.6% Chapter 13 dismissal rate -- the worst in the nation -- and a 53.5% prior filer rate, understanding your options before filing is critical.</p>
<div class="alert">W.D. Tenn. Chapter 13 Dismissal Rate: 79.6% -- Worst in the U.S.</div>
<div style="margin-top:20px">
<a href="/memphis/faq.html" class="cta" style="margin-right:12px">Read the FAQ</a>
<a href="https://1328f.com" class="cta" style="background:#1f6feb">Check Your Eligibility</a>
</div>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card danger"><div class="number">79.6%</div><div class="label">Ch. 13 Dismissal Rate</div></div>
<div class="stat-card danger"><div class="number">53.5%</div><div class="label">Prior Filer Rate</div></div>
<div class="stat-card"><div class="number">$5,000 / $7,500</div><div class="label">TN Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Chapter 7 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13: Which Is Right for You?</h2>
<div class="compare-grid">
<div class="compare-card">
<h3>Chapter 7 -- Fresh Start</h3>
<p>Chapter 7 eliminates most unsecured debts (credit cards, medical bills, personal loans) in about 3-4 months. You must pass a <a href="https://bankruptcymeanstest.org">means test</a> based on your income.</p>
<ul>
<li>Discharge in 3-4 months</li>
<li>Eliminates credit cards, medical debt</li>
<li>Must pass the <a href="https://meanstest.org">means test</a></li>
<li>May lose non-exempt property</li>
<li>Filing fee: $338</li>
</ul>
<a href="/memphis/chapter-7.html">Learn more about Chapter 7 &rarr;</a>
</div>
<div class="compare-card">
<h3>Chapter 13 -- Payment Plan</h3>
<p>Chapter 13 lets you keep your property while repaying debts over 3-5 years. Good for saving a home from foreclosure or a car from repossession.</p>
<ul>
<li>3-5 year <a href="https://chapter13plan.org">repayment plan</a></li>
<li>Keep your home and car</li>
<li>Catch up on missed payments</li>
<li>No means test requirement</li>
<li>Filing fee: $313</li>
</ul>
<a href="/memphis/chapter-13.html">Learn more about Chapter 13 &rarr;</a>
</div>
</div>
<div class="disclaimer">Warning: W.D. Tenn. has the highest Chapter 13 dismissal rate in the nation at 79.6%. More than 3 out of 4 Chapter 13 cases here end in dismissal. Consider Chapter 7 if you qualify, or research local attorney success rates carefully before filing Chapter 13.</div>
<p style="color:#8b949e;font-size:0.9rem;margin-top:8px">Not sure which chapter fits? <a href="https://chapter7vs13.org">Compare them in detail</a>.</p>
</div></section>

<section><div class="container">
<h2>Memphis Courthouse</h2>
<div class="card">
<h3>Western District of Tennessee -- Memphis Division</h3>
<p>Courthouse: {courthouse}</p>
<p>Phone: {phone} | <a href="https://www.{court_url}" target="_blank" rel="noopener">{court_url}</a></p>
<p>All bankruptcy filings for Memphis and western Tennessee residents are handled here. Tennessee uses a non-judicial foreclosure process, meaning your home can be foreclosed without a court proceeding -- which makes the <a href="https://automaticstay.org">automatic stay</a> especially important.</p>
</div>
</div></section>

<section><div class="container">
<h2>Tennessee Exemptions at a Glance</h2>
<div class="card">
<p>Tennessee filers can choose between state and federal exemptions. For Memphis homeowners with significant equity, <strong>federal exemptions are often the better choice</strong> because the federal homestead exemption ($27,900) far exceeds Tennessee's ($5,000/$7,500).</p>
{exemption_table()}
<p style="margin-top:12px"><a href="/memphis/exemptions.html">Full exemption details &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>How Much Does Bankruptcy Cost in Memphis?</h2>
<div class="card">
<ul>
<li><strong>Chapter 7 filing fee:</strong> $338 (can request installment payments)</li>
<li><strong>Chapter 13 filing fee:</strong> $313 (can be paid through your plan)</li>
<li><strong>Attorney fees:</strong> Typically $900-$1,800 for Chapter 7; $2,500-$4,000 for Chapter 13</li>
<li><strong>Credit counseling:</strong> $15-25 per course (two required)</li>
</ul>
<p>Fee waivers are available for Chapter 7 filers whose income is below 150% of the federal poverty guidelines.</p>
<a href="/memphis/cost.html">Full cost breakdown &rarr;</a> | <a href="https://howmuchdoesbankruptcycost.com">National cost guide</a>
</div>
</div></section>

<section><div class="container">
<h2>Free Legal Resources in Memphis</h2>
<div class="card">
<h3>{legal_aid}</h3>
<p>Phone: {legal_aid_phone} | Provides free legal assistance to low-income Memphis residents, including bankruptcy guidance.</p>
<p>Tennessee also has a <a href="https://www.tba.org/index.cfm/resources/find-an-attorney/">Lawyer Referral Service</a> through the Tennessee Bar Association.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How much does bankruptcy cost in Memphis?</summary><div class="answer"><p>Chapter 7 filing fees are $338 and Chapter 13 filing fees are $313. Attorney fees typically range from $900-$1,800 for Chapter 7 and $2,500-$4,000 for Chapter 13. <a href="/memphis/cost.html">Full cost breakdown</a>.</p></div></details>
<details class="faq-item"><summary>Will I lose my house filing bankruptcy in Memphis?</summary><div class="answer"><p>Tennessee's homestead exemption is $5,000/$7,500, but you can choose federal exemptions ($27,900 homestead) instead. In Chapter 13, you can keep your home while catching up on payments. <a href="/memphis/keep-your-house.html">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>Why is the dismissal rate so high in Memphis?</summary><div class="answer"><p>W.D. Tenn. has a 79.6% Chapter 13 dismissal rate -- the worst nationally. Contributing factors include high poverty rates, aggressive filing practices, and the 53.5% prior-filer rate suggesting many people are filing repeatedly without success.</p></div></details>
<details class="faq-item"><summary>Where do I file for bankruptcy in Memphis?</summary><div class="answer"><p>Memphis residents file in the Western District of Tennessee at {courthouse}. Phone: {phone}.</p></div></details>
<p style="margin-top:16px"><a href="/memphis/faq.html">See all frequently asked questions &rarr;</a></p>
</div></section>

<div class="container">
{CTA_SECTION}
{memphis_suburb_links}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Memphis chapter-7
write_page("memphis/chapter-7.html", f"""{head(
    "Chapter 7 Bankruptcy in Memphis -- Eligibility, Exemptions, Timeline | Tennessee Bankruptcy Guide",
    "Complete guide to filing Chapter 7 bankruptcy in Memphis, TN. Covers W.D. Tenn. means test, Tennessee exemptions, timeline, and what to expect.",
    f"https://{DOMAIN}/memphis/chapter-7.html",
    [("What debts does Chapter 7 eliminate?","Chapter 7 discharges most unsecured debts including credit cards, medical bills, personal loans, and old utility bills. It does not discharge student loans (usually), recent taxes, child support, alimony, or debts from fraud."),
     ("What is the means test for Chapter 7 in Tennessee?","The means test compares your household income to the Tennessee median. If below, you qualify automatically. If above, a detailed expense calculation determines eligibility."),
     ("How long does Chapter 7 take in Memphis?","From filing to discharge, Chapter 7 typically takes 3-4 months in the W.D. Tenn. The 341 meeting occurs about 30 days after filing."),
     ("What property can I keep in Chapter 7 in Tennessee?","Tennessee lets you choose state or federal exemptions. State: $5,000/$7,500 homestead, $4,000 household goods, $10,000 wildcard. Federal: $27,900 homestead, $4,450 vehicle, $1,475 wildcard.")],
    [("Home",f"https://{DOMAIN}"),("Memphis",f"https://{DOMAIN}/memphis/"),("Chapter 7",f"https://{DOMAIN}/memphis/chapter-7.html")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Chapter 7 Bankruptcy in Memphis</h1>
<p class="subtitle">Chapter 7 is the fastest path to debt relief. Most unsecured debts are eliminated in 3-4 months. Here is what Memphis residents need to know.</p>
</div></div>

<section><div class="container">
<h2>What Is Chapter 7?</h2>
<div class="card">
<p>Chapter 7, sometimes called "liquidation bankruptcy" or a "<a href="https://bankruptcyfreshstart.org">fresh start</a>," eliminates most unsecured debts. A court-appointed trustee reviews your assets. If you have non-exempt property, the trustee may sell it to pay creditors -- but most Chapter 7 cases are "no-asset" cases where the filer keeps everything.</p>
<p>In Memphis, the vast majority of Chapter 7 filers keep all their property because it falls within <a href="/memphis/exemptions.html">Tennessee exemption limits</a> or the more generous federal exemptions.</p>
</div>
</div></section>

<section><div class="container">
<h2>Debts Chapter 7 Eliminates</h2>
<div class="compare-grid">
<div class="compare-card" style="border-color:#3fb950">
<h3 style="color:#3fb950">Dischargeable</h3>
<ul>
<li>Credit card debt</li>
<li><a href="/memphis/medical-debt.html">Medical bills</a></li>
<li>Personal loans</li>
<li>Utility bills</li>
<li>Some older tax debts</li>
<li>Deficiency balances</li>
</ul>
</div>
<div class="compare-card" style="border-color:#f85149">
<h3 style="color:#f85149">NOT Dischargeable</h3>
<ul>
<li>Student loans (usually)</li>
<li>Recent taxes (last 3 years)</li>
<li>Child support / alimony</li>
<li>Debts from fraud</li>
<li>Criminal fines</li>
<li>Most government debts</li>
</ul>
</div>
</div>
</div></section>

<section><div class="container">
<h2>Memphis Means Test</h2>
<div class="card">
<p>The <a href="https://meanstest.org">means test</a> compares your household income to the Tennessee state median. If your income is below the median, you automatically qualify for Chapter 7.</p>
<h3>2026 Tennessee Median Income Thresholds</h3>
<table>
<thead><tr><th>Household Size</th><th>Annual Median</th><th>Monthly</th></tr></thead>
<tbody>
<tr><td>1 person</td><td style="color:#3fb950;font-weight:700">$53,697</td><td>$4,475</td></tr>
<tr><td>2 persons</td><td style="color:#3fb950;font-weight:700">$67,854</td><td>$5,655</td></tr>
<tr><td>3 persons</td><td style="color:#3fb950;font-weight:700">$77,379</td><td>$6,448</td></tr>
<tr><td>4 persons</td><td style="color:#3fb950;font-weight:700">$94,416</td><td>$7,868</td></tr>
</tbody>
</table>
<p style="margin-top:12px">If your income exceeds the median, you may still qualify after deducting allowed expenses. <a href="/memphis/means-test.html">Full means test guide &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 7 Timeline in Memphis</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Credit counseling</strong> -- Complete an approved course (within 180 days before filing)</div>
<div class="step"><span class="step-number">2</span><strong>File petition</strong> -- Submit forms to W.D. Tenn. at {courthouse}</div>
<div class="step"><span class="step-number">3</span><strong><a href="/memphis/341-meeting.html">341 meeting</a></strong> -- About 30 days after filing. Answer questions under oath.</div>
<div class="step"><span class="step-number">4</span><strong>Financial management course</strong> -- Complete before discharge</div>
<div class="step"><span class="step-number">5</span><strong>Discharge</strong> -- Typically 60-90 days after 341 meeting (3-4 months total)</div>
</div>
</div></section>

<section><div class="container">
<h2>Tennessee Exemptions in Chapter 7</h2>
<div class="card">
<p>Tennessee allows you to choose between state and federal exemptions. This is a significant advantage -- compare both to see which protects more of your property.</p>
{exemption_table()}
<p style="margin-top:12px"><a href="/memphis/exemptions.html">Full exemption comparison &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What debts does Chapter 7 eliminate?</summary><div class="answer"><p>Chapter 7 discharges most unsecured debts including credit cards, medical bills, personal loans, and old utility bills. It does not discharge student loans (usually), recent taxes, child support, alimony, or debts from fraud.</p></div></details>
<details class="faq-item"><summary>Will I lose my car in Chapter 7?</summary><div class="answer"><p>Tennessee's $10,000 wildcard exemption can protect vehicle equity. Alternatively, the federal vehicle exemption is $4,450. If you owe more than the car is worth, you can usually keep it by reaffirming the loan. <a href="/memphis/keep-your-car.html">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>How long does Chapter 7 take in Memphis?</summary><div class="answer"><p>From filing to discharge, about 3-4 months. The 341 meeting is about 30 days after filing.</p></div></details>
<details class="faq-item"><summary>Can I file Chapter 7 if I have a job?</summary><div class="answer"><p>Yes. Having a job does not disqualify you. The means test compares your income to Tennessee's median. Many working people qualify. <a href="/memphis/means-test.html">Check the means test</a>.</p></div></details>
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Memphis chapter-13
write_page("memphis/chapter-13.html", f"""{head(
    "Chapter 13 Bankruptcy in Memphis -- Repayment Plan Guide | Tennessee Bankruptcy Guide",
    "Guide to Chapter 13 bankruptcy in Memphis, TN. W.D. Tenn. has the worst dismissal rate in the nation at 79.6%. Learn what to expect and how to protect yourself.",
    f"https://{DOMAIN}/memphis/chapter-13.html",
    [("What is Chapter 13 bankruptcy?","Chapter 13 allows you to keep your property while repaying debts over 3-5 years through a court-approved plan."),
     ("What is the Chapter 13 dismissal rate in Memphis?","W.D. Tenn. has a 79.6% Chapter 13 dismissal rate -- the worst in the nation. More than 3 out of 4 cases end without a discharge."),
     ("How long does Chapter 13 take?","The repayment plan lasts 3-5 years. Below-median income filers may qualify for a 3-year plan; above-median must complete 5 years."),
     ("Can I save my house in Chapter 13?","Yes. Chapter 13 allows you to catch up on missed mortgage payments over the life of the plan while keeping your home.")],
    [("Home",f"https://{DOMAIN}"),("Memphis",f"https://{DOMAIN}/memphis/"),("Chapter 13",f"https://{DOMAIN}/memphis/chapter-13.html")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Chapter 13 Bankruptcy in Memphis</h1>
<p class="subtitle">Chapter 13 lets you keep your property while repaying debts over 3-5 years. But in Memphis, the numbers are alarming: W.D. Tenn. has the highest Chapter 13 dismissal rate in the entire country.</p>
<div class="alert">79.6% of Chapter 13 cases in W.D. Tenn. end in dismissal</div>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card danger"><div class="number">79.6%</div><div class="label">Dismissal Rate</div></div>
<div class="stat-card danger"><div class="number">53.5%</div><div class="label">Prior Filer Rate</div></div>
<div class="stat-card"><div class="number">3-5 yrs</div><div class="label">Plan Length</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>How Chapter 13 Works</h2>
<div class="card">
<p>In Chapter 13, you propose a repayment plan to pay back some or all of your debts over 3-5 years. You make monthly payments to a trustee, who distributes funds to creditors. At the end, remaining eligible unsecured debts are discharged.</p>
<p>Chapter 13 is especially useful for:</p>
<ul>
<li><strong>Saving your home</strong> -- catch up on missed mortgage payments over the plan</li>
<li><strong><a href="/memphis/keep-your-car.html">Keeping your car</a></strong> -- cure defaults and potentially reduce the loan balance</li>
<li><strong>Stopping wage garnishments</strong> -- the <a href="https://automaticstay.org">automatic stay</a> halts collections</li>
<li><strong>Repaying tax debts</strong> -- spread tax obligations over 3-5 years</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>The Memphis Dismissal Problem</h2>
<div class="card" style="border-color:#f85149">
<p>W.D. Tenn. has a <strong>79.6% Chapter 13 dismissal rate</strong>, making it the worst-performing district in the country. This means fewer than 1 in 4 Chapter 13 filers here actually receive a discharge.</p>
<p>The 53.5% prior-filer rate indicates that many people in this district file Chapter 13 multiple times without ever completing a plan. Each filing costs money and time while providing only temporary relief from the <a href="https://automaticstay.org">automatic stay</a>.</p>
<p><strong>Before filing Chapter 13 in Memphis, seriously consider whether Chapter 7 is an option.</strong> If you qualify for Chapter 7, it eliminates debt in months rather than years and does not depend on completing a multi-year plan.</p>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 13 Timeline</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Credit counseling</strong> -- Required before filing</div>
<div class="step"><span class="step-number">2</span><strong>File petition + plan</strong> -- Submit to W.D. Tenn.</div>
<div class="step"><span class="step-number">3</span><strong>Begin payments</strong> -- Within 30 days of filing (before confirmation)</div>
<div class="step"><span class="step-number">4</span><strong><a href="/memphis/341-meeting.html">341 meeting</a></strong> -- 20-50 days after filing</div>
<div class="step"><span class="step-number">5</span><strong>Confirmation hearing</strong> -- Court approves the plan</div>
<div class="step"><span class="step-number">6</span><strong>Complete plan</strong> -- 3-5 years of payments</div>
<div class="step"><span class="step-number">7</span><strong>Financial management course</strong> + <strong>discharge</strong></div>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>What is the Chapter 13 dismissal rate in Memphis?</summary><div class="answer"><p>79.6% -- the worst in the nation. More than 3 out of 4 Chapter 13 cases in the Western District of Tennessee end in dismissal rather than discharge.</p></div></details>
<details class="faq-item"><summary>Can I save my house from foreclosure in Chapter 13?</summary><div class="answer"><p>Yes. The automatic stay stops foreclosure immediately, and your plan can include catch-up payments on the mortgage arrearage. <a href="/memphis/keep-your-house.html">More details</a>.</p></div></details>
<details class="faq-item"><summary>What happens if my Chapter 13 is dismissed?</summary><div class="answer"><p>Dismissal means creditors can resume collection activity. You lose the protection of the automatic stay. Repeated filings may result in a shortened or denied stay. <a href="https://bankruptcydismissed.com">Learn more about dismissal</a>.</p></div></details>
<details class="faq-item"><summary>Should I file Chapter 7 instead?</summary><div class="answer"><p>Given the 79.6% dismissal rate, Chapter 7 may be the safer option if you qualify. <a href="https://chapter7vs13.org">Compare Chapter 7 vs 13</a>.</p></div></details>
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Memphis exemptions
write_page("memphis/exemptions.html", f"""{head(
    "Memphis Bankruptcy Exemptions -- State vs Federal | Tennessee Bankruptcy Guide",
    "Tennessee bankruptcy exemptions for Memphis filers. Compare state exemptions ($5,000 homestead) with federal exemptions ($27,900 homestead). Choose which protects more.",
    f"https://{DOMAIN}/memphis/exemptions.html",
    [("What is the homestead exemption in Tennessee?","$5,000 for an individual or $7,500 for a family/couple. But Tennessee allows you to choose federal exemptions instead, where the homestead is $27,900."),
     ("Can I choose federal exemptions in Tennessee?","Yes. Tennessee is one of the states that allows filers to choose between state and federal exemption systems."),
     ("What is the vehicle exemption in Memphis?","Tennessee has no specific vehicle exemption under state law, but offers a $10,000 wildcard. Federal exemptions provide a $4,450 vehicle exemption plus a $1,475 wildcard.")],
    [("Home",f"https://{DOMAIN}"),("Memphis",f"https://{DOMAIN}/memphis/"),("Exemptions",f"https://{DOMAIN}/memphis/exemptions.html")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Memphis Bankruptcy Exemptions</h1>
<p class="subtitle">Tennessee allows you to choose between state and federal exemptions -- a significant advantage. Compare both systems to protect the most property.</p>
</div></div>

<section><div class="container">
<h2>State vs. Federal Exemptions</h2>
<div class="card">
<p>Tennessee is one of the states that lets filers choose between state exemptions and the federal bankruptcy exemptions under 11 U.S.C. section 522(d). You must pick one system -- you cannot mix and match.</p>
<p>For many Memphis filers, <strong>federal exemptions are the better choice</strong> because the federal homestead exemption ($27,900) is much higher than Tennessee's ($5,000/$7,500).</p>
{exemption_table()}
</div>
</div></section>

<section><div class="container">
<h2>When to Choose State Exemptions</h2>
<div class="card">
<ul>
<li>You have little or no home equity but significant personal property</li>
<li>Tennessee's $10,000 wildcard covers your most valuable assets</li>
<li>You have large household goods collections (state: $4,000)</li>
</ul>
</div>
<h2>When to Choose Federal Exemptions</h2>
<div class="card">
<ul>
<li>You own a home with equity between $7,500 and $27,900</li>
<li>You need the federal vehicle exemption ($4,450)</li>
<li>You are not married (state homestead is only $5,000 for individuals)</li>
<li>You want to stack the unused homestead as wildcard ($1,475 + up to $13,950)</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Can married couples double exemptions in Tennessee?</summary><div class="answer"><p>If both spouses file jointly, each spouse claims their own set of exemptions. Both must choose the same system (both state or both federal).</p></div></details>
<details class="faq-item"><summary>What happens to property that is not exempt?</summary><div class="answer"><p>In Chapter 7, the trustee may sell non-exempt property to pay creditors. In Chapter 13, non-exempt property value determines your minimum plan payment but you keep everything.</p></div></details>
<details class="faq-item"><summary>Is my retirement account protected?</summary><div class="answer"><p>Yes. 401(k)s, IRAs, and other qualified retirement accounts are fully exempt under both state and federal exemption systems.</p></div></details>
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Memphis cost
write_page("memphis/cost.html", f"""{head(
    "How Much Does Bankruptcy Cost in Memphis? | Tennessee Bankruptcy Guide",
    "Complete cost breakdown for filing bankruptcy in Memphis, TN. Filing fees, attorney fees, credit counseling, and ways to reduce costs.",
    f"https://{DOMAIN}/memphis/cost.html",
    [("How much does Chapter 7 cost in Memphis?","Filing fee: $338. Attorney fees: $900-$1,800. Credit counseling: $25-$50 total."),
     ("How much does Chapter 13 cost in Memphis?","Filing fee: $313. Attorney fees: $2,500-$4,000 (paid through the plan). Credit counseling: $25-$50 total."),
     ("Can I file bankruptcy for free?","Chapter 7 filing fee waivers are available if your income is below 150% of federal poverty guidelines. Chapter 13 fees can be paid through your plan.")],
    [("Home",f"https://{DOMAIN}"),("Memphis",f"https://{DOMAIN}/memphis/"),("Cost",f"https://{DOMAIN}/memphis/cost.html")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>How Much Does Bankruptcy Cost in Memphis?</h1>
<p class="subtitle">A complete breakdown of bankruptcy costs for Memphis residents, including filing fees, attorney fees, and ways to reduce your out-of-pocket expenses.</p>
</div></div>

<section><div class="container">
<h2>Cost Breakdown</h2>
<div class="card">
<table>
<thead><tr><th>Expense</th><th>Chapter 7</th><th>Chapter 13</th></tr></thead>
<tbody>
<tr><td>Court filing fee</td><td>$338</td><td>$313</td></tr>
<tr><td>Attorney fees (typical)</td><td>$900 - $1,800</td><td>$2,500 - $4,000</td></tr>
<tr><td>Credit counseling (2 courses)</td><td>$25 - $50</td><td>$25 - $50</td></tr>
<tr><td><strong>Total (typical)</strong></td><td><strong>$1,263 - $2,188</strong></td><td><strong>$2,838 - $4,363</strong></td></tr>
</tbody>
</table>
</div>
</div></section>

<section><div class="container">
<h2>Ways to Reduce Costs</h2>
<div class="card">
<ul>
<li><strong>Fee waiver (Chapter 7):</strong> If your income is below 150% of federal poverty guidelines</li>
<li><strong>Installment payments:</strong> Ask the court to pay the filing fee in installments</li>
<li><strong>Chapter 13 fees through plan:</strong> Attorney fees can be paid through your repayment plan</li>
<li><strong>Pro se filing:</strong> You can file without an attorney, though this is not recommended</li>
<li><strong>Legal aid:</strong> Contact {legal_aid} at {legal_aid_phone}</li>
</ul>
</div>
{DISCLAIMER}
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Memphis FAQ
write_page("memphis/faq.html", f"""{head(
    "Memphis Bankruptcy FAQ -- Common Questions Answered | Tennessee Bankruptcy Guide",
    "Frequently asked questions about filing bankruptcy in Memphis, TN. Covers costs, exemptions, the 341 meeting, timeline, and the W.D. Tenn. dismissal rate.",
    f"https://{DOMAIN}/memphis/faq.html",
    [("How much does bankruptcy cost in Memphis?","Chapter 7: $1,263-$2,188 total. Chapter 13: $2,838-$4,363 total. Includes filing fees, attorney fees, and credit counseling."),
     ("What is the automatic stay?","The automatic stay is a court order that immediately stops most collection actions, including foreclosure, repossession, wage garnishment, and lawsuits."),
     ("How long does bankruptcy stay on my credit report?","Chapter 7: 10 years from filing. Chapter 13: 7 years from filing."),
     ("Can I file bankruptcy without an attorney?","Yes, but it is not recommended. Bankruptcy law is complex and mistakes can result in dismissal or loss of property.")],
    [("Home",f"https://{DOMAIN}"),("Memphis",f"https://{DOMAIN}/memphis/"),("FAQ",f"https://{DOMAIN}/memphis/faq.html")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Memphis Bankruptcy FAQ</h1>
<p class="subtitle">Answers to the most common questions about filing bankruptcy in Memphis, Tennessee.</p>
</div></div>

<section><div class="container">
<h2>General Questions</h2>
<details class="faq-item"><summary>How much does bankruptcy cost in Memphis?</summary><div class="answer"><p>Chapter 7: $338 filing fee + $900-$1,800 attorney fees. Chapter 13: $313 filing fee + $2,500-$4,000 attorney fees. Credit counseling adds $25-$50. <a href="/memphis/cost.html">Full breakdown</a>.</p></div></details>
<details class="faq-item"><summary>What is the automatic stay?</summary><div class="answer"><p>The <a href="https://automaticstay.org">automatic stay</a> is a court order that immediately stops foreclosure, repossession, wage garnishment, lawsuits, and most other collection actions the moment you file.</p></div></details>
<details class="faq-item"><summary>Where do I file for bankruptcy in Memphis?</summary><div class="answer"><p>Western District of Tennessee, {courthouse}. Phone: {phone}.</p></div></details>
<details class="faq-item"><summary>Should I file Chapter 7 or Chapter 13?</summary><div class="answer"><p>Chapter 7 eliminates debt in 3-4 months but requires passing a means test. Chapter 13 lets you keep property through a 3-5 year plan but has a 79.6% dismissal rate in W.D. Tenn. <a href="https://chapter7vs13.org">Compare chapters</a>.</p></div></details>
<details class="faq-item"><summary>Can I file bankruptcy without an attorney?</summary><div class="answer"><p>Yes, you can file "pro se," but it is not recommended. Bankruptcy involves complex forms and procedures. Mistakes can lead to dismissal or loss of property.</p></div></details>
<details class="faq-item"><summary>What is the means test?</summary><div class="answer"><p>The <a href="https://meanstest.org">means test</a> determines Chapter 7 eligibility by comparing your income to Tennessee's median. <a href="/memphis/means-test.html">Memphis means test guide</a>.</p></div></details>
<details class="faq-item"><summary>How long does bankruptcy stay on my credit?</summary><div class="answer"><p>Chapter 7: 10 years from filing. Chapter 13: 7 years from filing. <a href="/memphis/credit-after-bankruptcy.html">Rebuilding your credit</a>.</p></div></details>
<details class="faq-item"><summary>Will I lose my house?</summary><div class="answer"><p>It depends on your equity and which exemption system you choose. Tennessee allows federal exemptions ($27,900 homestead). <a href="/memphis/keep-your-house.html">Full guide</a>.</p></div></details>
<details class="faq-item"><summary>Will I lose my car?</summary><div class="answer"><p>Usually not. Tennessee's $10,000 wildcard or federal $4,450 vehicle exemption protects most vehicles. <a href="/memphis/keep-your-car.html">Full guide</a>.</p></div></details>
<details class="faq-item"><summary>What is the 341 meeting?</summary><div class="answer"><p>The <a href="https://341meeting.org">341 meeting of creditors</a> is a brief hearing about 30 days after filing where you answer questions under oath about your finances. <a href="/memphis/341-meeting.html">What to expect</a>.</p></div></details>
<details class="faq-item"><summary>Can I file bankruptcy again?</summary><div class="answer"><p>Yes, but timing rules apply. Chapter 7 to Chapter 7: 8 years. Chapter 13 to Chapter 13: 2 years. <a href="https://filebankruptcyagain.com">Full timing rules</a> or use the <a href="https://1328f.com">1328(f) screener</a>.</p></div></details>
<details class="faq-item"><summary>Why is the dismissal rate so high in Memphis?</summary><div class="answer"><p>W.D. Tenn. has a 79.6% Chapter 13 dismissal rate. Contributing factors include poverty, aggressive filing practices, and a 53.5% prior-filer rate suggesting repeat filings without plan completion.</p></div></details>
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Helper for remaining Memphis topic pages
def memphis_topic(slug, title_short, title_full, desc, subtitle, body_html, faq_pairs):
    crumbs = [("Home",f"https://{DOMAIN}"),("Memphis",f"https://{DOMAIN}/memphis/"),(title_short,f"https://{DOMAIN}/memphis/{slug}.html")]
    write_page(f"memphis/{slug}.html", f"""{head(
    f"{title_full} | Tennessee Bankruptcy Guide",
    desc,
    f"https://{DOMAIN}/memphis/{slug}.html",
    faq_pairs,
    crumbs
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>{title_full}</h1>
<p class="subtitle">{subtitle}</p>
</div></div>
{body_html}
<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# means-test
memphis_topic("means-test", "Means Test",
    "Memphis Means Test -- Do You Qualify for Chapter 7?",
    "How the bankruptcy means test works for Memphis residents. Tennessee median income thresholds and step-by-step walkthrough.",
    "The means test determines whether you can file Chapter 7 bankruptcy. It compares your income to the Tennessee state median for your household size.",
    f"""<section><div class="container">
<h2>2026 Tennessee Median Income Thresholds</h2>
<div class="card"><table>
<thead><tr><th>Household Size</th><th>Annual Median</th><th>Monthly</th></tr></thead>
<tbody>
<tr><td>1 person</td><td style="color:#3fb950;font-weight:700">$53,697</td><td>$4,475</td></tr>
<tr><td>2 persons</td><td style="color:#3fb950;font-weight:700">$67,854</td><td>$5,655</td></tr>
<tr><td>3 persons</td><td style="color:#3fb950;font-weight:700">$77,379</td><td>$6,448</td></tr>
<tr><td>4 persons</td><td style="color:#3fb950;font-weight:700">$94,416</td><td>$7,868</td></tr>
</tbody>
</table>
<p style="margin-top:12px">Add $9,900 for each additional person beyond 4.</p>
</div>
</div></section>

<section><div class="container">
<h2>How the Means Test Works</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Calculate your income</strong> -- Average your last 6 months of gross income</div>
<div class="step"><span class="step-number">2</span><strong>Compare to median</strong> -- If below Tennessee's median for your household size, you pass automatically</div>
<div class="step"><span class="step-number">3</span><strong>If above median</strong> -- Deduct allowed expenses (mortgage, car payments, taxes, health insurance, etc.)</div>
<div class="step"><span class="step-number">4</span><strong>Calculate disposable income</strong> -- If remaining disposable income is low enough, you still qualify</div>
</div>
<p>Not sure if you qualify? The <a href="https://meanstest.org">means test calculator</a> can help estimate your eligibility.</p>
</div></section>

<section><div class="container">
<h2>What If You Do Not Pass?</h2>
<div class="card">
<ul>
<li><strong>File Chapter 13 instead</strong> -- No means test required (but note the 79.6% dismissal rate in W.D. Tenn.)</li>
<li><strong>Wait for income to drop</strong> -- The test uses the last 6 months' income</li>
<li><strong>Special circumstances</strong> -- Military service, serious illness, or job loss may qualify for exemptions</li>
</ul>
</div>
</div></section>""",
    [("What is the means test?","The means test compares your income to Tennessee median income. If below, you qualify for Chapter 7 automatically."),
     ("What is the Tennessee median income for 2026?","Single filer: $53,697. 2-person: $67,854. 3-person: $77,379. 4-person: $94,416."),
     ("What if I fail the means test?","You can file Chapter 13 instead, wait until income drops, or challenge with special circumstances.")])

# automatic-stay
memphis_topic("automatic-stay", "Automatic Stay",
    "The Automatic Stay in Memphis Bankruptcy",
    "How the automatic stay protects Memphis residents when filing bankruptcy. Stops foreclosure, repossession, garnishment, and lawsuits immediately.",
    "The moment you file bankruptcy, the automatic stay stops most collection actions against you. This is one of the most powerful protections in bankruptcy law.",
    f"""<section><div class="container">
<h2>What the Automatic Stay Stops</h2>
<div class="compare-grid">
<div class="compare-card" style="border-color:#3fb950">
<h3 style="color:#3fb950">Stopped by Automatic Stay</h3>
<ul>
<li>Foreclosure proceedings</li>
<li>Vehicle repossession</li>
<li>Wage garnishment</li>
<li>Lawsuits and judgments</li>
<li>Collection calls and letters</li>
<li>Utility disconnection (20 days)</li>
<li>Bank account levies</li>
</ul>
</div>
<div class="compare-card" style="border-color:#f85149">
<h3 style="color:#f85149">NOT Stopped</h3>
<ul>
<li>Criminal proceedings</li>
<li>Child support / alimony actions</li>
<li>Tax audits (assessment only)</li>
<li>Eviction (in some cases)</li>
<li>Pension loan repayment</li>
</ul>
</div>
</div>
</div></section>

<section><div class="container">
<h2>Tennessee-Specific Concerns</h2>
<div class="card">
<p>Tennessee uses <strong>non-judicial foreclosure</strong>, meaning your lender can foreclose without going through court. This makes the automatic stay especially critical for Memphis homeowners -- it may be the only thing stopping a foreclosure sale.</p>
<p>However, be aware that repeat filers face reduced protection:</p>
<ul>
<li><strong>Second filing within 1 year:</strong> Automatic stay expires after 30 days unless you prove good faith</li>
<li><strong>Third+ filing within 1 year:</strong> No automatic stay at all unless you get a court order</li>
</ul>
<p>Given the 53.5% prior-filer rate in W.D. Tenn., many Memphis filers may face these limitations.</p>
</div>
<p>Learn more at <a href="https://automaticstay.org">automaticstay.org</a>.</p>
</div></section>""",
    [("What does the automatic stay stop?","Foreclosure, repossession, wage garnishment, lawsuits, collection calls, and utility shutoffs."),
     ("When does the automatic stay take effect?","Immediately upon filing your bankruptcy petition."),
     ("Does the stay apply to repeat filers?","Limited. Second filing in a year: 30-day stay. Third+ filing in a year: no automatic stay without court order.")])

# keep-your-car
memphis_topic("keep-your-car", "Keep Your Car",
    "Can You Keep Your Car in Memphis Bankruptcy?",
    "How to protect your vehicle when filing bankruptcy in Memphis. Tennessee exemptions, reaffirmation, and redemption options.",
    "Most Memphis residents can keep their car when filing bankruptcy. Here is how to protect your vehicle using Tennessee or federal exemptions.",
    f"""<section><div class="container">
<h2>Vehicle Exemptions</h2>
<div class="card">
<table>
<tr><th>System</th><th>Vehicle Protection</th></tr>
<tr><td>Tennessee state</td><td>$10,000 wildcard (no specific vehicle exemption)</td></tr>
<tr><td>Federal</td><td>$4,450 vehicle + $1,475 wildcard (+ up to $13,950 unused homestead)</td></tr>
</table>
<p style="margin-top:12px">If you do not own a home, the federal wildcard can protect up to <strong>$19,875</strong> in vehicle equity ($4,450 + $1,475 + $13,950).</p>
</div>
</div></section>

<section><div class="container">
<h2>Options for Cars with Loans</h2>
<div class="card">
<ul>
<li><strong>Reaffirmation:</strong> Sign a new agreement to keep paying. Keeps the car but you remain liable.</li>
<li><strong>Redemption:</strong> Pay the car's current value in a lump sum, discharge the remaining balance.</li>
<li><strong>Surrender:</strong> Return the car and discharge the remaining debt.</li>
<li><strong>Chapter 13 cramdown:</strong> If the loan is over 910 days old, you may reduce the balance to the car's current value.</li>
</ul>
</div>
</div></section>""",
    [("Can I keep my car in bankruptcy?","Usually yes. Tennessee's $10,000 wildcard or federal $4,450 vehicle exemption protects most vehicles."),
     ("What if I owe more than the car is worth?","You can reaffirm the loan, redeem for current value, or surrender and discharge the debt."),
     ("What is a cramdown?","In Chapter 13, if your car loan is over 910 days old, you may reduce the balance to the car's current market value.")])

# keep-your-house
memphis_topic("keep-your-house", "Keep Your House",
    "Can You Keep Your House in Memphis Bankruptcy?",
    "How to protect your home when filing bankruptcy in Memphis. Tennessee vs federal homestead exemption comparison. Non-judicial foreclosure state.",
    "Tennessee has a low state homestead exemption, but you can choose federal exemptions -- which protect far more equity. Here is how to keep your home.",
    f"""<section><div class="container">
<h2>Homestead Exemption Comparison</h2>
<div class="card">
<table>
<tr><th>System</th><th>Homestead Protection</th></tr>
<tr><td>Tennessee state (individual)</td><td>$5,000</td></tr>
<tr><td>Tennessee state (family/62+)</td><td>$7,500</td></tr>
<tr><td>Federal</td><td>$27,900</td></tr>
</table>
<div class="quick-answer">Federal exemptions protect over 5x more home equity than Tennessee state exemptions. Most Memphis homeowners should choose federal.</div>
</div>
</div></section>

<section><div class="container">
<h2>Non-Judicial Foreclosure Warning</h2>
<div class="card" style="border-color:#d29922">
<p>Tennessee is a <strong>non-judicial foreclosure state</strong>. Your lender can foreclose without going to court, with as little as 20 days' notice. The bankruptcy <a href="https://automaticstay.org">automatic stay</a> is the most effective way to stop a non-judicial foreclosure.</p>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 7 vs Chapter 13 for Homeowners</h2>
<div class="compare-grid">
<div class="compare-card">
<h3>Chapter 7</h3>
<ul>
<li>Keep home if equity is within exemptions</li>
<li>Must be current on mortgage or catch up quickly</li>
<li>Does not help with mortgage arrears</li>
</ul>
</div>
<div class="compare-card">
<h3>Chapter 13</h3>
<ul>
<li>Catch up on missed payments over 3-5 years</li>
<li>Strip off junior liens if underwater</li>
<li>But: 79.6% dismissal rate in W.D. Tenn.</li>
</ul>
</div>
</div>
</div></section>""",
    [("Will I lose my house in bankruptcy?","Not if your equity is within exemptions. Federal exemptions protect $27,900 of home equity."),
     ("Is Tennessee a non-judicial foreclosure state?","Yes. Lenders can foreclose without court proceedings. The automatic stay stops this."),
     ("Should I use state or federal exemptions for my home?","Usually federal -- $27,900 vs $5,000/$7,500 state.")])

# medical-debt
memphis_topic("medical-debt", "Medical Debt",
    "Eliminating Medical Debt in Memphis Bankruptcy",
    "How Memphis residents can eliminate medical debt through bankruptcy. Medical bills are fully dischargeable in Chapter 7 and Chapter 13.",
    "Medical debt is the leading cause of bankruptcy in America. In Memphis, medical bills are fully dischargeable in both Chapter 7 and Chapter 13.",
    f"""<section><div class="container">
<h2>Medical Debt in Bankruptcy</h2>
<div class="card">
<div class="quick-answer">Medical debt is 100% dischargeable in bankruptcy. It is treated as general unsecured debt with no special protections for creditors.</div>
<p>Whether you owe $5,000 or $500,000 in medical bills, bankruptcy can eliminate it entirely. In Chapter 7, medical debt is wiped out in 3-4 months. In Chapter 13, you may pay a portion through your plan, with the remainder discharged.</p>
</div>
</div></section>

<section><div class="container">
<h2>Before Filing: Know Your Options</h2>
<div class="card">
<ul>
<li><strong>Negotiate directly:</strong> Many Memphis hospitals offer charity care or payment reductions</li>
<li><strong>Check for billing errors:</strong> Medical billing errors are common</li>
<li><strong>Statute of limitations:</strong> Tennessee's statute of limitations on medical debt is 6 years</li>
<li><strong>Credit reporting:</strong> Medical debt under $500 no longer appears on credit reports</li>
</ul>
<p>If negotiation is not enough and you have other debts too, bankruptcy may be the most effective solution.</p>
</div>
</div></section>""",
    [("Is medical debt dischargeable in bankruptcy?","Yes, 100%. Medical bills are general unsecured debt and are fully eliminated in both Chapter 7 and Chapter 13."),
     ("What is the statute of limitations on medical debt in Tennessee?","6 years from the date of last payment or service."),
     ("Should I file bankruptcy for medical debt alone?","It depends on the amount and your other debts. Consult with an attorney to evaluate all options.")])

# 341-meeting
memphis_topic("341-meeting", "341 Meeting",
    "The 341 Meeting in Memphis -- What to Expect",
    "What to expect at your 341 meeting of creditors in Memphis. How to prepare, what questions are asked, and where it takes place.",
    "The 341 meeting of creditors is a brief hearing about 30 days after you file bankruptcy. Here is what Memphis filers need to know.",
    f"""<section><div class="container">
<h2>What Is the 341 Meeting?</h2>
<div class="card">
<p>The <a href="https://341meeting.org">341 meeting of creditors</a> (named after 11 U.S.C. section 341) is a required hearing where you answer questions under oath about your finances, assets, and the information in your petition.</p>
<p>The meeting is conducted by the Chapter 7 or Chapter 13 trustee, not a judge. It typically lasts 5-10 minutes if everything is in order.</p>
</div>
</div></section>

<section><div class="container">
<h2>Where and When</h2>
<div class="card">
<p><strong>Location:</strong> 341 meetings in Memphis are typically held at or near the W.D. Tenn. courthouse at {courthouse}.</p>
<p><strong>Timing:</strong> Usually scheduled 20-40 days after filing. You will receive a notice with the exact date, time, and location.</p>
</div>
</div></section>

<section><div class="container">
<h2>What to Bring</h2>
<div class="card">
<ul>
<li>Government-issued photo ID (driver's license or passport)</li>
<li>Social Security card or proof of SSN</li>
<li>Recent pay stubs (last 60 days)</li>
<li>Most recent tax return</li>
<li>Bank statements (last 2-3 months)</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Common Questions Asked</h2>
<div class="card">
<ul>
<li>Did you review the petition before signing?</li>
<li>Is the information accurate?</li>
<li>Do you own any real estate?</li>
<li>Have you transferred or sold any property recently?</li>
<li>Are you expecting any inheritance or lawsuit settlement?</li>
<li>Do you have any additional bank accounts?</li>
</ul>
</div>
</div></section>""",
    [("What is the 341 meeting?","A brief hearing where you answer questions under oath about your finances. Conducted by the trustee, not a judge."),
     ("How long does the 341 meeting last?","Typically 5-10 minutes if all documents are in order."),
     ("Do creditors attend the 341 meeting?","They can, but most do not. In consumer cases, creditor attendance is rare.")])

# timeline
memphis_topic("timeline", "Timeline",
    "Memphis Bankruptcy Timeline -- How Long Does It Take?",
    "Step-by-step timeline for filing bankruptcy in Memphis. Chapter 7 takes 3-4 months. Chapter 13 takes 3-5 years.",
    "From pre-filing preparation to discharge, here is a detailed timeline for filing bankruptcy in Memphis.",
    f"""<section><div class="container">
<h2>Chapter 7 Timeline</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Before filing:</strong> Complete credit counseling course (up to 180 days before)</div>
<div class="step"><span class="step-number">2</span><strong>Day 1:</strong> File petition with W.D. Tenn. Automatic stay takes effect immediately.</div>
<div class="step"><span class="step-number">3</span><strong>Day 20-40:</strong> <a href="/memphis/341-meeting.html">341 meeting of creditors</a></div>
<div class="step"><span class="step-number">4</span><strong>Day 30-60:</strong> Complete financial management course</div>
<div class="step"><span class="step-number">5</span><strong>Day 60-90:</strong> Deadline for creditor objections</div>
<div class="step"><span class="step-number">6</span><strong>Day 90-120:</strong> Discharge granted (3-4 months total)</div>
<div class="step"><span class="step-number">7</span><strong>After discharge:</strong> Case closed. Begin <a href="/memphis/credit-after-bankruptcy.html">rebuilding credit</a>.</div>
</div>
</div></section>

<section><div class="container">
<h2>Chapter 13 Timeline</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Before filing:</strong> Complete credit counseling course</div>
<div class="step"><span class="step-number">2</span><strong>Day 1:</strong> File petition and proposed plan. Automatic stay takes effect.</div>
<div class="step"><span class="step-number">3</span><strong>Day 30:</strong> Begin plan payments (before confirmation)</div>
<div class="step"><span class="step-number">4</span><strong>Day 20-50:</strong> 341 meeting of creditors</div>
<div class="step"><span class="step-number">5</span><strong>Day 45-120:</strong> Confirmation hearing</div>
<div class="step"><span class="step-number">6</span><strong>Years 1-5:</strong> Make monthly plan payments</div>
<div class="step"><span class="step-number">7</span><strong>End of plan:</strong> Complete financial management course, receive discharge</div>
</div>
<div class="disclaimer">Remember: 79.6% of Chapter 13 cases in W.D. Tenn. end in dismissal before reaching discharge.</div>
</div>
</div></section>""",
    [("How long does Chapter 7 take in Memphis?","3-4 months from filing to discharge."),
     ("How long does Chapter 13 take?","3-5 years to complete the repayment plan."),
     ("When does the automatic stay start?","Immediately upon filing your petition.")])

# checklist
memphis_topic("checklist", "Checklist",
    "Memphis Bankruptcy Filing Checklist",
    "Complete checklist for filing bankruptcy in Memphis. Documents needed, steps to take, and common mistakes to avoid.",
    "Use this checklist to prepare for your Memphis bankruptcy filing. Proper preparation helps ensure a smooth process.",
    f"""<section><div class="container">
<h2>Documents to Gather</h2>
<div class="card">
<ul>
<li>Last 6 months of pay stubs or income records</li>
<li>Last 2 years of federal and state tax returns</li>
<li>Bank statements (all accounts, last 3-6 months)</li>
<li>Mortgage statements and property tax bills</li>
<li>Vehicle titles and loan statements</li>
<li>Credit card and loan statements (all debts)</li>
<li>Medical bills and collection letters</li>
<li>Insurance policies</li>
<li>Retirement account statements (401k, IRA)</li>
<li>Any court judgments, garnishment orders, or lawsuits</li>
<li>Lease agreements</li>
<li>Government-issued photo ID</li>
<li>Social Security card</li>
</ul>
</div>
</div></section>

<section><div class="container">
<h2>Steps Before Filing</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Complete credit counseling</strong> -- From an approved provider (within 180 days of filing)</div>
<div class="step"><span class="step-number">2</span><strong>Decide: state or federal exemptions</strong> -- Compare to protect the most property. <a href="/memphis/exemptions.html">Exemption guide</a></div>
<div class="step"><span class="step-number">3</span><strong>Run the means test</strong> -- Determine Chapter 7 eligibility. <a href="/memphis/means-test.html">Means test guide</a></div>
<div class="step"><span class="step-number">4</span><strong>List ALL debts</strong> -- Missing a debt means it may not be discharged</div>
<div class="step"><span class="step-number">5</span><strong>List ALL assets</strong> -- Hiding assets is a federal crime</div>
<div class="step"><span class="step-number">6</span><strong>Stop using credit cards</strong> -- Charges near filing time may be considered fraud</div>
<div class="step"><span class="step-number">7</span><strong>Do not transfer property</strong> -- Transfers within 2 years can be reversed</div>
</div>
</div></section>

<section><div class="container">
<h2>Common Mistakes to Avoid</h2>
<div class="card" style="border-color:#f85149">
<ul>
<li>Paying back family members before filing (preferential transfers)</li>
<li>Running up credit card debt before filing</li>
<li>Transferring property to friends or family</li>
<li>Cashing out retirement accounts (they are exempt!)</li>
<li>Filing without comparing state vs. federal exemptions</li>
<li>Not listing all creditors and debts</li>
</ul>
</div>
</div></section>""",
    [("What documents do I need to file bankruptcy?","Pay stubs, tax returns, bank statements, debt statements, property records, ID, and Social Security card."),
     ("What should I NOT do before filing bankruptcy?","Do not transfer property, pay back family members, run up new credit card debt, or cash out retirement accounts."),
     ("Do I need to complete credit counseling before filing?","Yes. You must complete an approved credit counseling course within 180 days before filing.")])

# credit-after-bankruptcy
memphis_topic("credit-after-bankruptcy", "Credit After Bankruptcy",
    "Rebuilding Credit After Bankruptcy in Memphis",
    "How to rebuild your credit score after filing bankruptcy in Memphis. Timeline, strategies, and realistic expectations.",
    "Bankruptcy is not the end of your financial life -- it is a fresh start. Here is how to rebuild your credit after filing in Memphis.",
    f"""<section><div class="container">
<h2>Credit Report Timeline</h2>
<div class="card">
<table>
<tr><th>Event</th><th>Duration on Credit Report</th></tr>
<tr><td>Chapter 7 filing</td><td>10 years from filing date</td></tr>
<tr><td>Chapter 13 filing</td><td>7 years from filing date</td></tr>
<tr><td>Individual discharged debts</td><td>7 years from date of default</td></tr>
</table>
</div>
</div></section>

<section><div class="container">
<h2>Steps to Rebuild</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Check your credit reports</strong> -- Ensure all discharged debts show $0 balance. Dispute errors.</div>
<div class="step"><span class="step-number">2</span><strong>Get a secured credit card</strong> -- Start with a small deposit ($200-$500). Use it lightly and pay in full monthly.</div>
<div class="step"><span class="step-number">3</span><strong>Pay all current bills on time</strong> -- Payment history is the biggest factor in your credit score.</div>
<div class="step"><span class="step-number">4</span><strong>Keep credit utilization low</strong> -- Use less than 30% of available credit (ideally under 10%).</div>
<div class="step"><span class="step-number">5</span><strong>Consider a credit-builder loan</strong> -- Available through credit unions and some banks.</div>
<div class="step"><span class="step-number">6</span><strong>Be patient</strong> -- Most filers see significant credit improvement within 1-2 years.</div>
</div>
</div></section>

<section><div class="container">
<h2>Realistic Expectations</h2>
<div class="card">
<ul>
<li><strong>6 months after:</strong> You may qualify for secured credit cards</li>
<li><strong>1-2 years after:</strong> Many filers reach 650+ credit scores</li>
<li><strong>2-3 years after:</strong> You may qualify for a car loan at reasonable rates</li>
<li><strong>3-4 years after:</strong> FHA mortgage may be possible (Chapter 7 requires 2-year wait)</li>
</ul>
<p>Learn more at <a href="https://rebuildcreditafterbankruptcy.com">rebuildcreditafterbankruptcy.com</a>.</p>
</div>
</div></section>""",
    [("How long does bankruptcy stay on my credit?","Chapter 7: 10 years. Chapter 13: 7 years."),
     ("Can I rebuild my credit after bankruptcy?","Yes. Most filers see significant improvement within 1-2 years with responsible credit use."),
     ("When can I buy a house after bankruptcy?","FHA loans: 2 years after Chapter 7 discharge, 1 year into Chapter 13 with court approval.")])

# =============================================================================
# MEMPHIS SUBURBS (8 pages)
# =============================================================================
def suburb_page(city_slug, city_name, suburb_slug, suburb_name, population, district, courthouse, state_flag=None, extra_note=""):
    """Generate a suburb page."""
    is_ms = "MS" in suburb_name or state_flag == "MS"
    if is_ms:
        jurisdiction_note = f"""<div class="card" style="border-color:#d29922">
<h3 style="color:#d29922">Mississippi Jurisdiction Notice</h3>
<p><strong>{suburb_name} is in Mississippi, not Tennessee.</strong> Residents file in the <strong>Northern District of Mississippi</strong>, not the Western District of Tennessee. Mississippi has different exemptions and procedures. We include {suburb_name} in the Memphis metro guide because it is part of the greater Memphis area, but Mississippi law governs your filing.</p>
</div>"""
        exemptions_section = """<section><div class="container">
<h2>Mississippi Exemptions</h2>
<div class="card">
<table>
<tr><th>Property</th><th>Mississippi Exemption</th></tr>
<tr><td>Homestead</td><td>$75,000 (160 acres)</td></tr>
<tr><td>Vehicle</td><td>$10,000</td></tr>
<tr><td>Personal property</td><td>$10,000</td></tr>
<tr><td>Retirement</td><td>Fully exempt</td></tr>
</table>
<p style="margin-top:8px;color:#d29922">Mississippi does NOT allow federal exemptions. State exemptions only.</p>
</div>
</div></section>"""
        file_district = "Northern District of Mississippi"
        file_courthouse = "703 N. 1st St, Oxford, MS 38655 (Aberdeen Division also serves DeSoto County)"
    else:
        jurisdiction_note = ""
        exemptions_section = f"""<section><div class="container">
<h2>Tennessee Exemptions</h2>
<div class="card">
<p>Tennessee allows you to choose between state and federal exemptions.</p>
{exemption_table()}
<p style="margin-top:12px"><a href="/{city_slug}/exemptions.html">Full exemption details &rarr;</a></p>
</div>
</div></section>"""
        file_district = district
        file_courthouse = courthouse

    faq_pairs = [
        (f"Where do {suburb_name} residents file?", f"{file_district} at {file_courthouse}"),
        (f"How much does bankruptcy cost in {suburb_name}?", "Chapter 7: $1,238-$2,188. Chapter 13: $2,838-$4,363 including filing fees, attorney fees, and credit counseling."),
        (f"What exemptions apply in {suburb_name}?", "Mississippi state exemptions only." if is_ms else "Tennessee state or federal exemptions -- filer's choice.")
    ]
    crumbs = [("Home",f"https://{DOMAIN}"),(city_name,f"https://{DOMAIN}/{city_slug}/"),(suburb_name.split(",")[0],f"https://{DOMAIN}/{city_slug}/suburbs/{suburb_slug}.html")]

    write_page(f"{city_slug}/suburbs/{suburb_slug}.html", f"""{head(
    f"Bankruptcy in {suburb_name} | Tennessee Bankruptcy Guide",
    f"Filing bankruptcy in {suburb_name}. {'Mississippi' if is_ms else 'Tennessee'} exemptions, {file_district} courthouse info, costs, and options.",
    f"https://{DOMAIN}/{city_slug}/suburbs/{suburb_slug}.html",
    faq_pairs,
    crumbs
)}
<body>
{nav(city_slug)}
<div class="hero"><div class="container">
<h1>Bankruptcy in {suburb_name}</h1>
<p class="subtitle">{suburb_name} residents considering bankruptcy can find help here. As part of the {city_name} metro area, {suburb_name.split(",")[0]} filers are served by the {file_district}.{extra_note}</p>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card"><div class="number">{population}</div><div class="label">Population (est.)</div></div>
<div class="stat-card"><div class="number">{"$75,000" if is_ms else "$5,000 / $7,500"}</div><div class="label">Homestead Exemption</div></div>
<div class="stat-card"><div class="number">{"$10,000" if is_ms else "$10,000 wildcard"}</div><div class="label">Vehicle Protection</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Chapter 7 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Where to File</h2>
<div class="card">
<h3>{file_district}</h3>
<p>{file_courthouse}</p>
</div>
{jurisdiction_note}
</div></section>

{exemptions_section}

<section><div class="container">
<h2>Bankruptcy Options</h2>
<div class="compare-grid">
<div class="compare-card"><h3>Chapter 7</h3><p>Eliminates most unsecured debt in 3-4 months. Filing fee: $338. Attorney fees: $900-$1,800.</p><a href="/{city_slug}/chapter-7.html">Chapter 7 guide &rarr;</a></div>
<div class="compare-card"><h3>Chapter 13</h3><p>Keep property, repay over 3-5 years. Filing fee: $313. Attorney fees: $2,500-$4,000.</p><a href="/{city_slug}/chapter-13.html">Chapter 13 guide &rarr;</a></div>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>Where do {suburb_name} residents file for bankruptcy?</summary><div class="answer"><p>{file_district} at {file_courthouse}.</p></div></details>
<details class="faq-item"><summary>How much does bankruptcy cost in {suburb_name}?</summary><div class="answer"><p>Chapter 7: $1,238-$2,188 total. Chapter 13: $2,838-$4,363. <a href="/{city_slug}/cost.html">Full breakdown</a>.</p></div></details>
<details class="faq-item"><summary>What exemptions apply?</summary><div class="answer"><p>{"Mississippi state exemptions only. Homestead: $75,000. Vehicle: $10,000." if is_ms else "Tennessee state or federal exemptions -- your choice. State homestead: $5,000/$7,500. Federal homestead: $27,900."} <a href="/{city_slug}/exemptions.html">Full list</a>.</p></div></details>
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Memphis suburbs
suburb_page("memphis", "Memphis", "germantown", "Germantown, TN", "40,475", "W.D. Tenn.", courthouse)
suburb_page("memphis", "Memphis", "collierville", "Collierville, TN", "52,270", "W.D. Tenn.", courthouse)
suburb_page("memphis", "Memphis", "bartlett", "Bartlett, TN", "60,564", "W.D. Tenn.", courthouse)
suburb_page("memphis", "Memphis", "southaven-ms", "Southaven, MS", "55,026", "N.D. Miss.", "", state_flag="MS")
suburb_page("memphis", "Memphis", "olive-branch-ms", "Olive Branch, MS", "42,305", "N.D. Miss.", "", state_flag="MS")
suburb_page("memphis", "Memphis", "lakeland", "Lakeland, TN", "14,230", "W.D. Tenn.", courthouse)
suburb_page("memphis", "Memphis", "arlington", "Arlington, TN", "13,265", "W.D. Tenn.", courthouse)
suburb_page("memphis", "Memphis", "millington", "Millington, TN", "10,650", "W.D. Tenn.", courthouse)

# =============================================================================
# NASHVILLE (10 pages + 6 suburbs)
# =============================================================================
city = "nashville"
CITY = "Nashville"
district = "M.D. Tenn."
courthouse_nash = "701 Broadway, Nashville, TN 37203"
phone_nash = "(615) 736-5584"
court_url_nash = "tnmb.uscourts.gov"
legal_aid_nash = "Legal Aid Society of Middle Tennessee"

nashville_suburb_links = """<div class="card">
<h3>Nashville Suburb Guides</h3>
<p>Find bankruptcy information for your community in the Nashville metro area:</p>
<div class="network-links" style="margin-top:8px">
<a href="/nashville/suburbs/murfreesboro.html">Murfreesboro</a>
<a href="/nashville/suburbs/franklin.html">Franklin</a>
<a href="/nashville/suburbs/hendersonville.html">Hendersonville</a>
<a href="/nashville/suburbs/gallatin.html">Gallatin</a>
<a href="/nashville/suburbs/lebanon.html">Lebanon</a>
<a href="/nashville/suburbs/clarksville.html">Clarksville</a>
</div>
</div>"""

# Nashville index
write_page("nashville/index.html", f"""{head(
    "Bankruptcy in Nashville, Tennessee -- Complete Guide | Tennessee Bankruptcy Guide",
    "Free 2026 guide to filing bankruptcy in Nashville, TN. Covers Chapter 7, Chapter 13, M.D. Tenn. courthouse, Tennessee exemptions, costs, and Nashville suburb guides.",
    f"https://{DOMAIN}/nashville/",
    [("How much does bankruptcy cost in Nashville?","Chapter 7 filing fees are $338 and Chapter 13 filing fees are $313. Attorney fees in Nashville typically range from $1,000-$2,000 for Chapter 7 and $2,500-$4,500 for Chapter 13."),
     ("Will I lose my house filing bankruptcy in Nashville?","Tennessee offers a $5,000/$7,500 homestead exemption, but Nashville filers can choose federal exemptions ($27,900 homestead) instead."),
     ("Where do Nashville residents file for bankruptcy?","Middle District of Tennessee at 701 Broadway, Nashville, TN 37203."),
     ("How long does bankruptcy take in Nashville?","Chapter 7: 3-4 months. Chapter 13: 3-5 years.")],
    [("Home",f"https://{DOMAIN}"),("Nashville",f"https://{DOMAIN}/nashville/")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Bankruptcy in Nashville, Tennessee</h1>
<p class="subtitle">Nashville residents file in the Middle District of Tennessee. This free guide covers everything Music City residents need to know about filing bankruptcy, from exemptions to costs to what happens after.</p>
<a href="/nashville/faq.html" class="cta" style="margin-right:12px">Read the FAQ</a>
<a href="https://1328f.com" class="cta" style="background:#1f6feb">Check Your Eligibility</a>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card"><div class="number">$5,000 / $7,500</div><div class="label">TN Homestead Exemption</div></div>
<div class="stat-card"><div class="number">3</div><div class="label">TN Federal Districts</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Chapter 7 Filing Fee</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Chapter 13 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13: Which Is Right for You?</h2>
<div class="compare-grid">
<div class="compare-card">
<h3>Chapter 7 -- Fresh Start</h3>
<p>Eliminates most unsecured debts in 3-4 months. Must pass the <a href="https://meanstest.org">means test</a>.</p>
<ul><li>Discharge in 3-4 months</li><li>Eliminates credit cards, medical debt</li><li>Filing fee: $338</li></ul>
<a href="/nashville/chapter-7.html">Learn more about Chapter 7 &rarr;</a>
</div>
<div class="compare-card">
<h3>Chapter 13 -- Payment Plan</h3>
<p>Keep your property while repaying debts over 3-5 years.</p>
<ul><li>3-5 year <a href="https://chapter13plan.org">repayment plan</a></li><li>Keep your home and car</li><li>Filing fee: $313</li></ul>
<a href="/nashville/chapter-13.html">Learn more about Chapter 13 &rarr;</a>
</div>
</div>
<p style="color:#8b949e;font-size:0.9rem;margin-top:8px">Not sure? <a href="https://chapter7vs13.org">Compare them in detail</a>.</p>
</div></section>

<section><div class="container">
<h2>Nashville Courthouse</h2>
<div class="card">
<h3>Middle District of Tennessee -- Nashville Division</h3>
<p>Courthouse: {courthouse_nash}</p>
<p>Phone: {phone_nash} | <a href="https://www.{court_url_nash}" target="_blank" rel="noopener">{court_url_nash}</a></p>
<p>Tennessee uses non-judicial foreclosure, making the <a href="https://automaticstay.org">automatic stay</a> critical for Nashville homeowners facing foreclosure.</p>
</div>
</div></section>

<section><div class="container">
<h2>Tennessee Exemptions at a Glance</h2>
<div class="card">
<p>Tennessee filers can choose between state and federal exemptions. Federal exemptions often provide better protection, especially for homeowners.</p>
{exemption_table()}
<p style="margin-top:12px"><a href="/nashville/exemptions.html">Full exemption details &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>How Much Does Bankruptcy Cost in Nashville?</h2>
<div class="card">
<ul>
<li><strong>Chapter 7 filing fee:</strong> $338</li>
<li><strong>Chapter 13 filing fee:</strong> $313</li>
<li><strong>Attorney fees:</strong> $1,000-$2,000 for Chapter 7; $2,500-$4,500 for Chapter 13</li>
<li><strong>Credit counseling:</strong> $25-$50 total</li>
</ul>
<a href="/nashville/cost.html">Full cost breakdown &rarr;</a> | <a href="https://howmuchdoesbankruptcycost.com">National cost guide</a>
</div>
</div></section>

<section><div class="container">
<h2>Free Legal Resources in Nashville</h2>
<div class="card">
<h3>{legal_aid_nash}</h3>
<p>Phone: (615) 244-6610 | Provides free legal assistance to low-income Nashville residents.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How much does bankruptcy cost in Nashville?</summary><div class="answer"><p>Chapter 7: $1,338-$2,388 total. Chapter 13: $2,838-$4,863. <a href="/nashville/cost.html">Full breakdown</a>.</p></div></details>
<details class="faq-item"><summary>Will I lose my house?</summary><div class="answer"><p>Not if your equity is within exemptions. Federal homestead: $27,900. <a href="/nashville/keep-your-house.html">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>Where do I file in Nashville?</summary><div class="answer"><p>Middle District of Tennessee, {courthouse_nash}. Phone: {phone_nash}.</p></div></details>
<details class="faq-item"><summary>How long does bankruptcy take?</summary><div class="answer"><p>Chapter 7: 3-4 months. Chapter 13: 3-5 years. <a href="https://341meeting.org">341 meeting</a> about 30 days after filing.</p></div></details>
<p style="margin-top:16px"><a href="/nashville/faq.html">See all frequently asked questions &rarr;</a></p>
</div></section>

<div class="container">
{CTA_SECTION}
{nashville_suburb_links}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Nashville topic pages helper
def nash_topic(slug, title_short, title_full, desc, subtitle, body_html, faq_pairs):
    crumbs = [("Home",f"https://{DOMAIN}"),("Nashville",f"https://{DOMAIN}/nashville/"),(title_short,f"https://{DOMAIN}/nashville/{slug}.html")]
    write_page(f"nashville/{slug}.html", f"""{head(
    f"{title_full} | Tennessee Bankruptcy Guide",
    desc,
    f"https://{DOMAIN}/nashville/{slug}.html",
    faq_pairs,
    crumbs
)}
<body>
{nav("nashville")}
<div class="hero"><div class="container">
<h1>{title_full}</h1>
<p class="subtitle">{subtitle}</p>
</div></div>
{body_html}
<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Nashville chapter-7
nash_topic("chapter-7", "Chapter 7",
    "Chapter 7 Bankruptcy in Nashville",
    "Complete guide to Chapter 7 bankruptcy in Nashville, TN. Means test, Tennessee exemptions, timeline, and what to expect in M.D. Tenn.",
    "Chapter 7 eliminates most unsecured debts in 3-4 months. Here is what Nashville residents need to know.",
    f"""<section><div class="container">
<h2>What Is Chapter 7?</h2>
<div class="card">
<p>Chapter 7 eliminates most unsecured debts (credit cards, medical bills, personal loans). A trustee reviews your assets, but most Nashville cases are "no-asset" -- you keep everything within <a href="/nashville/exemptions.html">exemption limits</a>.</p>
</div>
</div></section>
<section><div class="container">
<h2>Debts Chapter 7 Eliminates</h2>
<div class="compare-grid">
<div class="compare-card" style="border-color:#3fb950"><h3 style="color:#3fb950">Dischargeable</h3><ul><li>Credit card debt</li><li>Medical bills</li><li>Personal loans</li><li>Utility bills</li><li>Some older tax debts</li></ul></div>
<div class="compare-card" style="border-color:#f85149"><h3 style="color:#f85149">NOT Dischargeable</h3><ul><li>Student loans (usually)</li><li>Recent taxes</li><li>Child support / alimony</li><li>Debts from fraud</li><li>Criminal fines</li></ul></div>
</div>
</div></section>
<section><div class="container">
<h2>Nashville Means Test</h2>
<div class="card">
<p>The <a href="https://meanstest.org">means test</a> compares your income to Tennessee's median. <a href="/nashville/means-test.html">Full means test guide</a>.</p>
<table>
<thead><tr><th>Household</th><th>Annual Median</th></tr></thead>
<tbody>
<tr><td>1 person</td><td style="color:#3fb950;font-weight:700">$53,697</td></tr>
<tr><td>2 persons</td><td style="color:#3fb950;font-weight:700">$67,854</td></tr>
<tr><td>3 persons</td><td style="color:#3fb950;font-weight:700">$77,379</td></tr>
<tr><td>4 persons</td><td style="color:#3fb950;font-weight:700">$94,416</td></tr>
</tbody></table>
</div>
</div></section>
<section><div class="container">
<h2>Chapter 7 Timeline</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Credit counseling</strong></div>
<div class="step"><span class="step-number">2</span><strong>File petition</strong> at M.D. Tenn., {courthouse_nash}</div>
<div class="step"><span class="step-number">3</span><strong><a href="https://341meeting.org">341 meeting</a></strong> -- ~30 days after filing</div>
<div class="step"><span class="step-number">4</span><strong>Financial management course</strong></div>
<div class="step"><span class="step-number">5</span><strong>Discharge</strong> -- 3-4 months total</div>
</div>
</div></section>""",
    [("What debts does Chapter 7 eliminate?","Credit cards, medical bills, personal loans, utility bills, and some older tax debts. Not student loans, child support, or recent taxes."),
     ("How long does Chapter 7 take in Nashville?","3-4 months from filing to discharge."),
     ("What is the means test?","A comparison of your income to Tennessee's median. Below median = automatic qualification.")])

# Nashville chapter-13
nash_topic("chapter-13", "Chapter 13",
    "Chapter 13 Bankruptcy in Nashville",
    "Guide to Chapter 13 bankruptcy in Nashville. Repayment plan, timeline, how to save your home and car in M.D. Tenn.",
    "Chapter 13 lets you keep your property while repaying debts over 3-5 years. Here is what Nashville filers need to know.",
    f"""<section><div class="container">
<h2>How Chapter 13 Works</h2>
<div class="card">
<p>You propose a repayment plan paying back some or all debts over 3-5 years. Monthly payments go to a trustee. Useful for saving homes from foreclosure and catching up on car payments.</p>
<ul>
<li><strong>Save your home</strong> -- catch up on mortgage arrears</li>
<li><strong><a href="/nashville/keep-your-car.html">Keep your car</a></strong> -- cure defaults</li>
<li><strong>Stop garnishments</strong> -- <a href="https://automaticstay.org">automatic stay</a> halts collections</li>
</ul>
</div>
</div></section>
<section><div class="container">
<h2>Chapter 13 Timeline</h2>
<div class="card">
<div class="step"><span class="step-number">1</span><strong>Credit counseling + file petition</strong></div>
<div class="step"><span class="step-number">2</span><strong>Begin payments within 30 days</strong></div>
<div class="step"><span class="step-number">3</span><strong>341 meeting</strong> (20-50 days after filing)</div>
<div class="step"><span class="step-number">4</span><strong>Confirmation hearing</strong></div>
<div class="step"><span class="step-number">5</span><strong>3-5 years of plan payments</strong></div>
<div class="step"><span class="step-number">6</span><strong>Discharge</strong></div>
</div>
</div></section>""",
    [("What is Chapter 13?","A repayment plan over 3-5 years that lets you keep property while paying back some debts."),
     ("Can I save my house in Chapter 13?","Yes. The automatic stay stops foreclosure and your plan can include catch-up payments."),
     ("How long is a Chapter 13 plan?","3 years if below median income, 5 years if above.")])

# Nashville exemptions
nash_topic("exemptions", "Exemptions",
    "Nashville Bankruptcy Exemptions -- State vs Federal",
    "Tennessee bankruptcy exemptions for Nashville filers. Compare state ($5,000 homestead) with federal ($27,900 homestead).",
    "Tennessee lets you choose between state and federal exemptions. Compare both to protect the most property.",
    f"""<section><div class="container">
<h2>State vs. Federal Exemptions</h2>
<div class="card">
<p>Tennessee allows filers to choose between state and federal exemptions. You must pick one system -- no mixing.</p>
{exemption_table()}
<div class="quick-answer">For most Nashville homeowners, federal exemptions protect significantly more home equity ($27,900 vs $5,000/$7,500).</div>
</div>
</div></section>""",
    [("What is the homestead exemption in Tennessee?","State: $5,000/$7,500. Federal: $27,900. You can choose which system to use."),
     ("Can I choose federal exemptions in Tennessee?","Yes. Tennessee is one of the states that allows this choice."),
     ("What is the wildcard exemption?","State: $10,000 for any property. Federal: $1,475 + up to $13,950 of unused homestead.")])

# Nashville cost
nash_topic("cost", "Cost",
    "How Much Does Bankruptcy Cost in Nashville?",
    "Cost breakdown for filing bankruptcy in Nashville, TN. Filing fees, attorney fees, and ways to reduce costs.",
    "A complete breakdown of bankruptcy costs for Nashville residents.",
    f"""<section><div class="container">
<h2>Cost Breakdown</h2>
<div class="card">
<table>
<thead><tr><th>Expense</th><th>Chapter 7</th><th>Chapter 13</th></tr></thead>
<tbody>
<tr><td>Court filing fee</td><td>$338</td><td>$313</td></tr>
<tr><td>Attorney fees (typical)</td><td>$1,000 - $2,000</td><td>$2,500 - $4,500</td></tr>
<tr><td>Credit counseling</td><td>$25 - $50</td><td>$25 - $50</td></tr>
<tr><td><strong>Total</strong></td><td><strong>$1,363 - $2,388</strong></td><td><strong>$2,838 - $4,863</strong></td></tr>
</tbody></table>
</div>
</div></section>
<section><div class="container">
<h2>Ways to Reduce Costs</h2>
<div class="card">
<ul>
<li><strong>Fee waiver (Ch. 7):</strong> Income below 150% of poverty guidelines</li>
<li><strong>Installment payments:</strong> Pay filing fee over time</li>
<li><strong>Ch. 13 fees through plan:</strong> Attorney fees paid through repayment plan</li>
<li><strong>Legal aid:</strong> {legal_aid_nash} at (615) 244-6610</li>
</ul>
</div>
{DISCLAIMER}
</div></section>""",
    [("How much does Chapter 7 cost in Nashville?","$1,363-$2,388 total including filing fee ($338), attorney ($1,000-$2,000), and counseling."),
     ("How much does Chapter 13 cost in Nashville?","$2,838-$4,863 total. Attorney fees can be paid through your repayment plan."),
     ("Can I get a fee waiver?","Chapter 7 filers below 150% of poverty guidelines may qualify.")])

# Nashville FAQ
nash_topic("faq", "FAQ",
    "Nashville Bankruptcy FAQ -- Common Questions Answered",
    "Frequently asked questions about filing bankruptcy in Nashville. Costs, exemptions, 341 meeting, timeline.",
    "Answers to common questions about filing bankruptcy in Nashville, Tennessee.",
    f"""<section><div class="container">
<details class="faq-item"><summary>How much does bankruptcy cost in Nashville?</summary><div class="answer"><p>Chapter 7: $1,363-$2,388. Chapter 13: $2,838-$4,863. <a href="/nashville/cost.html">Full breakdown</a>.</p></div></details>
<details class="faq-item"><summary>Where do I file in Nashville?</summary><div class="answer"><p>Middle District of Tennessee, {courthouse_nash}. Phone: {phone_nash}.</p></div></details>
<details class="faq-item"><summary>Will I lose my house?</summary><div class="answer"><p>Usually not. Federal homestead exemption is $27,900. <a href="/nashville/keep-your-house.html">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>Will I lose my car?</summary><div class="answer"><p>Usually not. Tennessee's $10,000 wildcard covers most vehicles. <a href="/nashville/keep-your-car.html">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>What is the means test?</summary><div class="answer"><p>Compares your income to Tennessee's median. Below = qualify for Chapter 7. <a href="/nashville/means-test.html">Details</a>.</p></div></details>
<details class="faq-item"><summary>How long does bankruptcy take?</summary><div class="answer"><p>Chapter 7: 3-4 months. Chapter 13: 3-5 years.</p></div></details>
<details class="faq-item"><summary>What is the automatic stay?</summary><div class="answer"><p>Court order stopping foreclosure, repossession, garnishment, and collection actions. <a href="https://automaticstay.org">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>Can I file again?</summary><div class="answer"><p>Yes, with timing limits. Ch 7 to Ch 7: 8 years. Ch 13 to Ch 13: 2 years. <a href="https://1328f.com">Check eligibility</a>.</p></div></details>
<details class="faq-item"><summary>How long does bankruptcy stay on my credit?</summary><div class="answer"><p>Chapter 7: 10 years. Chapter 13: 7 years.</p></div></details>
<details class="faq-item"><summary>Should I file Chapter 7 or Chapter 13?</summary><div class="answer"><p>Depends on income, assets, and goals. <a href="https://chapter7vs13.org">Compare chapters</a>.</p></div></details>
</div></section>""",
    [("How much does bankruptcy cost in Nashville?","Chapter 7: $1,363-$2,388 total. Chapter 13: $2,838-$4,863 total."),
     ("Where do Nashville residents file?","Middle District of Tennessee, 701 Broadway, Nashville, TN 37203."),
     ("How long does bankruptcy take?","Chapter 7: 3-4 months. Chapter 13: 3-5 years.")])

# Nashville means-test
nash_topic("means-test", "Means Test",
    "Nashville Means Test -- Do You Qualify for Chapter 7?",
    "How the bankruptcy means test works for Nashville residents. Tennessee median income and step-by-step walkthrough.",
    "The means test determines Chapter 7 eligibility by comparing your income to Tennessee's state median.",
    f"""<section><div class="container">
<h2>2026 Tennessee Median Income</h2>
<div class="card"><table>
<thead><tr><th>Household</th><th>Annual</th><th>Monthly</th></tr></thead>
<tbody>
<tr><td>1 person</td><td style="color:#3fb950;font-weight:700">$53,697</td><td>$4,475</td></tr>
<tr><td>2 persons</td><td style="color:#3fb950;font-weight:700">$67,854</td><td>$5,655</td></tr>
<tr><td>3 persons</td><td style="color:#3fb950;font-weight:700">$77,379</td><td>$6,448</td></tr>
<tr><td>4 persons</td><td style="color:#3fb950;font-weight:700">$94,416</td><td>$7,868</td></tr>
</tbody></table>
<p style="margin-top:12px">Add $9,900 for each person beyond 4. Full details at <a href="https://meanstest.org">meanstest.org</a>.</p>
</div>
</div></section>""",
    [("What is the means test?","Compares your income to Tennessee's median. Below = automatic Chapter 7 qualification."),
     ("What is the Tennessee median income?","Single: $53,697. 2-person: $67,854. 3-person: $77,379. 4-person: $94,416."),
     ("What if I fail?","File Chapter 13, wait for income to drop, or claim special circumstances.")])

# Nashville keep-your-car
nash_topic("keep-your-car", "Keep Your Car",
    "Can You Keep Your Car in Nashville Bankruptcy?",
    "Protect your vehicle in Nashville bankruptcy. Tennessee exemptions, reaffirmation, and redemption options.",
    "Most Nashville residents can keep their car in bankruptcy. Here is how.",
    f"""<section><div class="container">
<h2>Vehicle Exemptions</h2>
<div class="card">
<table>
<tr><th>System</th><th>Vehicle Protection</th></tr>
<tr><td>Tennessee state</td><td>$10,000 wildcard</td></tr>
<tr><td>Federal</td><td>$4,450 vehicle + $1,475 wildcard + up to $13,950 unused homestead</td></tr>
</table>
</div>
</div></section>
<section><div class="container">
<h2>Options for Cars with Loans</h2>
<div class="card">
<ul>
<li><strong>Reaffirmation:</strong> Keep paying, keep the car</li>
<li><strong>Redemption:</strong> Pay current value in lump sum</li>
<li><strong>Surrender:</strong> Return car, discharge remaining debt</li>
<li><strong>Chapter 13 cramdown:</strong> Reduce balance to current value (loan must be 910+ days old)</li>
</ul>
</div>
</div></section>""",
    [("Can I keep my car?","Usually yes. Tennessee's $10,000 wildcard protects most vehicles."),
     ("What if I still owe on the car?","Reaffirm the loan, redeem at current value, or surrender and discharge the debt.")])

# Nashville keep-your-house
nash_topic("keep-your-house", "Keep Your House",
    "Can You Keep Your House in Nashville Bankruptcy?",
    "Protect your home in Nashville bankruptcy. Tennessee vs federal homestead exemption. Non-judicial foreclosure.",
    "Tennessee has a low state homestead exemption, but you can choose federal exemptions for much better protection.",
    f"""<section><div class="container">
<h2>Homestead Exemption Comparison</h2>
<div class="card">
<table>
<tr><th>System</th><th>Protection</th></tr>
<tr><td>TN state (individual)</td><td>$5,000</td></tr>
<tr><td>TN state (family/62+)</td><td>$7,500</td></tr>
<tr><td>Federal</td><td>$27,900</td></tr>
</table>
<div class="quick-answer">Federal exemptions protect over 5x more equity. Most Nashville homeowners should choose federal.</div>
</div>
</div></section>
<section><div class="container">
<h2>Non-Judicial Foreclosure</h2>
<div class="card" style="border-color:#d29922">
<p>Tennessee is a non-judicial foreclosure state. The <a href="https://automaticstay.org">automatic stay</a> is your strongest defense against foreclosure.</p>
</div>
</div></section>""",
    [("Will I lose my house?","Not if equity is within exemptions. Federal: $27,900."),
     ("Is Tennessee non-judicial foreclosure?","Yes. The automatic stay is critical for stopping foreclosure."),
     ("State or federal for my home?","Usually federal -- $27,900 vs $5,000/$7,500.")])

# Nashville 341-meeting
nash_topic("341-meeting", "341 Meeting",
    "The 341 Meeting in Nashville -- What to Expect",
    "What to expect at your 341 meeting in Nashville. How to prepare, what to bring, and common questions.",
    "The 341 meeting of creditors is a brief hearing about 30 days after filing. Here is what Nashville filers need to know.",
    f"""<section><div class="container">
<h2>What Is the 341 Meeting?</h2>
<div class="card">
<p>The <a href="https://341meeting.org">341 meeting of creditors</a> is a required hearing where you answer questions under oath. Conducted by the trustee, not a judge. Typically lasts 5-10 minutes.</p>
</div>
</div></section>
<section><div class="container">
<h2>Where and When</h2>
<div class="card">
<p><strong>Location:</strong> Near the M.D. Tenn. courthouse at {courthouse_nash}.</p>
<p><strong>Timing:</strong> 20-40 days after filing.</p>
</div>
</div></section>
<section><div class="container">
<h2>What to Bring</h2>
<div class="card">
<ul>
<li>Government-issued photo ID</li>
<li>Social Security card or proof of SSN</li>
<li>Recent pay stubs (last 60 days)</li>
<li>Most recent tax return</li>
<li>Bank statements (last 2-3 months)</li>
</ul>
</div>
</div></section>""",
    [("What is the 341 meeting?","A brief hearing where the trustee asks questions about your finances under oath."),
     ("How long does it last?","Typically 5-10 minutes."),
     ("Do creditors attend?","They can, but rarely do in consumer cases.")])

# Nashville suburbs
suburb_page("nashville", "Nashville", "murfreesboro", "Murfreesboro, TN", "163,377", "M.D. Tenn.", courthouse_nash)
suburb_page("nashville", "Nashville", "franklin", "Franklin, TN", "87,521", "M.D. Tenn.", courthouse_nash)
suburb_page("nashville", "Nashville", "hendersonville", "Hendersonville, TN", "61,753", "M.D. Tenn.", courthouse_nash)
suburb_page("nashville", "Nashville", "gallatin", "Gallatin, TN", "45,616", "M.D. Tenn.", courthouse_nash)
suburb_page("nashville", "Nashville", "lebanon", "Lebanon, TN", "41,277", "M.D. Tenn.", courthouse_nash)
suburb_page("nashville", "Nashville", "clarksville", "Clarksville, TN", "166,722", "M.D. Tenn.", courthouse_nash)

# =============================================================================
# KNOXVILLE (5 pages)
# =============================================================================
city = "knoxville"
courthouse_knox = "800 Market St, Suite 330, Knoxville, TN 37902"
phone_knox = "(865) 545-4279"
court_url_knox = "tneb.uscourts.gov"

# Knoxville index
write_page("knoxville/index.html", f"""{head(
    "Bankruptcy in Knoxville, Tennessee -- Complete Guide | Tennessee Bankruptcy Guide",
    "Free 2026 guide to filing bankruptcy in Knoxville, TN. Covers Chapter 7, Chapter 13, E.D. Tenn. courthouse, Tennessee exemptions, and costs.",
    f"https://{DOMAIN}/knoxville/",
    [("How much does bankruptcy cost in Knoxville?","Chapter 7: $338 filing + $900-$1,800 attorney. Chapter 13: $313 filing + $2,500-$4,000 attorney."),
     ("Where do Knoxville residents file?","Eastern District of Tennessee at 800 Market St, Suite 330, Knoxville, TN 37902."),
     ("What exemptions apply in Knoxville?","Tennessee state or federal -- filer's choice. State homestead: $5,000/$7,500. Federal: $27,900."),
     ("How long does bankruptcy take in Knoxville?","Chapter 7: 3-4 months. Chapter 13: 3-5 years.")],
    [("Home",f"https://{DOMAIN}"),("Knoxville",f"https://{DOMAIN}/knoxville/")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Bankruptcy in Knoxville, Tennessee</h1>
<p class="subtitle">Knoxville residents file in the Eastern District of Tennessee. This free guide covers Chapter 7, Chapter 13, Tennessee exemptions, costs, and what to expect when filing in East Tennessee.</p>
<a href="/knoxville/faq.html" class="cta" style="margin-right:12px">Read the FAQ</a>
<a href="https://1328f.com" class="cta" style="background:#1f6feb">Check Your Eligibility</a>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card"><div class="number">$5,000 / $7,500</div><div class="label">TN Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$27,900</div><div class="label">Federal Homestead Option</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Chapter 7 Filing Fee</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Chapter 13 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13</h2>
<div class="compare-grid">
<div class="compare-card"><h3>Chapter 7 -- Fresh Start</h3><p>Eliminates most unsecured debts in 3-4 months. Must pass the <a href="https://meanstest.org">means test</a>. Filing fee: $338.</p><a href="/knoxville/chapter-7.html">Chapter 7 guide &rarr;</a></div>
<div class="compare-card"><h3>Chapter 13 -- Payment Plan</h3><p>Keep property, repay over 3-5 years. No means test. Filing fee: $313.</p><a href="/knoxville/chapter-13.html">Chapter 13 guide &rarr;</a></div>
</div>
</div></section>

<section><div class="container">
<h2>Knoxville Courthouse</h2>
<div class="card">
<h3>Eastern District of Tennessee -- Knoxville Division</h3>
<p>Courthouse: {courthouse_knox}</p>
<p>Phone: {phone_knox} | <a href="https://www.{court_url_knox}" target="_blank" rel="noopener">{court_url_knox}</a></p>
<p>The Eastern District also covers Chattanooga (separate division). Knoxville residents file in the Knoxville division.</p>
</div>
</div></section>

<section><div class="container">
<h2>Tennessee Exemptions</h2>
<div class="card">
<p>Tennessee lets you choose state or federal exemptions. Federal homestead ($27,900) is much higher than state ($5,000/$7,500).</p>
{exemption_table()}
<p style="margin-top:12px"><a href="/knoxville/exemptions.html">Full exemption details &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Free Legal Resources</h2>
<div class="card">
<h3>Legal Aid of East Tennessee</h3>
<p>Phone: (865) 637-0484 | Free legal assistance for low-income East Tennessee residents.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How much does bankruptcy cost in Knoxville?</summary><div class="answer"><p>Chapter 7: $1,238-$2,188 total. Chapter 13: $2,838-$4,363. <a href="https://howmuchdoesbankruptcycost.com">National cost guide</a>.</p></div></details>
<details class="faq-item"><summary>Where do I file in Knoxville?</summary><div class="answer"><p>Eastern District of Tennessee, {courthouse_knox}.</p></div></details>
<details class="faq-item"><summary>State or federal exemptions?</summary><div class="answer"><p>Compare both. Federal homestead ($27,900) is much higher. <a href="/knoxville/exemptions.html">Details</a>.</p></div></details>
<p style="margin-top:16px"><a href="/knoxville/faq.html">See all FAQ &rarr;</a></p>
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

# Knoxville topic pages
def knox_topic(slug, title_short, title_full, desc, subtitle, body_html, faq_pairs):
    crumbs = [("Home",f"https://{DOMAIN}"),("Knoxville",f"https://{DOMAIN}/knoxville/"),(title_short,f"https://{DOMAIN}/knoxville/{slug}.html")]
    write_page(f"knoxville/{slug}.html", f"""{head(
    f"{title_full} | Tennessee Bankruptcy Guide",
    desc,
    f"https://{DOMAIN}/knoxville/{slug}.html",
    faq_pairs,
    crumbs
)}
<body>
{nav("knoxville")}
<div class="hero"><div class="container">
<h1>{title_full}</h1>
<p class="subtitle">{subtitle}</p>
</div></div>
{body_html}
<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

knox_topic("chapter-7", "Chapter 7",
    "Chapter 7 Bankruptcy in Knoxville",
    "Guide to Chapter 7 in Knoxville, TN. Means test, exemptions, timeline in E.D. Tenn.",
    "Chapter 7 eliminates most unsecured debts in 3-4 months. Here is what Knoxville residents need to know.",
    f"""<section><div class="container">
<h2>What Is Chapter 7?</h2>
<div class="card"><p>Chapter 7 eliminates credit cards, medical bills, and personal loans. Most Knoxville filers keep all property within <a href="/knoxville/exemptions.html">exemption limits</a>.</p></div>
</div></section>
<section><div class="container">
<h2>Knoxville Means Test</h2>
<div class="card"><table>
<thead><tr><th>Household</th><th>Annual Median</th></tr></thead>
<tbody>
<tr><td>1</td><td style="color:#3fb950;font-weight:700">$53,697</td></tr>
<tr><td>2</td><td style="color:#3fb950;font-weight:700">$67,854</td></tr>
<tr><td>3</td><td style="color:#3fb950;font-weight:700">$77,379</td></tr>
<tr><td>4</td><td style="color:#3fb950;font-weight:700">$94,416</td></tr>
</tbody></table></div>
</div></section>
<section><div class="container">
<h2>Timeline</h2>
<div class="card">
<div class="step"><span class="step-number">1</span>Credit counseling</div>
<div class="step"><span class="step-number">2</span>File at E.D. Tenn., {courthouse_knox}</div>
<div class="step"><span class="step-number">3</span><a href="https://341meeting.org">341 meeting</a> (~30 days)</div>
<div class="step"><span class="step-number">4</span>Financial management course</div>
<div class="step"><span class="step-number">5</span>Discharge (3-4 months)</div>
</div>
</div></section>""",
    [("How long does Chapter 7 take in Knoxville?","3-4 months."),
     ("What is the means test?","Compares income to Tennessee median. Below = qualify for Chapter 7."),
     ("What debts are eliminated?","Credit cards, medical bills, personal loans, utility bills.")])

knox_topic("chapter-13", "Chapter 13",
    "Chapter 13 Bankruptcy in Knoxville",
    "Guide to Chapter 13 in Knoxville, TN. Repayment plan, save your home, E.D. Tenn. filing.",
    "Chapter 13 lets you keep property while repaying debts over 3-5 years.",
    f"""<section><div class="container">
<h2>How Chapter 13 Works</h2>
<div class="card">
<p>Propose a repayment plan over 3-5 years. Keep your home and car while catching up on arrears. No means test.</p>
<ul><li>Save your home from foreclosure</li><li>Keep your car and cure defaults</li><li>Stop wage garnishment via <a href="https://automaticstay.org">automatic stay</a></li><li>Filing fee: $313</li></ul>
</div>
</div></section>
<section><div class="container">
<h2>Tennessee Non-Judicial Foreclosure</h2>
<div class="card" style="border-color:#d29922"><p>Tennessee is a non-judicial foreclosure state. Chapter 13's automatic stay is the most effective tool to stop foreclosure in Knoxville.</p></div>
</div></section>""",
    [("What is Chapter 13?","A 3-5 year repayment plan. Keep property while paying debts."),
     ("Can I save my house?","Yes. Automatic stay stops foreclosure. Plan can include catch-up payments."),
     ("How long is the plan?","3 years (below median income) or 5 years (above median).")])

knox_topic("exemptions", "Exemptions",
    "Knoxville Bankruptcy Exemptions -- State vs Federal",
    "Tennessee exemptions for Knoxville filers. State vs federal comparison.",
    "Tennessee lets you choose state or federal exemptions. Compare to protect the most property.",
    f"""<section><div class="container">
<h2>Exemption Comparison</h2>
<div class="card">
{exemption_table()}
<div class="quick-answer">For homeowners: federal ($27,900) beats state ($5,000/$7,500). For renters with personal property: state's $10,000 wildcard may be better.</div>
</div>
</div></section>""",
    [("What is the homestead exemption?","State: $5,000/$7,500. Federal: $27,900. Your choice."),
     ("Can I choose federal exemptions?","Yes. Tennessee allows this."),
     ("What about my car?","State: $10,000 wildcard. Federal: $4,450 vehicle + $1,475 wildcard.")])

knox_topic("faq", "FAQ",
    "Knoxville Bankruptcy FAQ",
    "Common questions about filing bankruptcy in Knoxville, TN. E.D. Tenn. courthouse, exemptions, costs.",
    "Answers to common questions about filing bankruptcy in Knoxville.",
    f"""<section><div class="container">
<details class="faq-item"><summary>Where do I file in Knoxville?</summary><div class="answer"><p>Eastern District of Tennessee, {courthouse_knox}. Phone: {phone_knox}.</p></div></details>
<details class="faq-item"><summary>How much does bankruptcy cost?</summary><div class="answer"><p>Chapter 7: $1,238-$2,188. Chapter 13: $2,838-$4,363.</p></div></details>
<details class="faq-item"><summary>State or federal exemptions?</summary><div class="answer"><p>Tennessee lets you choose. Federal homestead ($27,900) is usually better for homeowners. <a href="/knoxville/exemptions.html">Details</a>.</p></div></details>
<details class="faq-item"><summary>How long does bankruptcy take?</summary><div class="answer"><p>Chapter 7: 3-4 months. Chapter 13: 3-5 years.</p></div></details>
<details class="faq-item"><summary>What is the 341 meeting?</summary><div class="answer"><p>Brief hearing with the trustee ~30 days after filing. <a href="https://341meeting.org">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>Can I file again?</summary><div class="answer"><p>Yes, with timing rules. <a href="https://1328f.com">Check eligibility</a>.</p></div></details>
</div></section>""",
    [("Where do Knoxville residents file?","E.D. Tenn., 800 Market St, Suite 330, Knoxville, TN 37902."),
     ("How much does bankruptcy cost in Knoxville?","Chapter 7: $1,238-$2,188. Chapter 13: $2,838-$4,363."),
     ("What exemptions apply?","Tennessee state or federal -- your choice.")])

# =============================================================================
# CHATTANOOGA (5 pages)
# =============================================================================
city = "chattanooga"
courthouse_chatt = "900 Georgia Ave, Suite 109, Chattanooga, TN 37402"
phone_chatt = "(423) 752-5163"

write_page("chattanooga/index.html", f"""{head(
    "Bankruptcy in Chattanooga, Tennessee -- Complete Guide | Tennessee Bankruptcy Guide",
    "Free 2026 guide to filing bankruptcy in Chattanooga, TN. Chapter 7, Chapter 13, E.D. Tenn. courthouse, Tennessee exemptions, and costs.",
    f"https://{DOMAIN}/chattanooga/",
    [("How much does bankruptcy cost in Chattanooga?","Chapter 7: $338 filing + $900-$1,800 attorney. Chapter 13: $313 filing + $2,500-$4,000 attorney."),
     ("Where do Chattanooga residents file?","Eastern District of Tennessee, Chattanooga Division, at 900 Georgia Ave, Suite 109, Chattanooga, TN 37402."),
     ("What exemptions apply?","Tennessee state or federal -- filer's choice."),
     ("How long does bankruptcy take?","Chapter 7: 3-4 months. Chapter 13: 3-5 years.")],
    [("Home",f"https://{DOMAIN}"),("Chattanooga",f"https://{DOMAIN}/chattanooga/")]
)}
<body>
{nav(city)}
<div class="hero"><div class="container">
<h1>Bankruptcy in Chattanooga, Tennessee</h1>
<p class="subtitle">Chattanooga residents file in the Eastern District of Tennessee, Chattanooga Division. This free guide covers Chapter 7, Chapter 13, Tennessee exemptions, costs, and what to expect.</p>
<a href="/chattanooga/faq.html" class="cta" style="margin-right:12px">Read the FAQ</a>
<a href="https://1328f.com" class="cta" style="background:#1f6feb">Check Your Eligibility</a>
</div></div>

<div class="container">
<div class="stats-row">
<div class="stat-card"><div class="number">$5,000 / $7,500</div><div class="label">TN Homestead Exemption</div></div>
<div class="stat-card"><div class="number">$27,900</div><div class="label">Federal Homestead Option</div></div>
<div class="stat-card"><div class="number">$338</div><div class="label">Chapter 7 Filing Fee</div></div>
<div class="stat-card"><div class="number">$313</div><div class="label">Chapter 13 Filing Fee</div></div>
</div>
</div>

<section><div class="container">
<h2>Chapter 7 vs. Chapter 13</h2>
<div class="compare-grid">
<div class="compare-card"><h3>Chapter 7 -- Fresh Start</h3><p>Eliminates most unsecured debts in 3-4 months. Must pass the <a href="https://meanstest.org">means test</a>. Filing fee: $338.</p><a href="/chattanooga/chapter-7.html">Chapter 7 guide &rarr;</a></div>
<div class="compare-card"><h3>Chapter 13 -- Payment Plan</h3><p>Keep property, repay over 3-5 years. No means test. Filing fee: $313.</p><a href="/chattanooga/chapter-13.html">Chapter 13 guide &rarr;</a></div>
</div>
</div></section>

<section><div class="container">
<h2>Chattanooga Courthouse</h2>
<div class="card">
<h3>Eastern District of Tennessee -- Chattanooga Division</h3>
<p>Courthouse: {courthouse_chatt}</p>
<p>Phone: {phone_chatt} | <a href="https://www.tneb.uscourts.gov" target="_blank" rel="noopener">tneb.uscourts.gov</a></p>
<p>Part of the Eastern District of Tennessee. Chattanooga has its own division separate from the Knoxville division.</p>
</div>
</div></section>

<section><div class="container">
<h2>Tennessee Exemptions</h2>
<div class="card">
<p>Choose state or federal exemptions. Federal homestead ($27,900) is typically better for homeowners.</p>
{exemption_table()}
<p style="margin-top:12px"><a href="/chattanooga/exemptions.html">Full exemption details &rarr;</a></p>
</div>
</div></section>

<section><div class="container">
<h2>Free Legal Resources</h2>
<div class="card">
<h3>Legal Aid of East Tennessee -- Chattanooga Office</h3>
<p>Phone: (423) 756-4013 | Free legal assistance for low-income Chattanooga residents.</p>
</div>
</div></section>

<section><div class="container">
<h2>Frequently Asked Questions</h2>
<details class="faq-item"><summary>How much does bankruptcy cost in Chattanooga?</summary><div class="answer"><p>Chapter 7: $1,238-$2,188 total. Chapter 13: $2,838-$4,363.</p></div></details>
<details class="faq-item"><summary>Where do I file?</summary><div class="answer"><p>E.D. Tenn. Chattanooga Division, {courthouse_chatt}.</p></div></details>
<details class="faq-item"><summary>State or federal exemptions?</summary><div class="answer"><p>Your choice. Federal homestead is $27,900 vs state $5,000/$7,500. <a href="/chattanooga/exemptions.html">Compare</a>.</p></div></details>
<p style="margin-top:16px"><a href="/chattanooga/faq.html">See all FAQ &rarr;</a></p>
</div></section>

<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

def chatt_topic(slug, title_short, title_full, desc, subtitle, body_html, faq_pairs):
    crumbs = [("Home",f"https://{DOMAIN}"),("Chattanooga",f"https://{DOMAIN}/chattanooga/"),(title_short,f"https://{DOMAIN}/chattanooga/{slug}.html")]
    write_page(f"chattanooga/{slug}.html", f"""{head(
    f"{title_full} | Tennessee Bankruptcy Guide",
    desc,
    f"https://{DOMAIN}/chattanooga/{slug}.html",
    faq_pairs,
    crumbs
)}
<body>
{nav("chattanooga")}
<div class="hero"><div class="container">
<h1>{title_full}</h1>
<p class="subtitle">{subtitle}</p>
</div></div>
{body_html}
<div class="container">
{CTA_SECTION}
{OBP_NETWORK}
</div>
{FOOTER}
</body>
</html>
""")

chatt_topic("chapter-7", "Chapter 7",
    "Chapter 7 Bankruptcy in Chattanooga",
    "Guide to Chapter 7 in Chattanooga, TN. Means test, exemptions, timeline in E.D. Tenn.",
    "Chapter 7 eliminates most unsecured debts in 3-4 months. Here is what Chattanooga residents need to know.",
    f"""<section><div class="container">
<h2>What Is Chapter 7?</h2>
<div class="card"><p>Chapter 7 eliminates credit cards, medical bills, and personal loans. Most Chattanooga filers keep all property within <a href="/chattanooga/exemptions.html">exemption limits</a>.</p></div>
</div></section>
<section><div class="container">
<h2>Means Test</h2>
<div class="card"><table>
<thead><tr><th>Household</th><th>Annual Median</th></tr></thead>
<tbody>
<tr><td>1</td><td style="color:#3fb950;font-weight:700">$53,697</td></tr>
<tr><td>2</td><td style="color:#3fb950;font-weight:700">$67,854</td></tr>
<tr><td>3</td><td style="color:#3fb950;font-weight:700">$77,379</td></tr>
<tr><td>4</td><td style="color:#3fb950;font-weight:700">$94,416</td></tr>
</tbody></table></div>
</div></section>
<section><div class="container">
<h2>Timeline</h2>
<div class="card">
<div class="step"><span class="step-number">1</span>Credit counseling</div>
<div class="step"><span class="step-number">2</span>File at E.D. Tenn. Chattanooga, {courthouse_chatt}</div>
<div class="step"><span class="step-number">3</span><a href="https://341meeting.org">341 meeting</a> (~30 days)</div>
<div class="step"><span class="step-number">4</span>Financial management course</div>
<div class="step"><span class="step-number">5</span>Discharge (3-4 months)</div>
</div>
</div></section>""",
    [("How long does Chapter 7 take?","3-4 months."),
     ("What is the means test?","Compares income to Tennessee median."),
     ("What debts are eliminated?","Credit cards, medical bills, personal loans.")])

chatt_topic("chapter-13", "Chapter 13",
    "Chapter 13 Bankruptcy in Chattanooga",
    "Guide to Chapter 13 in Chattanooga, TN. Repayment plan, save your home, E.D. Tenn. Chattanooga Division.",
    "Chapter 13 lets you keep property while repaying debts over 3-5 years.",
    f"""<section><div class="container">
<h2>How Chapter 13 Works</h2>
<div class="card">
<p>Propose a repayment plan over 3-5 years. Keep your home and car while catching up on arrears.</p>
<ul><li>Save your home from foreclosure</li><li>Keep your car and cure defaults</li><li>Stop wage garnishment via <a href="https://automaticstay.org">automatic stay</a></li><li>Filing fee: $313</li></ul>
</div>
</div></section>
<section><div class="container">
<h2>Non-Judicial Foreclosure</h2>
<div class="card" style="border-color:#d29922"><p>Tennessee is a non-judicial foreclosure state. Chapter 13's automatic stay is your strongest defense against losing your home.</p></div>
</div></section>""",
    [("What is Chapter 13?","A 3-5 year repayment plan keeping your property."),
     ("Can I save my house?","Yes. Automatic stay stops foreclosure. Plan includes catch-up payments."),
     ("How long is the plan?","3 years (below median) or 5 years (above median).")])

chatt_topic("exemptions", "Exemptions",
    "Chattanooga Bankruptcy Exemptions -- State vs Federal",
    "Tennessee exemptions for Chattanooga filers. State vs federal comparison.",
    "Tennessee lets you choose state or federal exemptions.",
    f"""<section><div class="container">
<h2>Exemption Comparison</h2>
<div class="card">
{exemption_table()}
<div class="quick-answer">Homeowners: federal ($27,900) usually wins. Renters: state's $10,000 wildcard may protect more personal property.</div>
</div>
</div></section>""",
    [("What is the homestead exemption?","State: $5,000/$7,500. Federal: $27,900."),
     ("Can I choose federal?","Yes. Tennessee allows this."),
     ("What about my car?","State $10,000 wildcard or federal $4,450 vehicle exemption.")])

chatt_topic("faq", "FAQ",
    "Chattanooga Bankruptcy FAQ",
    "Common questions about filing bankruptcy in Chattanooga, TN.",
    "Answers to common questions about filing bankruptcy in Chattanooga.",
    f"""<section><div class="container">
<details class="faq-item"><summary>Where do I file?</summary><div class="answer"><p>E.D. Tenn. Chattanooga Division, {courthouse_chatt}. Phone: {phone_chatt}.</p></div></details>
<details class="faq-item"><summary>How much does bankruptcy cost?</summary><div class="answer"><p>Chapter 7: $1,238-$2,188. Chapter 13: $2,838-$4,363.</p></div></details>
<details class="faq-item"><summary>State or federal exemptions?</summary><div class="answer"><p>Your choice. Federal homestead ($27,900) is higher. <a href="/chattanooga/exemptions.html">Compare</a>.</p></div></details>
<details class="faq-item"><summary>How long does bankruptcy take?</summary><div class="answer"><p>Chapter 7: 3-4 months. Chapter 13: 3-5 years.</p></div></details>
<details class="faq-item"><summary>What is the 341 meeting?</summary><div class="answer"><p>Brief trustee hearing ~30 days after filing. <a href="https://341meeting.org">Learn more</a>.</p></div></details>
<details class="faq-item"><summary>Can I file again?</summary><div class="answer"><p>Yes, with timing rules. <a href="https://1328f.com">Check eligibility</a>.</p></div></details>
</div></section>""",
    [("Where do Chattanooga residents file?","E.D. Tenn. Chattanooga Division, 900 Georgia Ave, Suite 109, Chattanooga, TN 37402."),
     ("How much does bankruptcy cost?","Chapter 7: $1,238-$2,188. Chapter 13: $2,838-$4,363."),
     ("What exemptions apply?","Tennessee state or federal -- your choice.")])

# Count pages
import glob
pages = glob.glob(os.path.join(BASE, '**/*.html'), recursive=True)
city_pages = [p for p in pages if any(c in p for c in ['memphis', 'nashville', 'knoxville', 'chattanooga'])]
print(f"\nTotal city pages written: {len(city_pages)}")
