#!/usr/bin/env python3
"""Hitung rasio kontras WCAG antara dua warna.

Pemakaian:
  python3 kontras.py "#777777" "#ffffff"
  python3 kontras.py "rgb(119,119,119)" "white"
"""
import re
import sys

NAMA = {"white": "#ffffff", "black": "#000000"}


def ke_rgb(warna: str):
    w = warna.strip().lower()
    w = NAMA.get(w, w)
    m = re.match(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", w)
    if m:
        return tuple(int(x) for x in m.groups())
    w = w.lstrip("#")
    if len(w) == 3:
        w = "".join(c * 2 for c in w)
    if not re.fullmatch(r"[0-9a-f]{6}", w):
        raise ValueError(f"Format warna tidak dikenali: {warna}")
    return tuple(int(w[i:i + 2], 16) for i in (0, 2, 4))


def luminans(rgb):
    def kanal(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (kanal(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def rasio(a, b):
    la, lb = sorted((luminans(ke_rgb(a)), luminans(ke_rgb(b))), reverse=True)
    return (la + 0.05) / (lb + 0.05)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    r = rasio(sys.argv[1], sys.argv[2])
    biasa = "LOLOS" if r >= 4.5 else "GAGAL"
    besar = "LOLOS" if r >= 3 else "GAGAL"
    print(f"Rasio kontras: {r:.2f}:1")
    print(f"Teks biasa (min 4,5:1): {biasa}")
    print(f"Teks besar/ikon (min 3:1): {besar}")
