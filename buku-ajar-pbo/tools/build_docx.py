#!/usr/bin/env python3
"""
Pembangun template .docx Buku Ajar Pemrograman Berorientasi Objek.

Menerapkan seluruh spesifikasi fisik pada ATURAN-BUKU-AJAR-PBO.md Bagian 2:
ukuran 15,5 x 23 cm, margin cermin, Arial 11 pt, dan seluruh gaya wajib
(BukuJudulBab, BukuBagianA, BukuSub1, BukuSub2, BukuIsi, BukuLabelBlok,
BukuKode, BukuKeteranganGambar, BukuKeteranganTabel, BukuPustaka,
BukuGlosarium).

Berkas keluaran hanya berisi kerangka: front matter, 15 judul bab beserta
lima blok pembuka yang masih kosong, dan back matter. Isi bab BELUM ditulis.

Pemakaian:
    python3 tools/build_docx.py
"""

from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION_START
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

FONT_ISI = "Arial"
FONT_KODE = "Courier New"  # pengganti resmi Consolas di macOS

BAB = [
    ("I", "PARADIGMA PEMROGRAMAN BERORIENTASI OBJEK", "CPMK2", "Sub-CPMK1", 1),
    ("II", "KELAS, OBJEK, ATRIBUT, METHOD, DAN CONSTRUCTOR", "CPMK2", "Sub-CPMK1", 2),
    ("III", "ENKAPSULASI, ACCESS MODIFIER, DAN INFORMATION HIDING", "CPMK2", "Sub-CPMK2", 3),
    ("IV", "PEMODELAN BERORIENTASI OBJEK DENGAN DIAGRAM KELAS UML", "CPMK1", "Sub-CPMK3", 4),
    ("V", "PEWARISAN (INHERITANCE)", "CPMK2", "Sub-CPMK4", 5),
    ("VI", "POLIMORFISME (POLYMORPHISM)", "CPMK2", "Sub-CPMK4", 6),
    ("VII", "ABSTRAKSI: ABSTRACT CLASS DAN INTERFACE", "CPMK2", "Sub-CPMK5", 7),
    ("VIII", "PENANGANAN EKSEPSI (EXCEPTION HANDLING)", "CPMK2", "Sub-CPMK6", 9),
    ("IX", "COLLECTION FRAMEWORK DAN GENERICS", "CPMK2", "Sub-CPMK6", 10),
    ("X", "OPERASI BERKAS DAN OBJECT PERSISTENCE", "CPMK3", "Sub-CPMK7", 11),
    ("XI", "KONEKSI BASIS DATA (JDBC) DAN OPERASI CRUD", "CPMK3", "Sub-CPMK7", 12),
    ("XII", "ANTARMUKA GRAFIS (GUI) DAN EVENT HANDLING", "CPMK3", "Sub-CPMK7", 13),
    ("XIII", "PRINSIP DESAIN BERORIENTASI OBJEK (SOLID)", "CPMK4", "Sub-CPMK8", 14),
    ("XIV", "PENGANTAR DESIGN PATTERN: SINGLETON, FACTORY, MVC", "CPMK4", "Sub-CPMK8", 14),
    ("XV", "INTEGRASI KONSEP DALAM PROYEK APLIKASI BERORIENTASI OBJEK",
     "CPMK3 dan CPMK4", "Sub-CPMK8", 15),
]

BLOK_PEMBUKA = [
    "CPMK/ Sub-CPMK :",
    "Indikator Penilaian:",
    "Kriteria Keberhasilan (Rubrik):",
    "Deskripsi Kemampuan yang Diharapkan:",
]

FRONT_MATTER = [
    "HALAMAN JUDUL",
    "HALAMAN IDENTITAS TERBITAN",
    "SANKSI PELANGGARAN PASAL 113 UNDANG-UNDANG NO. 28 TAHUN 2014",
    "KATA PENGANTAR",
    "PRAKATA PENULIS",
    "DAFTAR ISI",
    "DAFTAR GAMBAR",
    "DAFTAR TABEL",
    "DAFTAR KODE PROGRAM",
]

