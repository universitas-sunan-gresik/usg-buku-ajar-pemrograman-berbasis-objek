# ATURAN PENYUSUNAN BUKU AJAR
## Pemrograman Berorientasi Objek (PBO)
### Universitas Sunan Gresik — Program Studi Sarjana Sistem Informasi

Dokumen ini adalah **aturan baku (rule book)** yang mengikat seluruh proses penulisan buku ajar
Pemrograman Berorientasi Objek. Setiap bab yang ditulis wajib lolos Checklist pada Bagian 12.

Status: **disetujui untuk dieksekusi** (penulisan bab belum dimulai).
Versi: 1.0 — 12 September 2026.

---

## 0. Sumber Acuan

| Kode | Dokumen | Peran |
|---|---|---|
| **[RPS]** | `RPS Pemrograman Berbasis Objek OBE.docx.pdf` (15 hlm.) | Sumber tunggal CPL, CPMK, Sub-CPMK, bahan kajian, matriks mingguan, tugas, bobot asesmen, dan rubrik R1–R14. **Tidak boleh diubah, ditambah, atau ditafsirkan ulang.** |
| **[REF]** | `BUKU AJAR_ Anatomi dan Fisiologi Manusia_ Informatika Kesehatan.pdf` (98 hlm.) | Sumber tunggal **format dan struktur**. Semua tata letak, urutan blok bab, penamaan bagian, dan komponen front/back matter meniru dokumen ini. **Isi/substansinya tidak dipakai.** |

Aturan konflik: jika [RPS] dan [REF] berbeda, **[RPS] menang untuk isi dan capaian**, **[REF] menang untuk format dan struktur**.

---

## 1. Identitas Buku

| Butir | Ketetapan |
|---|---|
| Judul utama | **PEMROGRAMAN BERORIENTASI OBJEK** |
| Anak judul | **Konsep, Pemodelan UML, dan Implementasi Java untuk Sistem Informasi** |
| Penulis | Muhammad Muchson Attoyibi, S.Pd., M.Pd. (NUPTK 4846772673130330) |
| Jenis buku | Buku Ajar |
| Mata kuliah | Pemrograman Berorientasi Objek, kode **SI3C33**, semester 3, **4 SKS (T=3, P=1)** |
| Program studi | Sarjana Sistem Informasi, Fakultas Teknologi dan Rekayasa, USG |
| Sasaran pembaca | Mahasiswa semester 3 yang telah lulus Struktur Data dan Algoritma & Pemrograman |
| Bahasa | Bahasa Indonesia baku; istilah teknis Inggris dipertahankan dan dicetak miring |
| Jumlah bab | **15 bab** (satu bab = satu butir Bahan Kajian [RPS]) |
| Target tebal | 240–290 halaman isi (lihat Bagian 11) |
| Luaran akhir | **satu berkas `.docx`** siap penerbit + PDF pratinjau |
| Tahun terbit | Cetakan I, 2026 — Gresik |

**Studi kasus utama (running case):** *Sistem Informasi Perpustakaan Universitas Sunan Gresik* (disingkat **SIP-USG**).
Kasus ini dipakai berurutan dari Bab 1 sampai Bab 15 sehingga kode program bab ke-n adalah kelanjutan bab ke-(n−1).
**Studi kasus pembanding** untuk soal latihan: *Toko Daring Sederhana* (sesuai contoh pada Rancangan Tugas [RPS]).

**Lingkungan teknis yang dibakukan di seluruh buku:**
Java SE **JDK 21** (LTS), IDE **Apache NetBeans**, basis data **MySQL/MariaDB** melalui **JDBC**, GUI memakai **Java Swing**.
Tidak boleh berpindah teknologi di tengah buku (mis. tidak memakai JavaFX di satu bab dan Swing di bab lain).

---

## 2. Spesifikasi Fisik Berkas Word

Diambil dari pengukuran langsung [REF]. Semua angka bersifat wajib.

| Elemen | Ketetapan |
|---|---|
| Ukuran halaman | **15,5 cm × 23 cm** (standar UNESCO, bukan A4) |
| Margin | Atas 2 cm, Bawah 2 cm, Dalam (kiri) 2,5 cm, Luar (kanan) 1,8 cm; *mirror margins* aktif |
| Font isi | **Arial 11 pt**, rata kanan-kiri (*justify*) |
| Spasi baris | 1,15; spasi antarparagraf 6 pt; indentasi baris pertama 0,75 cm |
| Judul bab baris 1 | Arial **Bold 16 pt**, kapital, rata kiri, format `BAB I.` |
| Judul bab baris 2 | Arial **Bold 16 pt**, kapital, **di dalam tanda kurung**, contoh `(PARADIGMA PEMROGRAMAN BERORIENTASI OBJEK)` |
| Judul bagian (A, B, C…) | Arial **Bold 12 pt**, format `A. Judul Bagian` (huruf kapital di awal kata) |
| Sub-bagian tingkat 2 | Arial **Bold 11 pt**, format `1. Judul` |
| Sub-bagian tingkat 3 | Arial 11 pt, format `a. Judul` |
| Label blok bab | Arial **Bold 11 pt** diakhiri titik dua, contoh `Indikator Penilaian:` |
| Butir berpoin | Bullet `•` Symbol 11 pt, indentasi 0,75 cm |
| Nomor halaman | Bawah-tengah, Arial 10 pt |
| Penomoran front matter | Angka Romawi kecil (ii, iii, iv, …) |
| Penomoran isi | Angka Arab mulai **1** pada halaman pertama Bab 1 |
| Header/footer teks | Tidak ada header berjalan (mengikuti [REF]) |
| Awal bab | Selalu mulai di **halaman baru** (*page break*) |
| Daftar isi | Otomatis (field TOC Word), 1 level bab + level A/B/C |

