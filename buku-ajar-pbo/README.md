# Naskah Buku Ajar PBO

| Berkas / folder | Isi |
|---|---|
| `Buku-Ajar-PBO.docx` | Luaran utama. Saat ini masih **kerangka kosong**: front matter, 15 judul bab beserta lima blok pembuka, dan back matter. |
| `tools/build_docx.py` | Membangun ulang kerangka dan seluruh gaya Word dari nol. |
| `naskah/` | Draf Markdown per bab, satu berkas per bab (`bab-01.md` sampai `bab-15.md`). |
| `kode/` | Proyek Java per bab. Setiap listing di buku wajib berasal dari sini dan sudah diuji kompilasi pada JDK 21. |
| `gambar/` | Gambar dan diagram, penomoran berurutan satu buku. |

## Gaya Word yang tersedia

`BukuJudulBab`, `BukuBagianA`, `BukuSub1`, `BukuSub2`, `BukuIsi`, `BukuLabelBlok`,
`BukuKode`, `BukuKeteranganGambar`, `BukuKeteranganTabel`, `BukuPustaka`, `BukuGlosarium`.

Format manual dilarang. Gunakan gaya di atas.

## Catatan teknis

- Font kode memakai **Courier New 10 pt** karena Consolas tidak tersedia di macOS.
- Daftar Isi, Daftar Gambar, Daftar Tabel, dan Daftar Kode Program memakai field Word.
  Setelah naskah lengkap, buka berkas di Word lalu jalankan *Update Field*.
- Penomoran halaman: Romawi kecil pada front matter, Arab mulai 1 pada Bab I.
