"""Memperbarui seluruh field TOC-style (Daftar Isi/Gambar/Tabel/Kode
Program) pada Buku-Ajar-PBO.docx lewat LibreOffice UNO API (headless),
lalu menyimpan ulang .docx dan mengekspor PDF pratinjau.

Dijalankan dengan python.exe bawaan LibreOffice (punya modul uno):
  "C:\\Program Files\\LibreOffice\\program\\python.exe" tools/perbarui_daftar_lo.py

Skrip ini memulai sendiri satu instance soffice --headless yang
menerima koneksi lewat named pipe, jadi tidak perlu soffice berjalan
lebih dulu.
"""
import subprocess
import sys
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue

AKAR = Path(__file__).resolve().parent.parent
DOCX = AKAR / "Buku-Ajar-PBO.docx"
PDF = AKAR / "keluaran" / "Buku-Ajar-PBO.pdf"
SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"
PIPE_NAME = "pbo_update_pipe"


def prop(nama, nilai):
    p = PropertyValue()
    p.Name = nama
    p.Value = nilai
    return p


def sambungkan():
    ctx_lokal = uno.getComponentContext()
    resolver = ctx_lokal.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", ctx_lokal)
    url = (f"uno:pipe,name={PIPE_NAME};urp;"
           "StarOffice.ComponentContext")
    for percobaan in range(30):
        try:
            return resolver.resolve(url)
        except Exception:
            time.sleep(1)
    raise RuntimeError("tidak dapat terhubung ke soffice setelah 30 detik")


def main():
    proses = subprocess.Popen([
        SOFFICE, "--headless", "--invisible", "--nocrashreport",
        "--nodefault", "--norestore", "--nofirststartwizard", "--nologo",
        f"--accept=pipe,name={PIPE_NAME};urp;",
    ])
    try:
        ctx = sambungkan()
        smgr = ctx.ServiceManager
        desktop = smgr.createInstanceWithContext(
            "com.sun.star.frame.Desktop", ctx)

        url_docx = uno.systemPathToFileUrl(str(DOCX))
        doc = desktop.loadComponentFromURL(
            url_docx, "_blank", 0,
            (prop("Hidden", True),))

        indeks = doc.getDocumentIndexes()
        print(f"jumlah indeks/daftar ditemukan: {indeks.getCount()}")
        for i in range(indeks.getCount()):
            item = indeks.getByIndex(i)
            item.update()
            print(f"  diperbarui: {item.getName()}")

        # perbarui seluruh field teks lain (PAGE, REF, SEQ, dll.)
        try:
            doc.getTextFields().refresh()
        except Exception as exc:
            print(f"peringatan: refresh text fields gagal: {exc}")

        doc.store()
        print(f"docx disimpan ulang: {DOCX}")

        PDF.parent.mkdir(parents=True, exist_ok=True)
        url_pdf = uno.systemPathToFileUrl(str(PDF))
        doc.storeToURL(
            url_pdf, (prop("FilterName", "writer_pdf_Export"),))
        print(f"pdf diekspor: {PDF}")

        doc.close(False)
    finally:
        try:
            desktop.terminate()
        except Exception:
            pass
        time.sleep(1)
        proses.terminate()


if __name__ == "__main__":
    sys.exit(main())