**Gaya Word yang wajib dibuat** (jangan format manual):
`BukuJudulBab`, `BukuBagianA`, `BukuSub1`, `BukuSub2`, `BukuIsi`, `BukuLabelBlok`,
`BukuKode`, `BukuKeteranganGambar`, `BukuKeteranganTabel`, `BukuPustaka`, `BukuGlosarium`.

**Gaya khusus `BukuKode` (listing program Java):**
Consolas 9,5 pt, spasi 1,0, rata kiri (tanpa *justify*), latar abu-abu 5 %,
garis tepi tipis 0,5 pt, indentasi kiri 0,5 cm, **penomoran baris tidak dipakai** (agar mudah disalin mahasiswa),
lebar maksimum **64 karakter per baris** supaya tidak terpotong pada halaman 15,5 cm.

**Prasyarat teknis produksi:** `pip install python-docx` (belum terpasang di mesin ini),
font Arial tersedia di macOS. Consolas tidak tersedia di macOS — gunakan **Courier New 10 pt** sebagai pengganti resmi jika Consolas tidak terpasang, dan konsisten di seluruh buku.

---

## 3. Struktur Buku (urutan berkas)

Mengikuti [REF] secara berurutan.

**Front Matter** (Romawi kecil)
1. Halaman judul (sampul dalam) — judul, anak judul, nama penulis lengkap gelar
2. Halaman identitas terbitan — penulis, editor, tim penata letak, tim penyelaras naskah, tim perancang sampul, jenis buku, ISBN, penerbit, redaksi (alamat Kampus A USG), hak cipta, cetakan
3. Halaman sanksi pelanggaran — **Pasal 113 UU No. 28 Tahun 2014 tentang Hak Cipta** (4 ayat, disalin persis seperti [REF])
4. **KATA PENGANTAR** (2 halaman) — ditutup "Gresik, … 2026 / Penulis"
5. **PRAKATA PENULIS** (2–3 halaman) — latar belakang, visi keilmuan, tujuan, sasaran pembaca, ikhtisar 15 bab, ucapan terima kasih, ditutup nama penulis
6. **DAFTAR ISI**
7. **DAFTAR GAMBAR**
8. **DAFTAR TABEL**
9. **DAFTAR KODE PROGRAM**

**Isi** (Arab, 15 bab) — lihat Bagian 5 dan 8.

**Back Matter**
10. **DAFTAR PUSTAKA**
11. **GLOSARIUM** — dikelompokkan per huruf abjad (A, B, C, …), minimal **70 entri**
12. **LAMPIRAN A. Kisi-kisi dan Latihan Komprehensif UTS** (cakupan Sub-CPMK1–5, sesuai Mg 8 [RPS])
13. **LAMPIRAN B. Kisi-kisi dan Latihan Komprehensif UAS** (cakupan Sub-CPMK6–8, sesuai Mg 16 [RPS])
14. **LAMPIRAN C. Panduan Proyek Akhir** (Tugas 4 [RPS]: aplikasi OOP + GUI + basis data, kelompok 3–4 mahasiswa, rubrik R9, R8, R13)
15. **LAMPIRAN D. Rubrik Penilaian Ringkas** (R1, R3, R8, R9, R10, R13, R14 disalin ringkas dari [RPS] 6.4)
16. **BIOGRAFI PENULIS** (dengan pasfoto, ±1 halaman, ditutup alamat surel resmi)
17. **SINOPSIS BUKU** (1 halaman, 2 paragraf, untuk sampul belakang)

Lampiran A–D adalah **penambahan yang diizinkan** terhadap kerangka [REF] karena [RPS] mensyaratkan UTS, UAS, proyek, dan rubrik. Selain itu, tidak ada penambahan komponen lain.

---

## 4. Anatomi Wajib Setiap Bab

Urutan blok **tidak boleh diubah, tidak boleh dilewati**. Blok 1–5 meniru [REF] apa adanya; blok 6–12 adalah badan bab.