BACK_MATTER = [
    "DAFTAR PUSTAKA",
    "GLOSARIUM",
    "LAMPIRAN A. KISI-KISI DAN LATIHAN KOMPREHENSIF UTS",
    "LAMPIRAN B. KISI-KISI DAN LATIHAN KOMPREHENSIF UAS",
    "LAMPIRAN C. PANDUAN PROYEK AKHIR",
    "LAMPIRAN D. RUBRIK PENILAIAN RINGKAS",
    "BIOGRAFI PENULIS",
    "SINOPSIS BUKU",
]


def set_font(style, nama, ukuran, bold=False, italic=False):
    style.font.name = nama
    style.font.size = Pt(ukuran)
    style.font.bold = bold
    style.font.italic = italic
    style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for atr in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(atr), nama)


def buat_gaya(doc):
    st = doc.styles

    normal = st["Normal"]
    set_font(normal, FONT_ISI, 11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    def tambah(nama, base="Normal"):
        gaya = st.add_style(nama, 1)  # 1 = WD_STYLE_TYPE.PARAGRAPH
        gaya.base_style = st[base]
        return gaya

    g = tambah("BukuJudulBab")
    set_font(g, FONT_ISI, 16, bold=True)
    g.paragraph_format.space_before = Pt(0)
    g.paragraph_format.space_after = Pt(6)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuBagianA")
    set_font(g, FONT_ISI, 12, bold=True)
    g.paragraph_format.space_before = Pt(12)
    g.paragraph_format.space_after = Pt(6)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuSub1")
    set_font(g, FONT_ISI, 11, bold=True)
    g.paragraph_format.space_before = Pt(8)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuSub2")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.space_before = Pt(6)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuIsi")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    g.paragraph_format.first_line_indent = Cm(0.75)

    g = tambah("BukuLabelBlok")
    set_font(g, FONT_ISI, 11, bold=True)
    g.paragraph_format.space_before = Pt(10)
    g.paragraph_format.space_after = Pt(4)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuKode")
    set_font(g, FONT_KODE, 10)
    g.paragraph_format.line_spacing = 1.0
    g.paragraph_format.space_after = Pt(0)
    g.paragraph_format.left_indent = Cm(0.5)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    g = tambah("BukuKeteranganGambar")
    set_font(g, FONT_ISI, 10)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_before = Pt(4)

    g = tambah("BukuKeteranganTabel")
    set_font(g, FONT_ISI, 10)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_after = Pt(4)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuPustaka")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.left_indent = Cm(0.75)
    g.paragraph_format.first_line_indent = Cm(-0.75)
    g.paragraph_format.space_after = Pt(6)

    g = tambah("BukuGlosarium")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    g.paragraph_format.left_indent = Cm(0.75)
    g.paragraph_format.first_line_indent = Cm(-0.75)


def atur_halaman(section):
    section.page_width = Cm(15.5)
    section.page_height = Cm(23)
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(1.8)
    section.gutter = Cm(0)


def aktifkan_mirror(doc):
    sett = doc.settings.element
    el = OxmlElement("w:mirrorMargins")
    sett.append(el)


def nomor_halaman(section, format_angka):
    """Nomor halaman bawah-tengah; format_angka: 'lowerRoman' atau 'decimal'."""
    sec_pr = section._sectPr
    pg = sec_pr.find(qn("w:pgNumType"))
    if pg is None:
        pg = OxmlElement("w:pgNumType")
        sec_pr.append(pg)
    pg.set(qn("w:fmt"), format_angka)
    pg.set(qn("w:start"), "1")

    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    run = p.add_run()
    run.font.name = FONT_ISI
    run.font.size = Pt(10)
    for tipe, teks in (("begin", None), (None, "PAGE"), ("end", None)):
        if tipe:
            fld = OxmlElement("w:fldChar")
            fld.set(qn("w:fldCharType"), tipe)
            run._r.append(fld)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = f" {teks} "
            run._r.append(instr)


