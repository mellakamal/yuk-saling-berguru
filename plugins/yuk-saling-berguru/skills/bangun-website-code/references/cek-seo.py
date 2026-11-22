#!/usr/bin/env python3
"""Cek SEO dasar dan tampil profesional untuk web statis.
Pakai: python3 -I references/cek-seo.py FOLDER_WEB
Hanya memakai pustaka bawaan Python. Kode keluar 1 kalau ada masalah."""
import os, re, sys, html
from collections import Counter

root = sys.argv[1] if len(sys.argv) > 1 else "."
SKIP = {"node_modules", ".git", "dist", "build", ".astro"}
TITLE = (30, 65)
DESC = (130, 165)
IMG_NOTE_KB = 300
IMG_MAX_KB = 500
IMG_EXT = (".jpg", ".jpeg", ".png", ".webp", ".avif", ".gif")
BAD_TITLES = {"", "document", "untitled", "index", "home"}

pages = []
for d, dirs, files in os.walk(root):
    dirs[:] = [x for x in dirs if x not in SKIP]
    for f in files:
        if f.endswith(".html"):
            pages.append(os.path.join(d, f))
pages.sort()
problems, rows, notes = [], [], []
titles, descs = Counter(), Counter()
data = {}

def meta(h, name, attr="name"):
    m = re.search(r'<meta[^>]+%s="%s"[^>]+content="([^"]*)"' % (attr, name), h) or \
        re.search(r'<meta[^>]+content="([^"]*)"[^>]+%s="%s"' % (attr, name), h)
    return html.unescape(m.group(1)) if m else None

for p in pages:
    h = open(p, encoding="utf-8").read()
    is404 = os.path.basename(p).lower() == "404.html"
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    t = html.unescape(t.group(1).strip()) if t else ""
    d = meta(h, "description") or ""
    data[p] = (h, t, d, is404)
    titles[t] += 1
    descs[d] += 1

for p, (h, t, d, is404) in data.items():
    rel = os.path.relpath(p, root)
    noindex = bool(re.search(r'name="robots"[^>]+noindex', h))
    errs = []
    if t.lower() in BAD_TITLES or t.lower().endswith(".html"):
        errs.append("judul bawaan atau nama file")
    if noindex and not is404:
        errs.append("noindex di halaman utama")
    if not is404:
        if not TITLE[0] <= len(t) <= TITLE[1]:
            errs.append("judul %d kar (target %d-%d)" % (len(t), *TITLE))
        if not DESC[0] <= len(d) <= DESC[1]:
            errs.append("deskripsi %d kar (target %d-%d)" % (len(d), *DESC))
        if titles[t] > 1:
            errs.append("judul kembar")
        if descs[d] > 1:
            errs.append("deskripsi kembar")
        n = len(re.findall(r"<h1[\s>]", h))
        if n != 1:
            errs.append("H1 ada %d (harus 1)" % n)
        for k, pat in [("canonical", r'rel="canonical"'), ("lang", r'<html[^>]+lang="'),
                       ("viewport", r'name="viewport"'), ("og:image", r'property="og:image"'),
                       ("og:title", r'property="og:title"')]:
            if not re.search(pat, h):
                errs.append("tanpa " + k)
    for img in re.findall(r"<img\b[^>]*>", h):
        if not re.search(r'\balt="', img):
            errs.append("gambar tanpa alt")
            break
    for img in re.findall(r"<img\b[^>]*>", h):
        if not (re.search(r'\bwidth="', img) and re.search(r'\bheight="', img)):
            errs.append("gambar tanpa width dan height")
            break
    if re.search(r"&amp;(nbsp|amp|lt|gt|quot|#\d+);|&lt;/?[a-zA-Z!]", h):
        errs.append("kode tampil sebagai teks")
    for l in re.findall(r'href="([^"#?]+)', h):
        if not re.match(r"(https?:|mailto:|tel:|//|data:)", l) and l.endswith(".html"):
            errs.append("tautan memakai .html: " + l)
    for l in re.findall(r'(?:href|src)="([^"#?]+)', h):
        if re.match(r"(https?:|mailto:|tel:|//|data:)", l):
            continue
        target = os.path.normpath(os.path.join(root, l.lstrip("/")) if l.startswith("/")
                                  else os.path.join(os.path.dirname(p), l))
        if not (os.path.exists(target) or os.path.exists(target + ".html")
                or os.path.exists(os.path.join(target, "index.html"))):
            errs.append("tautan rusak: " + l)
    rows.append((rel, len(t), len(d), "OK" if not errs else "; ".join(errs)))
    problems += ["%s: %s" % (rel, e) for e in errs]

def block(h, tag):
    m = re.search(r"<%s\b.*?</%s>" % (tag, tag), h, re.S)
    if not m:
        return None
    x = re.sub(r'\s*aria-current="[^"]*"', "", m.group(0))
    return re.sub(r"\s+", " ", x).replace(" >", ">")

if len(data) > 3:
    for tag in ("header", "nav", "footer"):
        found = {block(h, tag) for (h, t, d, is404) in data.values() if not is404}
        if len(found) > 1:
            problems.append("isi <%s> berbeda antarhalaman" % tag)

for d, dirs, files in os.walk(root):
    dirs[:] = [x for x in dirs if x not in SKIP]
    for f in files:
        fp = os.path.join(d, f)
        if not f.lower().endswith(IMG_EXT):
            continue
        kb = os.path.getsize(fp) // 1024
        if kb > IMG_MAX_KB:
            problems.append("gambar lebih dari %d KB: %s (%d KB)" % (IMG_MAX_KB, os.path.relpath(fp, root), kb))
        elif kb > IMG_NOTE_KB:
            notes.append("gambar %d KB, pastikan ini gambar utama atau karya unggulan: %s" % (kb, os.path.relpath(fp, root)))

if not os.path.exists(os.path.join(root, "404.html")):
    problems.append("404.html tidak ada")
for name in ("sitemap.xml", "robots.txt"):
    if not os.path.exists(os.path.join(root, name)):
        problems.append(name + " tidak ada")
sm = os.path.join(root, "sitemap.xml")
if os.path.exists(sm):
    locs = re.findall(r"<loc>(.*?)</loc>", open(sm, encoding="utf-8").read())
    for u in locs:
        path = re.sub(r"^https?://[^/]+/?", "", u) or "index.html"
        cands = [path, path + ".html", os.path.join(path, "index.html")]
        if not any(os.path.exists(os.path.join(root, c)) for c in cands):
            problems.append("sitemap menunjuk ke halaman yang tidak ada: " + u)
    paths = {re.sub(r"^https?://[^/]+", "", u).strip("/") for u in locs}
    for p, (h, t, d, is404) in data.items():
        if is404:
            continue
        rel = os.path.relpath(p, root).replace(os.sep, "/")
        cands = {rel, rel[:-5]}
        if os.path.basename(rel) == "index.html":
            cands.add(os.path.dirname(rel))
        if not (cands & paths):
            problems.append("halaman tidak ada di sitemap: " + rel)

print("%-28s %6s %6s  %s" % ("Halaman", "Judul", "Desk.", "Hasil"))
for r in rows:
    print("%-28s %6d %6d  %s" % r)
if notes:
    print("\nCATATAN (tidak menggagalkan):")
    for x in notes:
        print("- " + x)
print("\nLOLOS" if not problems else "\nMASALAH (%d):" % len(problems))
for x in problems:
    print("- " + x)
sys.exit(1 if problems else 0)