| # | Blok | Ketentuan |
|---|---|---|
| 1 | `BAB <Romawi>.` + `(JUDUL BAB)` | Dua baris, Bold 16 pt, kapital, judul dalam kurung |
| 2 | `CPMK/ Sub-CPMK :` | Dua butir bullet: satu CPMK dan satu Sub-CPMK, **disalin verbatim dari [RPS]** |
| 3 | `Indikator Penilaian:` | Satu paragraf; disalin/diturunkan dari kolom Indikator pada Matriks Mingguan [RPS] |
| 4 | `Kriteria Keberhasilan (Rubrik):` | Tiga bullet: **Sangat Baik (≥ 85)**, **Baik (70–84)**, **Cukup (55–69)**. Rentang angka persis seperti [REF]. Isi deskriptor dikaitkan dengan rubrik [RPS] yang berlaku pada minggu tersebut (kolom "Rubrik" pada Bagian 7) |
| 5 | `Deskripsi Kemampuan yang Diharapkan:` | 1 paragraf, diawali "Setelah mempelajari bab ini, mahasiswa diharapkan…", wajib menyebut manfaat pada konteks **Sistem Informasi** |
| 6 | `A. Pendahuluan` | 2–3 paragraf: masalah nyata → mengapa konsep bab ini diperlukan → apa yang akan dipelajari. Wajib memuat 1 kalimat *WIIFM* ("apa untungnya bagi mahasiswa") |
| 7 | `B.` … `F.` Materi inti | 4–6 bagian. Setiap bagian: penjelasan konsep → ilustrasi/analogi → **Kode Program** → pembacaan baris demi baris → keluaran program |
| 8 | Bagian menjelang akhir: `Praktikum Terbimbing` | Selalu menjadi **bagian huruf terakhir sebelum Rangkuman** (mis. `F. Praktikum Terbimbing`). Berisi langkah bernomor di NetBeans, 5–10 langkah, hasil akhir yang bisa dijalankan, dan penggalan **SIP-USG** |
| 9 | `Kesalahan Umum dan Cara Mengatasinya` | Tabel 3 kolom: Gejala/pesan *error* — Penyebab — Perbaikan. Minimal **4 baris**. Ditempatkan sebagai sub-bagian terakhir dari blok Praktikum Terbimbing |
| 10 | `Rangkuman` | 1 paragraf padat 120–180 kata (meniru [REF]), tanpa bullet |
| 11 | `Soal/Pertanyaan` | Daftar bernomor **6–8 butir**, berjenjang: 2 soal pemahaman (C2), 3 soal penerapan/analisis kode (C3–C4), 1–2 soal perancangan/sintesis (C5–C6), **wajib 1 soal berkonteks SIP-USG** |
| 12 | `Rujukan Bab` | Daftar ringkas 2–4 sumber yang dipakai pada bab itu, diambil **hanya** dari Daftar Pustaka [RPS] |

Blok 9 dan 12 adalah penyesuaian untuk mata kuliah pemrograman; sisanya identik dengan pola [REF].

---

## 5. Aturan Khusus Materi Pemrograman

**Kode program**
- Setiap listing diberi label `Kode Program <n>. <Judul>` **di atas** blok kode (penomoran berurutan satu buku, 1..n).
- Kode wajib **dapat dikompilasi apa adanya** pada JDK 21. Tidak boleh ada potongan `...` di tengah kode yang membuatnya gagal dijalankan; jika perlu memendekkan, tulis komentar `// ... lanjutan pada Kode Program n`.
- Bahasa identifier: **Inggris** (`Book`, `borrowDate`, `getTitle()`), komentar: **Indonesia**.
- Konvensi penamaan Java wajib: kelas `PascalCase`, method dan variabel `camelCase`, konstanta `UPPER_SNAKE_CASE`, paket `id.ac.usg.sip`.
- Setiap listing **wajib diikuti** blok `Keluaran Program:` berisi keluaran konsol yang sebenarnya.
- Maksimum **40 baris** per listing. Lebih dari itu, pecah menjadi beberapa listing.
- Panjang baris maksimum **64 karakter**.

**Gambar dan diagram**
- Label `Gambar <n>. <Judul>` diletakkan **di bawah** gambar, rata tengah, Arial 10 pt; penomoran berurutan satu buku.
- Diagram UML wajib mengikuti notasi UML 2.x: kotak tiga kompartemen, `+ - #` untuk visibilitas, panah pewarisan segitiga kosong, asosiasi/agregasi/komposisi sesuai [RPS] Materi 4.
- Setiap bab **wajib memuat minimal 1 diagram** (UML kelas, alur objek, hierarki, atau diagram relasi konsep).
- Gambar hasil tangkapan layar NetBeans: resolusi minimal 150 dpi, dipotong hanya pada area yang relevan.
- Gambar dari sumber luar wajib mencantumkan `Sumber: (Penulis, tahun)` di bawah keterangan.

**Tabel**
- Label `Tabel <n>. <Judul>` diletakkan **di atas** tabel, rata tengah, Arial 10 pt; penomoran berurutan satu buku.
- Isi tabel Arial 10 pt, spasi 1,0. Tabel tidak boleh terpotong antarhalaman; jika panjang, ulangi baris judul.

**Analogi dan ilustrasi konseptual**
- Setiap konsep abstrak (objek, enkapsulasi, polimorfisme, interface, pola desain) wajib disertai **satu analogi dunia nyata** berlatar administrasi kampus atau perpustakaan, bukan analogi acak.

---

## 6. Aturan Bahasa dan Gaya

