#!/usr/bin/env python3
"""
Merender seluruh diagram sumber (gambar/svg/*.svg) menjadi PNG beresolusi
cetak (gambar/*.png) memakai CairoSVG.

Setiap SVG dirender pada lebar piksel yang cukup untuk 300 dpi pada lebar
halaman isi (11,2 cm = ± 1323 px), sehingga tetap tajam saat disisipkan
python-docx dengan lebar tetap dalam sentimeter.

Pemakaian:
    python tools/render_svg.py            # render semua yang berubah
    python tools/render_svg.py --paksa    # render ulang semua berkas
"""

import re
import sys
from pathlib import Path

import cairosvg

AKAR = Path(__file__).resolve().parent.parent
SUMBER = AKAR / "gambar" / "svg"
TUJUAN = AKAR / "gambar"
LEBAR_CETAK_PX = 1600  # ~300 dpi pada lebar teks 11,2 cm


def lebar_viewbox(teks_svg):
    m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"',
                  teks_svg)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None, None


def render(paksa=False):
    if not SUMBER.exists():
        print("tidak ada folder gambar/svg/")
        return
    dihasilkan = 0
    for svg_path in sorted(SUMBER.glob("*.svg")):
        png_path = TUJUAN / (svg_path.stem + ".png")
        if (not paksa and png_path.exists()
                and png_path.stat().st_mtime > svg_path.stat().st_mtime):
            continue
        teks = svg_path.read_text(encoding="utf-8")
        w, h = lebar_viewbox(teks)
        skala = (LEBAR_CETAK_PX / w) if w else 2.0
        cairosvg.svg2png(
            bytestring=teks.encode("utf-8"),
            write_to=str(png_path),
            scale=skala,
            background_color="white",
        )
        print(f"dirender: {svg_path.name} -> {png_path.name} "
              f"(skala {skala:.2f})")
        dihasilkan += 1
    print(f"selesai: {dihasilkan} berkas dirender")


if __name__ == "__main__":
    render(paksa="--paksa" in sys.argv)