def field_toc(paragraph, instruksi):
    run = paragraph.add_run()
    b = OxmlElement("w:fldChar")
    b.set(qn("w:fldCharType"), "begin")
    i = OxmlElement("w:instrText")
    i.set(qn("xml:space"), "preserve")
    i.text = instruksi
    s = OxmlElement("w:fldChar")
    s.set(qn("w:fldCharType"), "separate")
    t = OxmlElement("w:t")
    t.text = "Klik kanan lalu pilih Update Field untuk memuat daftar."
    e = OxmlElement("w:fldChar")
    e.set(qn("w:fldCharType"), "end")
    for el in (b, i, s, t, e):
        run._r.append(el)


def judul_halaman(doc, teks, gaya="BukuJudulBab"):
    p = doc.add_paragraph(teks, style=gaya)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def bangun():
    doc = Document()
    buat_gaya(doc)
    aktifkan_mirror(doc)

    sec = doc.sections[0]
    atur_halaman(sec)
    nomor_halaman(sec, "lowerRoman")

    # ---------- FRONT MATTER ----------
    for idx, judul in enumerate(FRONT_MATTER):
        if idx:
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        judul_halaman(doc, judul)
        if judul == "DAFTAR ISI":
            field_toc(doc.add_paragraph(), r' TOC \o "1-2" \h \z \u ')
        elif judul == "DAFTAR GAMBAR":
            field_toc(doc.add_paragraph(), r' TOC \h \z \c "Gambar" ')
        elif judul == "DAFTAR TABEL":
            field_toc(doc.add_paragraph(), r' TOC \h \z \c "Tabel" ')
        elif judul == "DAFTAR KODE PROGRAM":
            field_toc(doc.add_paragraph(), r' TOC \h \z \c "Kode Program" ')
        else:
            doc.add_paragraph("[ diisi pada Tahap 3 ]", style="BukuIsi")

    # ---------- ISI ----------
    sec2 = doc.add_section(WD_SECTION_START.NEW_PAGE)
    atur_halaman(sec2)
    sec2.footer.is_linked_to_previous = False
    nomor_halaman(sec2, "decimal")

    for i, (romawi, judul, cpmk, subcpmk, minggu) in enumerate(BAB):
        if i:
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        doc.add_paragraph(f"BAB {romawi}.", style="BukuJudulBab")
        doc.add_paragraph(f"({judul})", style="BukuJudulBab")
        for label in BLOK_PEMBUKA:
            doc.add_paragraph(label, style="BukuLabelBlok")
            if label.startswith("CPMK"):
                doc.add_paragraph(f"{cpmk} — [ salin verbatim dari RPS ]",
                                  style="List Bullet")
                doc.add_paragraph(f"{subcpmk} — [ salin verbatim dari RPS ]",
                                  style="List Bullet")
            elif label.startswith("Kriteria"):
                for lv in ("Sangat Baik (≥ 85):", "Baik (70-84):", "Cukup (55-69):"):
                    doc.add_paragraph(f"{lv} [ deskriptor ]", style="List Bullet")
            else:
                doc.add_paragraph("[ diisi pada Tahap 2 ]", style="BukuIsi")
        doc.add_paragraph("A. Pendahuluan", style="BukuBagianA")
        doc.add_paragraph(
            f"[ Isi bab belum ditulis. Rujukan RPS: Minggu {minggu}. ]",
            style="BukuIsi")
        doc.add_paragraph("Rangkuman", style="BukuLabelBlok")
        doc.add_paragraph("[ diisi pada Tahap 2 ]", style="BukuIsi")
        doc.add_paragraph("Soal/Pertanyaan", style="BukuLabelBlok")
        doc.add_paragraph("[ diisi pada Tahap 2 ]", style="BukuIsi")
        doc.add_paragraph("Rujukan Bab", style="BukuLabelBlok")
        doc.add_paragraph("[ diisi pada Tahap 2 ]", style="BukuIsi")

    # ---------- BACK MATTER ----------
    for judul in BACK_MATTER:
        doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        judul_halaman(doc, judul)
        doc.add_paragraph("[ diisi pada Tahap 3 ]", style="BukuIsi")

    keluaran = Path(__file__).resolve().parent.parent / "Buku-Ajar-PBO.docx"
    doc.save(keluaran)
    print(f"tersimpan: {keluaran}")


if __name__ == "__main__":
    bangun()