1. Bahasa Indonesia baku sesuai PUEBI. Sudut pandang: **mahasiswa sebagai pembaca** ("mahasiswa dapat…", "Anda akan…"), bukan "kita" kecuali pada Kata Pengantar dan Prakata.
2. Istilah Inggris yang dipertahankan ditulis **miring** pada kemunculan pertama di setiap bab, lalu tegak: *inheritance*, *polymorphism*, *interface*, *exception*.
3. Padanan Indonesia didahulukan bila baku: pewarisan (*inheritance*), polimorfisme, enkapsulasi, penanganan eksepsi, koleksi, antarmuka grafis.
4. Panjang paragraf 4–7 kalimat. Hindari paragraf satu kalimat.
5. Tidak memakai kata ganti orang pertama tunggal di badan bab.
6. Tidak memakai emoji, tidak memakai tanda seru berlebihan, tidak memakai gaya tutur blog.
7. Sitasi dalam teks gaya **APA 7**: (Deitel & Deitel, 2018); (Horstmann, 2022, hlm. 145).
8. Daftar Pustaka disusun alfabetis, *hanging indent* 0,75 cm, **hanya memuat sumber yang benar-benar disitasi**, dan **seluruh 8 pustaka [RPS] wajib muncul**:
   Deitel & Deitel (2018); Horstmann (2022); Bloch (2018); Kadir (2012); Gamma dkk. (1994); Oracle (2024) *Java Tutorials*; Oracle (2023) *JDK 21 Documentation*; Apache Software Foundation (2024) *NetBeans Documentation*.
   Penambahan pustaka di luar daftar itu maksimal **5 sumber**, harus terbitan 2018 ke atas, dan dicatat pada berkas `CATATAN-PUSTAKA-TAMBAHAN.md`.
9. Tidak menyalin teks dari sumber mana pun. Seluruh naskah ditulis ulang; kutipan langsung maksimal 25 kata dan wajib memakai tanda kutip beserta sumber.

---

## 7. Peta Induk: 15 Bab ↔ RPS

Kolom minggu, Sub-CPMK, CPMK, rubrik, dan bobot diambil langsung dari Matriks Pembelajaran Mingguan [RPS].

| Bab | Judul Bab | Bahan Kajian [RPS] | Mg | Sub-CPMK | CPMK | Rubrik | Bobot Mg |
|---|---|---|---|---|---|---|---|
| I | Paradigma Pemrograman Berorientasi Objek | 1 | 1 | Sub-CPMK1 | CPMK2 | R1 | 4 % |
| II | Kelas, Objek, Atribut, Method, dan Constructor | 2 | 2 | Sub-CPMK1 | CPMK2 | R10 | 5 % |
| III | Enkapsulasi, Access Modifier, dan Information Hiding | 3 | 3 | Sub-CPMK2 | CPMK2 | R10 | 5 % |
| IV | Pemodelan Berorientasi Objek dengan Diagram Kelas UML | 4 | 4 | Sub-CPMK3 | CPMK1 | R10 (Tugas 1) | 5 % |
| V | Pewarisan (Inheritance) | 5 | 5 | Sub-CPMK4 | CPMK2 | R10 | 5 % |
| VI | Polimorfisme (Polymorphism) | 6 | 6 | Sub-CPMK4 | CPMK2 | R3 + R10 (Kuis 1) | 5 % |
| VII | Abstraksi: Abstract Class dan Interface | 7 | 7 | Sub-CPMK5 | CPMK2 | R10 (Tugas 2) | 5 % |
| VIII | Penanganan Eksepsi (Exception Handling) | 8 | 9 | Sub-CPMK6 | CPMK2 | R10 | 4 % |
| IX | Collection Framework dan Generics | 9 | 10 | Sub-CPMK6 | CPMK2 | R3 + R10 (Kuis 2) | 4 % |
| X | Operasi Berkas dan Object Persistence | 10 | 11 | Sub-CPMK7 | CPMK3 | R10 | 5 % |
| XI | Koneksi Basis Data (JDBC) dan Operasi CRUD | 11 | 12 | Sub-CPMK7 | CPMK3 | R10 (Tugas 3) | 5 % |
| XII | Antarmuka Grafis (GUI) dan Event Handling | 12 | 13 | Sub-CPMK7 | CPMK3 | R10 | 4 % |
| XIII | Prinsip Desain Berorientasi Objek (SOLID) | 13 | 14 | Sub-CPMK8 | CPMK4 | R9 | 4 % (bersama Bab XIV) |
| XIV | Pengantar Design Pattern: Singleton, Factory, MVC | 14 | 14 | Sub-CPMK8 | CPMK4 | R9 | — |
| XV | Integrasi Konsep dalam Proyek Aplikasi Berorientasi Objek | 15 | 15 | Sub-CPMK8 | CPMK3 & CPMK4 | R9, R8, R13 (Tugas 4) | 5 % |

**Minggu 8 (UTS, 15 %)** dilayani oleh **Lampiran A**; **Minggu 16 (UAS, 20 %)** dilayani oleh **Lampiran B dan C**.

