#!/usr/bin/env python3
"""
Perakit .docx Buku Ajar Pemrograman Berorientasi Objek.

Membaca seluruh naskah Markdown pada folder naskah/ secara berurutan
(00-front-matter.md, bab-01.md ... bab-15.md, 90-back-matter.md) lalu
menyusunnya menjadi satu berkas Buku-Ajar-PBO.docx dengan spesifikasi
fisik ATURAN-BUKU-AJAR-PBO.md Bagian 2: ukuran 15,5 x 23 cm, margin
cermin, Arial 11 pt, dan seluruh gaya wajib Buku*.

Konvensi Markdown yang dikenali dijelaskan pada buku-ajar-pbo/README.md.
Skrip juga memeriksa aturan listing (maksimum 40 baris dan 64 karakter
per baris) serta menghitung penanda [TAHAP n] yang belum diisi.

Pemakaian:
    python tools/build_docx.py
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

AKAR = Path(__file__).resolve().parent.parent
NASKAH = AKAR / "naskah"
KELUARAN = AKAR / "Buku-Ajar-PBO.docx"

FONT_ISI = "Arial"
FONT_KODE = "Consolas"
LEBAR_TEKS = Cm(15.5 - 2.5 - 1.8)
MAKS_BARIS_LISTING = 40
# 54, bukan 64: pada Consolas 9,5 pt dengan indentasi kiri 0,5 cm, lebar
# teks isi (11,2 cm) hanya memuat ± 56 karakter monospace sebelum
# terpotong ke baris berikutnya; 54 memberi sedikit ruang aman. Lihat
# ATURAN-BUKU-AJAR-PBO.md Bagian 2 untuk perhitungannya.
MAKS_KOLOM_LISTING = 54

# Identifier SEQ tidak boleh berspasi, sehingga "Kode Program" memakai
# identifier KodeProgram. Teks yang tercetak tetap "Kode Program n."
SEQ = {"Gambar": "Gambar", "Tabel": "Tabel", "Kode Program": "KodeProgram"}

DAFTAR_FIELD = {
    "isi": r' TOC \o "1-2" \h \z \u ',
    "gambar": r' TOC \h \z \c "Gambar" ',
    "tabel": r' TOC \h \z \c "Tabel" ',
    "kode": r' TOC \h \z \c "KodeProgram" ',
}

peringatan = []


# ------------------------------------------------------------------ gaya

def set_font(style, nama, ukuran, bold=False, italic=False, underline=False):
    style.font.name = nama
    style.font.size = Pt(ukuran)
    style.font.bold = bold
    style.font.italic = italic
    style.font.underline = underline
    style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for atr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(atr), nama)


def set_outline(style, level):
    ppr = style.element.get_or_add_pPr()
    el = OxmlElement("w:outlineLvl")
    el.set(qn("w:val"), str(level))
    ppr.append(el)


def set_shading(ppr, warna):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), warna)
    ppr.append(shd)


def set_border(ppr, sisi=("top", "left", "bottom", "right"), warna="808080"):
    bdr = OxmlElement("w:pBdr")
    for s in sisi:
        el = OxmlElement(f"w:{s}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")  # 0,5 pt
        el.set(qn("w:space"), "1")
        el.set(qn("w:color"), warna)
        bdr.append(el)
    ppr.append(bdr)


def buat_gaya(doc):
    st = doc.styles

    normal = st["Normal"]
    set_font(normal, FONT_ISI, 11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    def tambah(nama, base="Normal"):
        gaya = st.add_style(nama, 1)  # 1 = WD_STYLE_TYPE.PARAGRAPH
        gaya.base_style = st[base]
        gaya.quick_style = True
        return gaya

    # --- gaya wajib (Aturan Bagian 2) ---
    g = tambah("BukuJudulBab")
    set_font(g, FONT_ISI, 16, bold=True)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    g.paragraph_format.space_after = Pt(12)
    g.paragraph_format.keep_with_next = True
    g.paragraph_format.page_break_before = True
    set_outline(g, 0)

    g = tambah("BukuBagianA")
    set_font(g, FONT_ISI, 12, bold=True)
    g.paragraph_format.space_before = Pt(12)
    g.paragraph_format.space_after = Pt(6)
    g.paragraph_format.keep_with_next = True
    set_outline(g, 1)

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
    set_font(g, FONT_KODE, 9.5)
    g.paragraph_format.line_spacing = 1.0
    g.paragraph_format.space_after = Pt(0)
    g.paragraph_format.left_indent = Cm(0.5)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    ppr = g.element.get_or_add_pPr()
    set_border(ppr)
    set_shading(ppr, "F2F2F2")  # abu-abu 5 %

    g = tambah("BukuKeteranganGambar")
    set_font(g, FONT_ISI, 10)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_before = Pt(4)

    g = tambah("BukuKeteranganTabel")
    set_font(g, FONT_ISI, 10)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_before = Pt(8)
    g.paragraph_format.space_after = Pt(4)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuPustaka")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    g.paragraph_format.left_indent = Cm(0.75)
    g.paragraph_format.first_line_indent = Cm(-0.75)

    g = tambah("BukuGlosarium")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    g.paragraph_format.left_indent = Cm(0.75)
    g.paragraph_format.first_line_indent = Cm(-0.75)

    # --- gaya pendukung front/back matter, daftar, tabel, dan draf ---
    g = tambah("BukuJudulHalaman")
    set_font(g, FONT_ISI, 16, bold=True, underline=True)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_after = Pt(12)
    g.paragraph_format.keep_with_next = True
    g.paragraph_format.page_break_before = True
    set_outline(g, 0)

    g = tambah("BukuButir")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    g.paragraph_format.space_after = Pt(3)

    g = tambah("BukuTabelIsi")
    set_font(g, FONT_ISI, 10)
    g.paragraph_format.line_spacing = 1.0
    g.paragraph_format.space_after = Pt(0)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    g = tambah("BukuSampulJudul")
    set_font(g, FONT_ISI, 24, bold=True)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_before = Pt(48)
    g.paragraph_format.line_spacing = 1.0

    g = tambah("BukuSampulAnakJudul")
    set_font(g, FONT_ISI, 18, bold=True)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_after = Pt(60)
    g.paragraph_format.line_spacing = 1.0

    g = tambah("BukuSampulPenerbit")
    set_font(g, FONT_ISI, 14, bold=True)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_before = Pt(170)

    g = tambah("BukuTengah")
    set_font(g, FONT_ISI, 12)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_after = Pt(0)

    g = tambah("BukuTengahTebal")
    set_font(g, FONT_ISI, 11, bold=True)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_before = Pt(12)

    g = tambah("BukuJudulSanksi")
    set_font(g, FONT_ISI, 12, bold=True, underline=True)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    g.paragraph_format.space_after = Pt(0)
    g.paragraph_format.keep_with_next = True

    g = tambah("BukuIdentitas")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.space_after = Pt(2)

    g = tambah("BukuKanan")
    set_font(g, FONT_ISI, 11)
    g.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    g.paragraph_format.space_before = Pt(12)

    g = tambah("BukuCatatanDraf")
    set_font(g, FONT_ISI, 9, italic=True)
    g.font.color.rgb = RGBColor(0x7F, 0x60, 0x00)
    g.paragraph_format.space_after = Pt(6)
    ppr = g.element.get_or_add_pPr()
    set_border(ppr, sisi=("left",), warna="BF9000")
    set_shading(ppr, "FFF2CC")

    # bahasa pemeriksa ejaan: Indonesia
    rpr_default = doc.styles.element.find(qn("w:docDefaults")).find(
        qn("w:rPrDefault")).find(qn("w:rPr"))
    lang = rpr_default.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr_default.append(lang)
    lang.set(qn("w:val"), "id-ID")


# ------------------------------------------------------------- penomoran

class Penomoran:
    """Definisi butir berpoin dan daftar bernomor yang dimulai ulang."""

    BULLET = 9001
    DESIMAL = 9002

    def __init__(self, doc):
        self.root = doc.part.numbering_part.element
        self.num_berikut = 9100
        self._abstrak(self.BULLET, "bullet", "", "Symbol", 794, 369)
        self._abstrak(self.DESIMAL, "decimal", "%1.", FONT_ISI, 425, 425)
        self.num_bullet = self.baru(self.BULLET)

    def _abstrak(self, aid, fmt, teks, font, kiri, gantung):
        an = OxmlElement("w:abstractNum")
        an.set(qn("w:abstractNumId"), str(aid))
        lvl = OxmlElement("w:lvl")
        lvl.set(qn("w:ilvl"), "0")
        for tag, val in (("w:start", "1"), ("w:numFmt", fmt),
                         ("w:lvlText", teks), ("w:lvlJc", "left")):
            el = OxmlElement(tag)
            el.set(qn("w:val"), val)
            lvl.append(el)
        ppr = OxmlElement("w:pPr")
        ind = OxmlElement("w:ind")
        ind.set(qn("w:left"), str(kiri))
        ind.set(qn("w:hanging"), str(gantung))
        ppr.append(ind)
        lvl.append(ppr)
        rpr = OxmlElement("w:rPr")
        rf = OxmlElement("w:rFonts")
        rf.set(qn("w:ascii"), font)
        rf.set(qn("w:hAnsi"), font)
        rf.set(qn("w:hint"), "default")
        rpr.append(rf)
        lvl.append(rpr)
        an.append(lvl)
        # abstractNum wajib mendahului seluruh elemen num
        pertama_num = self.root.find(qn("w:num"))
        if pertama_num is None:
            self.root.append(an)
        else:
            pertama_num.addprevious(an)

    def baru(self, aid):
        nid = self.num_berikut
        self.num_berikut += 1
        num = OxmlElement("w:num")
        num.set(qn("w:numId"), str(nid))
        ref = OxmlElement("w:abstractNumId")
        ref.set(qn("w:val"), str(aid))
        num.append(ref)
        ov = OxmlElement("w:lvlOverride")
        ov.set(qn("w:ilvl"), "0")
        so = OxmlElement("w:startOverride")
        so.set(qn("w:val"), "1")
        ov.append(so)
        num.append(ov)
        self.root.append(num)
        return nid


def pasang_nomor(paragraph, num_id):
    ppr = paragraph._p.get_or_add_pPr()
    numpr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), "0")
    nid = OxmlElement("w:numId")
    nid.set(qn("w:val"), str(num_id))
    numpr.append(ilvl)
    numpr.append(nid)
    ppr.append(numpr)


# ------------------------------------------------------ halaman & field

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
    zoom = sett.find(qn("w:zoom"))
    if zoom is not None:
        zoom.addnext(el)
    else:
        sett.insert(0, el)


def tambah_field(run, instruksi, hasil=""):
    for tipe in ("begin", "instr", "separate", "text", "end"):
        if tipe == "instr":
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = instruksi
        elif tipe == "text":
            el = OxmlElement("w:t")
            el.set(qn("xml:space"), "preserve")
            el.text = hasil
        else:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tipe)
        run._r.append(el)


def nomor_halaman(section, format_angka, mulai):
    """Nomor halaman bawah-tengah, Arial 10 pt."""
    sec_pr = section._sectPr
    pg = sec_pr.find(qn("w:pgNumType"))
    if pg is None:
        pg = OxmlElement("w:pgNumType")
        sec_pr.append(pg)
    pg.set(qn("w:fmt"), format_angka)
    pg.set(qn("w:start"), str(mulai))

    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    run = p.add_run()
    run.font.name = FONT_ISI
    run.font.size = Pt(10)
    tambah_field(run, " PAGE ", "1")


# ---------------------------------------------------------- teks inline

POLA_INLINE = re.compile(
    r"(\{\{(?:g|t|kp):[A-Za-z0-9_-]+\}\}"
    r"|\*\*.+?\*\*|`[^`]+`|\*[^*\s][^*]*?\*)")
POLA_REF = re.compile(r"^\{\{(g|t|kp):([A-Za-z0-9_-]+)\}\}$")
AWALAN_BOOKMARK = {"g": "refG_", "t": "refT_", "kp": "refK_"}


def nama_bookmark(tipe, slug):
    return AWALAN_BOOKMARK[tipe] + re.sub(r"[^A-Za-z0-9_]", "_", slug)


_id_bookmark = [0]


def tambah_bookmark(paragraph, nama, pembuat_isi):
    """Membungkus elemen yang dibuat pembuat_isi() dengan bookmark bernama
    `nama`, agar dapat dirujuk oleh field REF di tempat lain (rujukan
    silang nomor Gambar/Tabel/Kode Program yang otomatis mengikuti)."""
    _id_bookmark[0] += 1
    bid = str(_id_bookmark[0])
    mulai = OxmlElement("w:bookmarkStart")
    mulai.set(qn("w:id"), bid)
    mulai.set(qn("w:name"), nama)
    paragraph._p.append(mulai)
    hasil = pembuat_isi()
    selesai = OxmlElement("w:bookmarkEnd")
    selesai.set(qn("w:id"), bid)
    paragraph._p.append(selesai)
    return hasil


def tulis_inline(paragraph, teks, bold=False):
    for bagian in POLA_INLINE.split(teks):
        if not bagian:
            continue
        mref = POLA_REF.match(bagian)
        if mref:
            tipe, slug = mref.group(1), mref.group(2)
            run = paragraph.add_run()
            if bold:
                run.bold = True
            tambah_field(run, f" REF {nama_bookmark(tipe, slug)} \\h ",
                         "#")
            continue
        if bagian.startswith("**") and bagian.endswith("**"):
            tulis_inline(paragraph, bagian[2:-2], bold=True)
            continue
        run = paragraph.add_run()
        if bagian.startswith("`") and bagian.endswith("`"):
            run.text = bagian[1:-1]
            run.font.name = FONT_KODE
            run._r.get_or_add_rPr().get_or_add_rFonts().set(
                qn("w:hAnsi"), FONT_KODE)
        elif (bagian.startswith("*") and bagian.endswith("*")
              and len(bagian) > 2):
            run.text = bagian[1:-1]
            run.italic = True
        else:
            run.text = bagian
        if bold:
            run.bold = True


# ------------------------------------------------------------- perakit

POLA_KETERANGAN = re.compile(
    r"^(Gambar|Tabel|Kode Program) #([A-Za-z0-9_-]*)\.\s+(.+)$")
POLA_GAMBAR = re.compile(r"^!\[(.*)\]\((.+)\)$")
POLA_DIREKTIF = re.compile(r"^<!--\s*([a-z-]+)\s*(?::\s*(.+?))?\s*-->$")


class Perakit:
    def __init__(self, doc):
        self.doc = doc
        self.nomor = Penomoran(doc)
        self.seq = {k: 0 for k in SEQ}
        self.putus_halaman = False
        self.penanda_draf = 0

    # -- utilitas paragraf --
    def paragraf(self, gaya):
        p = self.doc.add_paragraph(style=gaya)
        if self.putus_halaman:
            p.paragraph_format.page_break_before = True
            self.putus_halaman = False
        return p

    def keterangan(self, label, judul, gaya, slug=""):
        self.seq[label] += 1
        p = self.paragraf(gaya)
        p.add_run(f"{label} ")
        nomor = str(self.seq[label])
        if slug:
            tipe = {"Gambar": "g", "Tabel": "t",
                    "Kode Program": "kp"}[label]
            tambah_bookmark(
                p, nama_bookmark(tipe, slug),
                lambda: tambah_field(
                    p.add_run(), f" SEQ {SEQ[label]} \\* ARABIC ", nomor))
        else:
            tambah_field(p.add_run(), f" SEQ {SEQ[label]} \\* ARABIC ",
                         nomor)
        tulis_inline(p, f". {judul}")
        return p

    # -- blok --
    def blok_kode(self, baris, bahasa, sumber):
        if bahasa == "java" and len(baris) > MAKS_BARIS_LISTING:
            peringatan.append(f"{sumber}: listing {len(baris)} baris "
                              f"(maks {MAKS_BARIS_LISTING})")
        for teks in baris:
            if len(teks) > MAKS_KOLOM_LISTING:
                peringatan.append(f"{sumber}: baris kode {len(teks)} "
                                  f"karakter: {teks.strip()[:40]}...")
            p = self.paragraf("BukuKode")
            p.add_run(teks.replace("\t", "    ") or " ")

    def blok_tabel(self, baris):
        sel = [[c.strip() for c in b.strip().strip("|").split("|")]
               for b in baris
               if not re.match(r"^\|?\s*:?-{3,}", b.strip())]
        kolom = max(len(r) for r in sel)
        tabel = self.doc.add_table(rows=len(sel), cols=kolom)
        tabel.style = self.doc.styles["Table Grid"]
        tabel.alignment = WD_TABLE_ALIGNMENT.CENTER
        tabel.autofit = False
        if kolom == 2:
            lebar = [LEBAR_TEKS * 0.3, LEBAR_TEKS * 0.7]
        else:
            lebar = [LEBAR_TEKS / kolom] * kolom
        # w:tblGrid eksplisit: lebar kolom tabel juga perlu
        # didefinisikan pada level tabel, bukan hanya per sel,
        # agar autofit=False benar-benar dihormati.
        tblgrid = tabel._tbl.find(qn("w:tblGrid"))
        if tblgrid is not None:
            for gridcol, lb in zip(tblgrid.findall(qn("w:gridCol")),
                                    lebar):
                gridcol.set(qn("w:w"), str(int(lb)))
        for i, isi_baris in enumerate(sel):
            row = tabel.rows[i]
            if i == 0:
                trpr = row._tr.get_or_add_trPr()
                hdr = OxmlElement("w:tblHeader")
                trpr.append(hdr)
            cant = OxmlElement("w:cantSplit")
            row._tr.get_or_add_trPr().append(cant)
            for j in range(kolom):
                cell = row.cells[j]
                cell.width = int(lebar[j])
                p = cell.paragraphs[0]
                p.style = self.doc.styles["BukuTabelIsi"]
                teks = isi_baris[j] if j < len(isi_baris) else ""
                tulis_inline(p, teks, bold=(i == 0))
                if i == 0:
                    set_shading(cell._tc.get_or_add_tcPr(), "D9D9D9")
        self.doc.add_paragraph(style="BukuTabelIsi")  # jarak setelah tabel

    def blok_gambar(self, keterangan, path, sumber):
        berkas = (NASKAH / path).resolve()
        p = self.paragraf("BukuKeteranganGambar")
        p.paragraph_format.keep_with_next = True
        if berkas.exists():
            p.add_run().add_picture(str(berkas), width=LEBAR_TEKS)
        else:
            peringatan.append(f"{sumber}: gambar belum ada: {path}")
            p.add_run(f"[gambar belum tersedia: {path}]").italic = True
        m = POLA_KETERANGAN.match(keterangan)
        if m and m.group(1) == "Gambar":
            self.keterangan("Gambar", m.group(3), "BukuKeteranganGambar",
                             slug=Path(path).stem)
        elif keterangan:
            self.paragraf("BukuKeteranganGambar").add_run(keterangan)

    def daftar(self, butir, bernomor):
        num_id = (self.nomor.baru(Penomoran.DESIMAL) if bernomor
                  else self.nomor.num_bullet)
        for teks in butir:
            p = self.paragraf("BukuButir")
            pasang_nomor(p, num_id)
            tulis_inline(p, teks)

    # -- berkas --
    def rakit(self, berkas):
        adalah_bab = berkas.name.startswith("bab-")
        sumber = berkas.name
        baris = berkas.read_text(encoding="utf-8").splitlines()
        i = 0
        gaya_berikut = None
        judul_bab = None  # paragraf judul bab yang sedang dirangkai

        while i < len(baris):
            b = baris[i].rstrip()
            s = b.strip()

            if not s or s == "---":
                i += 1
                continue

            m = POLA_DIREKTIF.match(s)
            if m:
                nama, nilai = m.group(1), m.group(2)
                if nama == "halaman-baru":
                    self.putus_halaman = True
                elif nama == "gaya":
                    gaya_berikut = nilai
                elif nama == "daftar":
                    p = self.paragraf("BukuIsi")
                    tambah_field(p.add_run(), DAFTAR_FIELD[nilai],
                                 "Perbarui field untuk memuat daftar.")
                i += 1
                continue
            if s.startswith("<!--"):
                i += 1
                continue

            if s.startswith("```"):
                bahasa = s[3:].strip()
                isi = []
                i += 1
                while i < len(baris) and not baris[i].strip().startswith("```"):
                    isi.append(baris[i].rstrip())
                    i += 1
                self.blok_kode(isi, bahasa, sumber)
                i += 1
                continue

            if s.startswith("|"):
                isi = []
                while i < len(baris) and baris[i].strip().startswith("|"):
                    isi.append(baris[i])
                    i += 1
                self.blok_tabel(isi)
                continue

            mh = re.match(r"^(#{1,5})\s+(.*)$", s)
            if mh:
                level, teks = len(mh.group(1)), mh.group(2)
                if level == 1 and adalah_bab:
                    if judul_bab is None:
                        judul_bab = self.paragraf("BukuJudulBab")
                        judul_bab.add_run(teks)
                    else:
                        judul_bab.add_run().add_break()
                        judul_bab.add_run(teks)
                    i += 1
                    continue
                gaya = {1: "BukuJudulHalaman", 2: "BukuBagianA",
                        3: "BukuLabelBlok", 4: "BukuSub1",
                        5: "BukuSub2"}[level]
                tulis_inline(self.paragraf(gaya), teks)
                judul_bab = None
                i += 1
                continue
            judul_bab = None

            mg = POLA_GAMBAR.match(s)
            if mg:
                self.blok_gambar(mg.group(1), mg.group(2), sumber)
                i += 1
                continue

            if re.match(r"^[-*]\s+", s) or re.match(r"^\d+\.\s+", s):
                bernomor = bool(re.match(r"^\d+\.\s+", s))
                pola = r"^\d+\.\s+" if bernomor else r"^[-*]\s+"
                butir = []
                while i < len(baris) and re.match(pola, baris[i].strip()):
                    butir.append(re.sub(pola, "", baris[i].strip()))
                    i += 1
                self.daftar(butir, bernomor)
                continue

            if s.startswith(">"):
                isi = []
                while i < len(baris) and baris[i].strip().startswith(">"):
                    isi.append(baris[i].strip().lstrip(">").strip())
                    i += 1
                teks = " ".join(isi)
                self.penanda_draf += len(re.findall(r"\[TAHAP \d\]", teks))
                tulis_inline(self.paragraf("BukuCatatanDraf"), teks)
                continue

            # paragraf biasa; blok bergaya khusus: satu baris satu paragraf
            isi = []
            while i < len(baris):
                t = baris[i].strip()
                if (not t or t.startswith(("#", "|", "```", ">", "<!--", "!["))
                        or re.match(r"^([-*]|\d+\.)\s+", t)):
                    break
                isi.append(t)
                i += 1
            if not isi:  # baris tak dikenali: cetak apa adanya
                isi.append(s)
                i += 1
            if gaya_berikut:
                for t in isi:
                    tulis_inline(self.paragraf(gaya_berikut), t)
                gaya_berikut = None
                continue
            teks = " ".join(isi)
            mk = POLA_KETERANGAN.match(teks)
            if mk and mk.group(1) in ("Tabel", "Kode Program"):
                self.keterangan(mk.group(1), mk.group(3),
                                "BukuKeteranganTabel", slug=mk.group(2))
            else:
                tulis_inline(self.paragraf("BukuIsi"), teks)


URUTAN_PPR = [
    "pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
    "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs",
    "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct",
    "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
    "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents",
    "suppressOverlap", "jc", "textDirection", "textAlignment",
    "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr",
    "pPrChange",
]


def urutkan_ppr(root):
    """Menyusun ulang anak w:pPr sesuai urutan skema OOXML."""
    peringkat = {qn(f"w:{n}"): i for i, n in enumerate(URUTAN_PPR)}
    for ppr in root.iter(qn("w:pPr")):
        anak = list(ppr)
        anak.sort(key=lambda el: peringkat.get(el.tag, len(URUTAN_PPR)))
        for el in anak:
            ppr.append(el)


def bangun():
    doc = Document()
    buat_gaya(doc)
    aktifkan_mirror(doc)

    sec = doc.sections[0]
    atur_halaman(sec)
    nomor_halaman(sec, "lowerRoman", 2)

    perakit = Perakit(doc)
    depan = NASKAH / "00-front-matter.md"
    bab = sorted(NASKAH.glob("bab-*.md"))
    belakang = NASKAH / "90-back-matter.md"

    perakit.rakit(depan)

    sec2 = doc.add_section(WD_SECTION_START.NEW_PAGE)
    atur_halaman(sec2)
    nomor_halaman(sec2, "decimal", 1)
    for berkas in bab:
        perakit.rakit(berkas)
    if belakang.exists():
        perakit.rakit(belakang)

    # paragraf kosong bawaan Document() di awal dokumen dibuang
    pertama = doc.paragraphs[0]
    if not pertama.text and pertama.style.name == "Normal":
        pertama._p.getparent().remove(pertama._p)

    urutkan_ppr(doc.styles.element)
    urutkan_ppr(doc.element.body)
    urutkan_ppr(doc.part.numbering_part.element)
    doc.save(KELUARAN)
    print(f"tersimpan: {KELUARAN}")
    print(f"bab: {len(bab)} | gambar: {perakit.seq['Gambar']} | "
          f"tabel: {perakit.seq['Tabel']} | "
          f"kode program: {perakit.seq['Kode Program']} | "
          f"penanda [TAHAP n] tersisa: {perakit.penanda_draf}")
    for w in peringatan:
        print(f"PERINGATAN {w}")
    return 1 if any("listing" in w or "karakter" in w
                    for w in peringatan) else 0


if __name__ == "__main__":
    sys.exit(bangun())
