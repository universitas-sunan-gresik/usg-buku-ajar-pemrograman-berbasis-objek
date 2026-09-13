# Buku Ajar Pemrograman Berorientasi Objek

Repositori kerja penyusunan buku ajar mata kuliah **Pemrograman Berorientasi Objek (SI3C33)**,
Program Studi Sarjana Sistem Informasi, Fakultas Teknologi dan Rekayasa,
**Universitas Sunan Gresik**.

Penulis: Muhammad Muchson Attoyibi, S.Pd., M.Pd.

## Status

| Tahap | Keterangan | Status |
|---|---|---|
| 0 | Penyiapan aturan, kerangka repositori, dan gaya Word | **selesai** |
| 1 | Kerangka front matter dan 15 bab | **selesai** |
| 2 | Penulisan isi Bab I sampai Bab XV | **selesai** |
| 3 | Back matter: pustaka, glosarium, lampiran, biografi, sinopsis | **selesai** |
| 4 | Perakitan naskah akhir ke satu berkas .docx | **selesai** |
| 5 | Pemeriksaan akhir dan ekspor PDF pratinjau | **selesai** |

Seluruh 15 bab telah ditulis lengkap (Blok 1–12 per bab, kode Java teruji kompilasi pada JDK 21,
diagram SVG asli, dan tangkapan layar GUI/keluaran program sungguhan), tidak ada lagi penanda
`[TAHAP n]` yang tersisa pada naskah. Back matter mencakup Daftar Pustaka (8 sumber wajib RPS),
Glosarium (100+ entri beralfabet), Lampiran A–D (kisi-kisi UTS/UAS, panduan proyek akhir, rubrik
ringkas), Biografi Penulis, dan Sinopsis Buku. Naskah lengkap ~248 halaman setelah dirakit.

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

## Membangun .docx dari naskah

```bash
pip install python-docx
cd buku-ajar-pbo
python tools/build_docx.py
```

Konvensi penulisan Markdown dan langkah pembaruan daftar isi ada di
[buku-ajar-pbo/README.md](buku-ajar-pbo/README.md).