**Bunyi CPMK yang disalin verbatim ke blok 2 setiap bab:**
- **CPMK1** — Mahasiswa mampu merancang model berorientasi objek (kelas, objek, dan relasi antarkelas) menggunakan diagram kelas UML secara tepat.
- **CPMK2** — Mahasiswa mampu mengimplementasikan konsep pemrograman berorientasi objek (enkapsulasi, pewarisan, polimorfisme, abstraksi, interface, penanganan eksepsi, collection, dan generics) dalam bahasa Java untuk menyelesaikan masalah.
- **CPMK3** — Melalui proyek pemrograman, mahasiswa mampu membangun aplikasi berorientasi objek yang terintegrasi dengan basis data dan antarmuka grafis (GUI) sebagai produk.
- **CPMK4** — Mahasiswa mampu berkolaborasi secara efektif dan etis dalam merancang, mengembangkan, mendokumentasikan, dan mempresentasikan produk aplikasi berorientasi objek.

**Bunyi Sub-CPMK yang disalin verbatim:**
- **Sub-CPMK1** — menjelaskan paradigma OOP serta menerapkan konsep kelas dan objek (atribut, method, constructor) dalam bahasa Java.
- **Sub-CPMK2** — menerapkan enkapsulasi dan information hiding melalui access modifier dan getter/setter.
- **Sub-CPMK3** — merancang model berorientasi objek menggunakan diagram kelas UML beserta relasi antarkelas.
- **Sub-CPMK4** — mengimplementasikan pewarisan (inheritance) dan polimorfisme (polymorphism) dalam bahasa Java.
- **Sub-CPMK5** — menerapkan abstraksi melalui abstract class dan interface.
- **Sub-CPMK6** — mengimplementasikan penanganan eksepsi (exception handling), collection, dan generics.
- **Sub-CPMK7** — membangun aplikasi berorientasi objek yang terintegrasi dengan operasi berkas/persistence, basis data (JDBC/CRUD), dan antarmuka grafis (GUI).
- **Sub-CPMK8** — menerapkan prinsip desain berorientasi objek (SOLID/design pattern) serta mengembangkan dan mempresentasikan proyek aplikasi berorientasi objek secara kolaboratif.

---

## 8. Gambaran Isi Setiap Bab

Setiap bab di bawah ini sudah memakai kerangka blok Bagian 4. Yang dicantumkan hanya bagian A–F, rencana gambar, listing, dan penanda SIP-USG.

### BAB I — (PARADIGMA PEMROGRAMAN BERORIENTASI OBJEK)
A. Pendahuluan · B. Keterbatasan Paradigma Prosedural · C. Gagasan Dasar Paradigma Berorientasi Objek ·
D. Empat Pilar OOP: Enkapsulasi, Pewarisan, Polimorfisme, Abstraksi (pengenalan) ·
E. Ekosistem Java: JDK, JRE, JVM, dan Siklus Kompilasi · F. Praktikum Terbimbing: Instalasi JDK 21 dan NetBeans, program `HelloUSG`
Gambar: perbandingan alur prosedural vs objek; siklus `.java → javac → .class → JVM`; peta empat pilar.
Kode: 3 listing (program prosedural, padanan berorientasi objek, HelloUSG).
SIP-USG: pengenalan kasus dan daftar entitas yang akan dibangun sepanjang buku.

### BAB II — (KELAS, OBJEK, ATRIBUT, METHOD, DAN CONSTRUCTOR)
A. Pendahuluan · B. Kelas sebagai Cetak Biru dan Objek sebagai Instans · C. Atribut dan Tipe Data ·
D. Method: Deklarasi, Parameter, dan Nilai Kembali · E. Constructor, Overloading Constructor, dan Kata Kunci `this` ·
F. Praktikum Terbimbing: Membangun kelas `Book` dan `Member` pada SIP-USG
Gambar: kelas vs objek; peta memori *stack/heap* saat `new`.
Kode: 6 listing. Tabel: tipe data primitif Java.

### BAB III — (ENKAPSULASI, ACCESS MODIFIER, DAN INFORMATION HIDING)
A. Pendahuluan · B. Konsep Enkapsulasi dan Information Hiding · C. Access Modifier: private, default, protected, public ·
D. Getter, Setter, dan Validasi Data di Dalam Setter · E. Immutability dan Praktik Baik Bloch (2018) ·
F. Praktikum Terbimbing: Mengamankan `Member` dan validasi nomor induk mahasiswa
Gambar: lapisan akses kelas; ilustrasi "kotak hitam".
Kode: 5 listing. Tabel: matriks visibilitas access modifier.

### BAB IV — (PEMODELAN BERORIENTASI OBJEK DENGAN DIAGRAM KELAS UML)
A. Pendahuluan · B. Notasi Kelas, Atribut, Method, dan Visibilitas · C. Relasi Antarkelas: Asosiasi, Agregasi, Komposisi ·
D. Multiplisitas, Dependensi, dan Generalisasi · E. Dari Diagram Kelas ke Kode Java (dan sebaliknya) ·
F. Praktikum Terbimbing: Diagram kelas lengkap SIP-USG
Gambar: 4 diagram UML (notasi dasar, tiga jenis relasi, multiplisitas, diagram kelas SIP-USG penuh).
Kode: 3 listing hasil penerjemahan diagram.
**Catatan asesmen:** bab ini menopang **Tugas 1 [RPS]** (individu, dikumpulkan Mg 5, luaran dokumen PDF diagram kelas).

