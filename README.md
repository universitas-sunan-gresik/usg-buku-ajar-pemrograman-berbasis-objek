# Buku Ajar Pemrograman Berorientasi Objek

Repositori kerja penyusunan buku ajar mata kuliah **Pemrograman Berorientasi Objek (SI3C33)**,
Program Studi Sarjana Sistem Informasi, Fakultas Teknologi dan Rekayasa,
**Universitas Sunan Gresik**.

Penulis: Muhammad Muchson Attoyibi, S.Pd., M.Pd.

## Status

| Tahap | Keterangan | Status |
|---|---|---|
| 0 | Penyiapan aturan, kerangka repositori, dan gaya Word | **selesai** |
| 1 | Kerangka front matter dan 15 bab | berjalan |
| 2 | Penulisan isi Bab I sampai Bab XV | belum |
| 3 | Back matter: pustaka, glosarium, lampiran, biografi, sinopsis | belum |
| 4 | Perakitan naskah akhir ke satu berkas .docx | belum |
| 5 | Pemeriksaan akhir dan ekspor PDF pratinjau | belum |

Isi bab **belum ditulis**. Berkas `.docx` yang ada saat ini adalah kerangka kosong
yang sudah memakai seluruh standar tata letak.

## Struktur

```
.
├── ATURAN-BUKU-AJAR-PBO.md   aturan utama, mengikat seluruh penulisan
├── reference/                dokumen acuan (RPS dan contoh format buku ajar)
└── buku-ajar-pbo/            naskah dan luaran .docx
    ├── Buku-Ajar-PBO.docx    kerangka .docx sesuai standar
    ├── tools/build_docx.py   pembangun kerangka dan gaya Word
    ├── naskah/               draf Markdown per bab
    ├── kode/                 proyek Java yang diuji kompilasi
    └── gambar/               gambar dan diagram
```

## Aturan pokok

Seluruh keputusan penulisan tunduk pada [ATURAN-BUKU-AJAR-PBO.md](ATURAN-BUKU-AJAR-PBO.md).
Ringkasnya:

- **15 bab**, satu bab untuk satu butir Bahan Kajian pada RPS.
- Isi dan capaian mengikuti **RPS**; format dan struktur mengikuti **contoh buku ajar** di `reference/`.
- Halaman **15,5 x 23 cm**, badan teks **Arial 11 pt**, bukan A4.
- Studi kasus berkelanjutan: **Sistem Informasi Perpustakaan USG (SIP-USG)**.
- Lingkungan teknis: **JDK 21, Apache NetBeans, MySQL/MariaDB, JDBC, Swing**.

## Membangun ulang kerangka .docx

```bash
pip install python-docx
cd buku-ajar-pbo
python3 tools/build_docx.py
```
