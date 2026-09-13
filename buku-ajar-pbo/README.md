# Naskah Buku Ajar PBO

| Berkas / folder | Isi |
|---|---|
| `Buku-Ajar-PBO.docx` | Luaran utama, **dirakit otomatis** dari seluruh berkas di `naskah/`. Jangan diedit langsung. |
| `naskah/` | Sumber naskah Markdown: `00-front-matter.md`, `bab-01.md` sampai `bab-15.md`, `90-back-matter.md`. |
| `kode/` | Proyek Java per bab. Setiap listing di buku wajib berasal dari sini dan sudah diuji kompilasi pada JDK 21. |
| `gambar/` | Gambar dan diagram, penomoran berurutan satu buku. |
| `tools/build_docx.py` | Merakit `naskah/*.md` menjadi `.docx` beserta seluruh gaya Word, lalu memeriksa aturan listing. |
| `tools/perbarui_daftar_lo.py` | **Cara utama** memperbarui Daftar Isi/Gambar/Tabel/Kode dan mengekspor PDF, lewat LibreOffice UNO API. |
| `tools/pratinjau.ps1` | Cara cadangan lewat Microsoft Word COM (lihat catatan di bawah). |
| `keluaran/` | PDF pratinjau (tidak di-commit). |

## Membangun

```bash
python tools/build_docx.py
```

```bash
"C:\Program Files\LibreOffice\program\python.exe" tools/perbarui_daftar_lo.py
```

`build_docx.py` keluar dengan kode 1 bila ada listing lebih dari 40 baris atau
baris kode lebih dari 54 karakter, dan melaporkan sisa penanda `[TAHAP n]`.

Untuk pratinjau PDF cepat tanpa memperbarui Daftar Isi/Gambar/Tabel/Kode
(nomor Gambar/Tabel/Kode Program di badan teks tetap benar karena dihitung
Python, hanya keempat daftar itu yang masih menampilkan placeholder):

```bash
"C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf --outdir keluaran Buku-Ajar-PBO.docx
```

### Catatan: Microsoft Word COM tidak andal pada dokumen ini

`tools/pratinjau.ps1` (otomasi Word lewat COM) terbukti gagal secara
konsisten pada naskah berukuran ~250 halaman ini: `Document.Repaginate()`
selalu melempar `COMException`, baik dengan `Word.Visible = $true` maupun
`$false`, dan `Document.Save()` sesudahnya menghasilkan `.docx` yang rusak
(jumlah halaman menggelembung dari ~248 menjadi 318 tanpa penjelasan).
Akar masalahnya diduga lingkungan otomasi tidak menyediakan permukaan
render yang dibutuhkan `Repaginate()`. **Jangan pakai `pratinjau.ps1`
sampai penyebabnya dipahami dan diperbaiki**; skrip `perbarui_daftar_lo.py`
memakai LibreOffice UNO API (`getDocumentIndexes()` lalu `.update()` pada
tiap indeks) dan terbukti berhasil bersih: seluruh 4 daftar terisi benar
dan `.docx`/PDF hasilnya sehat (260 halaman, wajar karena keempat daftar
kini berisi entri sungguhan, bukan lagi menggelembung tanpa sebab).

## Konvensi Markdown naskah

| Tulis di Markdown | Hasil di Word |
|---|---|
| `# BAB I.` lalu `# (JUDUL BAB)` pada berkas `bab-*.md` | `BukuJudulBab`, dua baris dalam satu paragraf, halaman baru |
| `# JUDUL` pada front/back matter | `BukuJudulHalaman` (tengah, tebal, bergaris bawah), halaman baru |
| `## A. Judul Bagian` | `BukuBagianA` |
| `### Label Blok:` | `BukuLabelBlok` (CPMK, Indikator, Rangkuman, Soal/Pertanyaan, dll.) |
| `#### 1. Judul` / `##### a. Judul` | `BukuSub1` / `BukuSub2` |
| paragraf biasa | `BukuIsi` (rata kanan-kiri, indentasi baris pertama 0,75 cm) |
| `- butir` / `1. butir` | butir berpoin `•` / daftar bernomor yang dimulai ulang tiap daftar |
| `*miring*`, `**tebal**`, `` `kode` `` | miring, tebal, Consolas |
| blok ```` ```java ```` | `BukuKode` (Consolas 9,5 pt, latar abu-abu, garis tepi) |
| `Kode Program #. Judul` (di atas listing) | keterangan bernomor otomatis, masuk Daftar Kode Program |
| `Tabel #. Judul` (di atas tabel) | keterangan bernomor otomatis, masuk Daftar Tabel |
| `![Gambar #. Judul](../gambar/berkas.png)` | gambar selebar teks + keterangan di bawahnya |
| tabel pipa `\| a \| b \|` | tabel Word, baris judul diulang dan tidak terpotong |
| `> [TAHAP 2] catatan` | kotak kuning penanda bagian yang belum ditulis |
| `<!-- halaman-baru -->` | paragraf berikutnya mulai di halaman baru |
| `<!-- gaya: NamaGaya -->` | blok berikutnya memakai gaya tersebut, satu baris satu paragraf |
| `<!-- daftar: isi\|gambar\|tabel\|kode -->` | field daftar otomatis |

Tanda `#` pada keterangan diganti nomor urut satu buku oleh field `SEQ`.
Format manual di Word dilarang; semua tampilan diatur lewat gaya.

## Catatan teknis

- Font kode **Consolas 9,5 pt**.
- JDK 21 portabel untuk uji kompilasi disimpan di `../.tools/` (tidak di-commit).
- Penomoran halaman: Romawi kecil mulai ii pada front matter, Arab mulai 1 pada Bab I.