### BAB V — (PEWARISAN / INHERITANCE)
A. Pendahuluan · B. Superclass, Subclass, dan Kata Kunci `extends` · C. Kata Kunci `super` pada Constructor dan Method ·
D. Override Method dan Anotasi `@Override` · E. Kelas `Object`, `final`, dan Batas Kewajaran Hierarki ·
F. Praktikum Terbimbing: Hierarki `LibraryItem → Book, Journal, DigitalItem`
Gambar: hierarki kelas SIP-USG; urutan pemanggilan constructor.
Kode: 6 listing.

### BAB VI — (POLIMORFISME / POLYMORPHISM)
A. Pendahuluan · B. Overloading (polimorfisme statis) · C. Overriding (polimorfisme dinamis) ·
D. Dynamic Binding, Upcasting, Downcasting, dan `instanceof` · E. Polimorfisme melalui Referensi Superclass pada Koleksi Objek ·
F. Praktikum Terbimbing: Method `calculateFine()` yang berperilaku berbeda per jenis koleksi
Gambar: pengikatan statis vs dinamis; alur pemilihan method saat *runtime*.
Kode: 6 listing. Tabel: beda overloading dan overriding.
**Catatan asesmen:** bab ini menopang **Kuis 1 (Mg 6, rubrik R3)**.

### BAB VII — (ABSTRAKSI: ABSTRACT CLASS DAN INTERFACE)
A. Pendahuluan · B. Abstract Class dan Abstract Method · C. Interface: Kontrak Perilaku ·
D. Default Method, Static Method, dan Functional Interface (Java 8+) · E. Memilih Abstract Class atau Interface ·
F. Praktikum Terbimbing: Interface `Borrowable` dan `Printable` pada SIP-USG
Gambar: diagram UML abstract class vs interface; pohon keputusan pemilihan.
Kode: 6 listing. Tabel: perbandingan abstract class dan interface.
**Catatan asesmen:** bab ini menopang **Tugas 2 [RPS]** (Mg 7, dikumpulkan Mg 8, luaran `.java` + laporan PDF) dan menutup cakupan **UTS**.

### BAB VIII — (PENANGANAN EKSEPSI / EXCEPTION HANDLING)
A. Pendahuluan · B. Hierarki `Throwable`: Error, Checked, dan Unchecked Exception ·
C. `try-catch-finally` dan `try-with-resources` · D. `throw`, `throws`, dan Perambatan Eksepsi ·
E. Custom Exception dan Pesan Kesalahan yang Bermakna ·
F. Praktikum Terbimbing: `BookNotAvailableException` pada proses peminjaman
Gambar: hierarki `Throwable`; alur eksekusi try-catch-finally.
Kode: 6 listing. Tabel: eksepsi umum Java dan pemicunya.

### BAB IX — (COLLECTION FRAMEWORK DAN GENERICS)
A. Pendahuluan · B. Arsitektur Collection Framework: Collection, List, Set, Map ·
C. `ArrayList`, `LinkedList`, `HashSet`, `HashMap`: karakteristik dan pemilihan ·
D. Generics: Type Parameter, Bounded Type, dan Type Safety ·
E. Iterasi, `Comparable`/`Comparator`, dan Pengurutan Objek ·
F. Praktikum Terbimbing: Katalog SIP-USG berbasis `Map<String, Book>` dengan pengurutan
Gambar: hierarki antarmuka Collection; struktur `HashMap`.
Kode: 7 listing. Tabel: perbandingan kompleksitas dan kasus pakai tiap koleksi.
**Catatan asesmen:** bab ini menopang **Kuis 2 (Mg 10, rubrik R3)**.

### BAB X — (OPERASI BERKAS DAN OBJECT PERSISTENCE)
A. Pendahuluan · B. Aliran Data Java: Byte Stream dan Character Stream · C. Membaca dan Menulis Berkas Teks serta CSV ·
D. Serialization dan Deserialization Objek · E. NIO.2 (`Path`, `Files`) dan Penanganan Eksepsi Berkas ·
F. Praktikum Terbimbing: Menyimpan dan memuat ulang katalog SIP-USG ke berkas `.dat` dan `.csv`
Gambar: alur aliran data; proses serialisasi objek.
Kode: 6 listing. Tabel: pemilihan kelas I/O menurut kebutuhan.

### BAB XI — (KONEKSI BASIS DATA / JDBC DAN OPERASI CRUD)
A. Pendahuluan · B. Arsitektur JDBC, Driver, dan Connection String · C. `Statement`, `PreparedStatement`, dan `ResultSet` ·
D. Operasi CRUD Berorientasi Objek · E. Pola DAO dan Pemisahan Lapisan Data ·
F. Praktikum Terbimbing: `BookDAO` lengkap terhadap basis data `sip_usg`
Gambar: arsitektur aplikasi–JDBC–DBMS; diagram kelas lapisan DAO.
Kode: 7 listing termasuk skrip SQL pembuatan tabel. Tabel: pemetaan tipe Java ↔ tipe SQL.
**Catatan asesmen:** bab ini menopang **Tugas 3 [RPS]** (Mg 12, dikumpulkan Mg 13, luaran `.java` + laporan PDF).

### BAB XII — (ANTARMUKA GRAFIS / GUI DAN EVENT HANDLING)
A. Pendahuluan · B. Komponen Swing dan Hierarki Container · C. Layout Manager ·
D. Event Handling: Listener, Event Object, dan Lambda · E. Menghubungkan Form dengan Lapisan DAO ·
F. Praktikum Terbimbing: Form data buku SIP-USG dengan tabel dan tombol CRUD
Gambar: hierarki komponen Swing; rancangan tata letak form; tangkapan layar form jadi.
Kode: 6 listing. Tabel: komponen Swing yang paling sering dipakai.

### BAB XIII — (PRINSIP DESAIN BERORIENTASI OBJEK / SOLID)
A. Pendahuluan · B. Single Responsibility dan Open-Closed · C. Liskov Substitution ·
D. Interface Segregation dan Dependency Inversion · E. Code Smell dan Refactoring Terarah ·
F. Praktikum Terbimbing: Refactoring kelas `LibraryService` agar memenuhi SOLID
Gambar: diagram UML sebelum dan sesudah refactoring (dua gambar berpasangan).
Kode: 6 listing berpasangan (sebelum/sesudah). Tabel: lima prinsip, gejala pelanggaran, dan perbaikannya.

### BAB XIV — (PENGANTAR DESIGN PATTERN: SINGLETON, FACTORY, MVC)
A. Pendahuluan · B. Konsep Design Pattern dan Klasifikasi Gamma dkk. (1994) ·
C. Singleton: Kasus Koneksi Basis Data · D. Factory Method: Pembuatan Objek Koleksi Perpustakaan ·
E. Arsitektur MVC pada Aplikasi Swing + JDBC ·
F. Praktikum Terbimbing: Menyusun ulang SIP-USG ke dalam paket `model`, `view`, `controller`
Gambar: diagram UML Singleton; diagram UML Factory; diagram alur MVC.
Kode: 6 listing. Tabel: pola, masalah yang diselesaikan, dan contoh di SIP-USG.

### BAB XV — (INTEGRASI KONSEP DALAM PROYEK APLIKASI BERORIENTASI OBJEK)
A. Pendahuluan · B. Peta Integrasi Seluruh Konsep Bab 1–14 · C. Tahapan Pengembangan Proyek: Analisis, Perancangan, Implementasi, Pengujian ·
D. Dokumentasi Proyek dan Etika Kolaborasi (kerja kelompok, atribusi kontribusi, integritas akademik) ·
E. Presentasi dan Diseminasi Produk · F. Praktikum Terbimbing: Merakit SIP-USG versi akhir dan menyiapkan demonstrasi
Gambar: diagram arsitektur akhir SIP-USG; peta relasi seluruh konsep OOP; lini masa proyek Mg 9–16.
Kode: 4 listing integratif. Tabel: daftar periksa kesiapan produk proyek.
**Catatan asesmen:** bab ini menopang **Tugas 4 [RPS]** (kelompok 3–4 mahasiswa, dikembangkan Mg 9–15, dipresentasikan Mg 16; dinilai dengan R9 60 %, R8 25 %, R13 15 %) dan **UAS**.

---

## 9. Aturan Keselarasan dengan Asesmen RPS

1. Setiap soal pada blok `Soal/Pertanyaan` wajib dapat dipetakan ke Sub-CPMK bab tersebut. Tidak boleh ada soal di luar cakupan Sub-CPMK bab.
2. Bobot penilaian **tidak boleh diubah** di dalam buku. Yang dicantumkan hanya bobot resmi [RPS]: Partisipasi 10 %, Proyek 25 %, Kuis 10 %, Tugas 20 %, UTS 15 %, UAS 20 %.
3. Rentang nilai akhir yang boleh dicetak di Lampiran D hanya yang tertulis di [RPS]: A 86–100; AB 78–85; B 70–77; BC 62–69; C 54–61; D 40–53; E 0–39.
4. Skala kinerja rubrik yang dipakai: 4 Sangat Baik, 3 Baik, 2 Cukup, 1 Kurang, 0 Tidak Ada Bukti, dengan rumus `Nilai Asesmen = Σ (Skor Kinerja ÷ 4 × Bobot Kriteria)`.
5. Blok `Kriteria Keberhasilan (Rubrik)` di dalam bab memakai rentang persentase gaya [REF] (≥85 / 70–84 / 55–69) dan **tidak menggantikan** rubrik resmi [RPS]; hubungan keduanya dijelaskan satu paragraf di Lampiran D.
6. Empat tugas [RPS] muncul utuh, masing-masing pada bab penopangnya (Bab IV, VII, XI, XV) dalam kotak `Catatan Asesmen` berisi: nama tugas, Sub-CPMK, ruang lingkup, cara pengerjaan, batas waktu, dan luaran.

---

## 10. Aturan Konsistensi Antarbab

1. **Kesinambungan kode:** kelas yang diperkenalkan di bab awal dipakai ulang, bukan ditulis ulang dari nol. Jika sebuah kelas berubah, tulis `// Perubahan dari Bab <n>: …`.
2. **Rujukan silang:** memakai frasa "sebagaimana dibahas pada Bab V", bukan nomor halaman.
3. **Glosarium:** setiap istilah teknis yang dicetak miring pertama kali wajib masuk Glosarium.
4. **Peta konsep:** Bab I memuat peta seluruh isi buku; Bab XV memuat peta yang sama dalam keadaan terisi penuh.
5. **Tingkat kesulitan:** naik bertahap. Bab I–IV tanpa asumsi pengetahuan OOP; Bab V–IX mengandaikan Bab I–IV; Bab X–XV mengandaikan seluruh bab sebelumnya.
6. **Nama berkas contoh:** `NamaKelas.java` konsisten dengan nama kelas di dalamnya.

---

## 11. Estimasi Tebal

| Bagian | Halaman |
|---|---|
| Front matter | 11 |
| Bab I–III (fondasi) | 3 × 14 = 42 |
| Bab IV (UML) | 16 |
| Bab V–VII (relasi antarkelas) | 3 × 15 = 45 |
| Bab VIII–IX (ketangguhan & koleksi) | 2 × 14 = 28 |
| Bab X–XII (data & antarmuka) | 3 × 17 = 51 |
| Bab XIII–XIV (desain) | 2 × 14 = 28 |
| Bab XV (integrasi) | 16 |
| Daftar Pustaka + Glosarium | 9 |
| Lampiran A–D | 16 |
| Biografi + Sinopsis | 3 |
| **Total** | **± 265 halaman** |

Toleransi per bab ±3 halaman. Bab tidak boleh kurang dari 12 halaman.

---

## 12. Checklist Mutu per Bab

Bab dinyatakan selesai hanya jika seluruh butir tercentang.

- [ ] Judul bab dua baris, baris kedua di dalam kurung dan kapital
- [ ] Blok 1–5 lengkap dan berurutan; CPMK/Sub-CPMK verbatim [RPS]
- [ ] Kriteria Keberhasilan memuat tepat tiga level (≥85 / 70–84 / 55–69)
- [ ] Bagian A adalah Pendahuluan; bagian huruf terakhir adalah Praktikum Terbimbing
- [ ] Ada tabel `Kesalahan Umum dan Cara Mengatasinya` minimal 4 baris
- [ ] Ada `Rangkuman` satu paragraf 120–180 kata
- [ ] Ada `Soal/Pertanyaan` 6–8 butir berjenjang C2–C6, minimal satu berkonteks SIP-USG
- [ ] Ada `Rujukan Bab` 2–4 sumber, semuanya ada di Daftar Pustaka
- [ ] Minimal 1 diagram; seluruh gambar bernomor urut dan berketerangan di bawah
- [ ] Seluruh listing bernomor urut, ≤40 baris, ≤64 karakter per baris, dan **sudah diuji kompilasi pada JDK 21**
- [ ] Setiap listing diikuti `Keluaran Program:`
- [ ] Kode SIP-USG menyambung dari bab sebelumnya
- [ ] Istilah asing miring pada kemunculan pertama dan masuk Glosarium
- [ ] Panjang bab 12–20 halaman
- [ ] Tidak ada kalimat hasil salinan langsung dari sumber mana pun

---

## 13. Alur Produksi

1. **Tahap 0 — Persiapan.** Pasang `python-docx`. Siapkan berkas gaya Word. Verifikasi Arial dan Courier New.
2. **Tahap 1 — Kerangka.** Susun front matter dan kerangka 15 bab beserta blok 1–5 setiap bab. Ditinjau penulis sebelum lanjut.
3. **Tahap 2 — Penulisan isi.** Satu bab per iterasi, urut Bab I → XV. Setiap bab: draf Markdown → uji kompilasi kode → checklist Bagian 12 → setujui → lanjut.
4. **Tahap 3 — Back matter.** Daftar Pustaka, Glosarium, Lampiran A–D, Biografi, Sinopsis.
5. **Tahap 4 — Perakitan.** Gabungkan seluruh naskah ke satu `.docx` dengan gaya Bagian 2, bangkitkan Daftar Isi, Daftar Gambar, Daftar Tabel, Daftar Kode Program.
6. **Tahap 5 — Pemeriksaan akhir.** Periksa penomoran, rujukan silang, konsistensi istilah, dan tebal halaman. Ekspor PDF pratinjau.

**Struktur folder kerja:**

```
buku ajar PBO/
├── aturan/ATURAN-BUKU-AJAR-PBO.md      (dokumen ini)
├── naskah/00-front-matter.md
├── naskah/bab-01.md … bab-15.md
├── naskah/90-back-matter.md
├── kode/bab-01/ … bab-15/             (proyek Java yang diuji kompilasi)
├── gambar/gambar-01.png …
└── keluaran/Buku-Ajar-PBO.docx
```

---

## 14. Yang Tidak Boleh Dilakukan

1. Mengubah bunyi CPMK, Sub-CPMK, bobot, atau nama tugas dari [RPS].
2. Menambah atau mengurangi jumlah bab dari 15.
3. Mengubah urutan blok wajib pada Bagian 4.
4. Menyisipkan kode yang belum diuji kompilasi.
5. Memakai teknologi di luar JDK 21, NetBeans, MySQL/MariaDB, JDBC, dan Swing.
6. Memakai ukuran halaman A4 atau font selain Arial untuk badan teks.
7. Menyalin kalimat, gambar, atau kode dari [REF] maupun dari buku rujukan lain.
8. Menulis lebih dari satu bab sebelum bab sebelumnya disetujui.
