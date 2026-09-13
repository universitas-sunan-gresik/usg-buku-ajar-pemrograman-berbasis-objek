# DAFTAR PUSTAKA

<!-- gaya: BukuPustaka -->
Apache Software Foundation. (2024). *Apache NetBeans documentation*. https://netbeans.apache.org/
Bloch, J. (2018). *Effective Java* (3rd ed.). Addison-Wesley Professional.
Deitel, P. J., & Deitel, H. M. (2018). *Java how to program, early objects* (11th ed.). Pearson Education.
Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design patterns: Elements of reusable object-oriented software*. Addison-Wesley.
Horstmann, C. S. (2022). *Core Java, Volume I: Fundamentals* (12th ed.). Oracle Press/Pearson.
Kadir, A. (2012). *Algoritma & pemrograman menggunakan Java*. Penerbit Andi.
Oracle Corporation. (2023). *Java Platform, Standard Edition & JDK documentation (JDK 21)*. https://docs.oracle.com/en/java/javase/21/
Oracle Corporation. (2024). *The Java tutorials: Object-oriented programming concepts*. https://docs.oracle.com/javase/tutorial/java/concepts/

# GLOSARIUM

#### A

<!-- gaya: BukuGlosarium -->
**Abstract class** — kelas yang tidak dapat diinstansiasi secara langsung, dapat memiliki *method* konkret maupun abstrak, dan dipakai sebagai kerangka bersama bagi *subclass*-nya (Bab VII).
**Abstract method** — *method* yang hanya dideklarasikan tanda tubuh (implementasi), wajib di-*override* oleh *subclass* konkretnya (Bab VII).
**Abstraksi** — pilar OOP yang menyembunyikan detail implementasi rumit di balik antarmuka yang sederhana bagi pemakainya (Bab I, VII).
**Access modifier** — kata kunci (`public`, `private`, `protected`, *default*) yang mengatur jangkauan akses terhadap anggota kelas (Bab III).
**Agregasi** — relasi "memiliki" antarkelas yang longgar, ditandai objek bagian yang dapat berdiri sendiri tanpa objek keseluruhannya (Bab IV).
**Asosiasi** — relasi umum antarkelas yang menunjukkan bahwa satu kelas menggunakan atau berhubungan dengan kelas lain (Bab IV).
**Atribut** — data yang melekat pada sebuah objek, merepresentasikan keadaan atau karakteristiknya (Bab II).

#### B

<!-- gaya: BukuGlosarium -->
**Behavioral (pattern)** — kategori *design pattern* yang mengatur bagaimana objek saling berkomunikasi dan membagi tanggung jawab perilaku (Bab XIV).
**Bounded type parameter** — parameter generik yang dibatasi agar hanya menerima tipe tertentu atau turunannya, ditulis dengan kata kunci `extends` (Bab IX).
**Bucket** — slot penyimpanan internal pada struktur data *hash* seperti `HashMap`, tempat pasangan kunci-nilai dengan nilai *hash* yang sama dikelompokkan (Bab IX).
**Byte stream** — aliran data I/O yang membaca/menulis data sebagai *byte* mentah, dipakai untuk data biner (Bab X).
**Bytecode** — kode hasil kompilasi Java (berkas `.class`) yang dijalankan oleh JVM, bersifat portabel lintas platform (Bab I).

#### C

<!-- gaya: BukuGlosarium -->
**Cast (casting)** — konversi eksplisit dari satu tipe referensi ke tipe referensi lain dalam hierarki pewarisan yang sama (Bab VI).
**Character stream** — aliran data I/O yang membaca/menulis data sebagai karakter teks, menangani *encoding* secara otomatis (Bab X).
**Checked exception** — *exception* yang wajib ditangani atau dideklarasikan pada *signature method*, diperiksa kompiler pada waktu kompilasi (Bab VIII).
**Classpath** — daftar lokasi (folder/berkas JAR) tempat JVM mencari kelas yang dibutuhkan saat menjalankan program (Bab XI).
**Code smell** — tanda pada kode yang mengindikasikan kemungkinan pelanggaran prinsip desain, meski kode tetap dapat dikompilasi dan berjalan (Bab XIII).
**Collection Framework** — kumpulan *interface* dan kelas siap pakai dalam Java untuk menyimpan dan memanipulasi kumpulan objek, seperti `List`, `Set`, dan `Map` (Bab IX).
**Compile-time error** — kesalahan yang terdeteksi kompiler sebelum program dijalankan, misalnya kesalahan sintaksis (Bab I).
**Connection string** — rangkaian teks yang memuat alamat, port, dan nama basis data yang dipakai untuk membuka koneksi JDBC (Bab XI).
**Constructor** — *method* khusus yang dipanggil otomatis saat objek dibuat, bertugas menginisialisasi atribut objek tersebut (Bab II).
**Constructor injection** — teknik menyerahkan dependensi sebuah objek lewat parameter *constructor*, alih-alih membuatnya sendiri di dalam kelas (Bab XIII).
**Constructor overloading** — penyediaan lebih dari satu *constructor* pada satu kelas dengan daftar parameter yang berbeda-beda (Bab II).
**Container** — komponen Swing yang dapat menampung dan mengatur komponen lain di dalamnya, misalnya `JFrame` dan `JPanel` (Bab XII).
**Creational (pattern)** — kategori *design pattern* yang mengatur bagaimana objek dibuat, seperti *Singleton* dan *Factory Method* (Bab XIV).
**Custom exception** — kelas *exception* buatan sendiri yang diwariskan dari `Exception` atau turunannya untuk merepresentasikan kondisi galat khusus aplikasi (Bab VIII).

#### D

<!-- gaya: BukuGlosarium -->
**Data Access Object (DAO)** — pola rancangan yang memisahkan logika akses data (basis data) dari logika bisnis aplikasi (Bab XI).
**Default method** — *method* pada *interface* yang sudah memiliki implementasi bawaan, sehingga kelas pengimplementasi tidak wajib meng-*override*-nya (Bab VII).
**Dependency Inversion Principle (DIP)** — prinsip SOLID yang menyatakan modul tingkat tinggi dan tingkat rendah sebaiknya sama-sama bergantung pada abstraksi, bukan satu sama lain secara langsung (Bab XIII).
**Deserialization** — proses membaca kembali objek yang sebelumnya disimpan dalam bentuk aliran *byte* menjadi objek Java yang utuh (Bab X).
**Design pattern** — solusi rancangan umum yang telah teruji untuk masalah desain perangkat lunak yang berulang (Bab XIII, XIV).
**Downcasting** — konversi referensi dari tipe *superclass* menuju tipe *subclass* yang lebih spesifik, memerlukan *cast* eksplisit (Bab VI).
**Driver (JDBC)** — pustaka perangkat lunak yang menjembatani program Java dengan sistem basis data tertentu (Bab XI).
**Dynamic binding** — mekanisme penentuan *method* mana yang benar-benar dijalankan pada saat *runtime*, bukan saat kompilasi; dasar dari polimorfisme (Bab VI).

#### E

<!-- gaya: BukuGlosarium -->
**Encapsulation** — lihat *Enkapsulasi*.
**Encoding** — aturan pemetaan karakter teks ke representasi biner, memengaruhi bagaimana teks dibaca/ditulis pada berkas (Bab X).
**Enkapsulasi** — pilar OOP yang membungkus data dan *method* dalam satu kesatuan sekaligus membatasi akses langsung terhadap data tersebut (Bab I, III).
**Event** — kejadian yang dihasilkan saat pengguna berinteraksi dengan komponen antarmuka grafis, misalnya menekan tombol (Bab XII).
**Event handling** — mekanisme menangkap dan merespons *event* yang terjadi pada komponen GUI (Bab XII).
**Exception** — kondisi tidak normal yang mengganggu alur eksekusi program secara wajar, ditangani lewat `try`-`catch` (Bab VIII).
**Exception handling** — mekanisme menangkap dan menangani *exception* agar program tidak berhenti secara tiba-tiba (Bab VIII).

#### F

<!-- gaya: BukuGlosarium -->
**Factory Method** — *design pattern* yang memusatkan logika pembuatan objek ke dalam satu *method* atau kelas tersendiri (Bab XIV).
**Field** — lihat *Atribut*.
**Functional interface** — *interface* yang hanya memiliki tepat satu *method* abstrak, dapat diimplementasikan secara ringkas memakai ekspresi *lambda* (Bab VII).

#### G

<!-- gaya: BukuGlosarium -->
**Generalisasi** — relasi antarkelas pada diagram UML yang menggambarkan hubungan pewarisan antara *superclass* dan *subclass* (Bab IV).
**Generics** — fitur Java yang memungkinkan kelas, *interface*, atau *method* bekerja dengan tipe data yang ditentukan saat pemakaian, meningkatkan keamanan tipe (Bab IX).
**Getter** — *method* yang mengembalikan nilai sebuah atribut privat, bagian dari penerapan enkapsulasi (Bab III).

#### H

<!-- gaya: BukuGlosarium -->
**Hashing** — proses mengubah suatu nilai (kunci) menjadi kode angka (nilai *hash*) yang menentukan lokasi penyimpanannya pada struktur data seperti `HashMap` (Bab IX).
**Heap** — area memori tempat objek Java disimpan selama masa hidupnya, dikelola otomatis oleh *garbage collector* (Bab II).

#### I

<!-- gaya: BukuGlosarium -->
**Immutable** — sifat objek yang nilainya tidak dapat diubah setelah dibuat; seluruh atributnya `final` dan diisi sekali lewat *constructor* (Bab III, IV).
**Information hiding** — praktik menyembunyikan detail internal implementasi kelas dari kode luar, salah satu tujuan utama enkapsulasi (Bab III).
**Inheritance** — lihat *Pewarisan*.
**Instance** — objek konkret yang dibuat dari sebuah kelas lewat kata kunci `new` (Bab II).
**Interface** — kontrak yang mendeklarasikan sekumpulan *method* tanpa implementasi (kecuali *default method*), wajib dipenuhi kelas yang mengimplementasikannya (Bab VII).
**Interface Segregation Principle (ISP)** — prinsip SOLID yang menyatakan lebih baik memecah *interface* besar menjadi beberapa *interface* kecil yang fokus, daripada satu *interface* besar yang memaksa *method* tak relevan (Bab XIII).
**Is-a** — istilah yang menggambarkan hubungan pewarisan yang wajar, misalnya "`Book` *is-a* `LibraryItem`" (Bab V).

#### J

<!-- gaya: BukuGlosarium -->
**Java Database Connectivity (JDBC)** — API standar Java untuk menghubungkan aplikasi dengan berbagai jenis basis data relasional (Bab XI).
**Java Development Kit (JDK)** — paket perangkat lunak lengkap untuk mengembangkan program Java, mencakup kompiler dan JRE (Bab I).
**Java Runtime Environment (JRE)** — lingkungan yang dibutuhkan untuk menjalankan program Java yang sudah dikompilasi, mencakup JVM dan pustaka bawaan (Bab I).
**Java Virtual Machine (JVM)** — mesin virtual yang mengeksekusi *bytecode* Java, menjadikan program Java portabel lintas platform (Bab I).

#### K

<!-- gaya: BukuGlosarium -->
**Kelas** — cetak biru (*template*) yang mendefinisikan atribut dan *method* yang akan dimiliki objek-objek yang dibuat darinya (Bab I, II).

#### L

<!-- gaya: BukuGlosarium -->
**Lambda (ekspresi lambda)** — sintaksis ringkas untuk mengimplementasikan *functional interface* tanpa menuliskan kelas anonim secara penuh (Bab VII).
**Layout manager** — objek yang mengatur posisi dan ukuran komponen di dalam sebuah *container* Swing (Bab XII).
**Liskov Substitution Principle (LSP)** — prinsip SOLID yang menyatakan objek *subclass* harus dapat menggantikan objek *superclass*-nya tanpa mengubah kebenaran program (Bab V, XIII).
**Listener** — objek yang "mendengarkan" *event* tertentu dan menjalankan kode saat *event* itu terjadi (Bab XII).
**Long-Term Support (LTS)** — versi Java yang mendapat dukungan pembaruan dan keamanan dalam jangka panjang, seperti Java 21 (Bab I).

#### M

<!-- gaya: BukuGlosarium -->
**Method** — blok kode bernama yang mendefinisikan perilaku atau operasi yang dapat dilakukan sebuah objek (Bab II).
**Method overloading** — penyediaan beberapa *method* dengan nama sama tetapi daftar parameter berbeda dalam satu kelas (Bab VI).
**Method overriding** — penulisan ulang implementasi *method* milik *superclass* di dalam *subclass*, dengan *signature* yang sama persis (Bab V, VI).
**Model-View-Controller (MVC)** — pola arsitektural yang memisahkan aplikasi menjadi lapisan data (Model), tampilan (View), dan penjembatan keduanya (Controller) (Bab XIV).

#### N

<!-- gaya: BukuGlosarium -->
**Nested class** — kelas yang dideklarasikan di dalam kelas lain (Bab I).
**NIO.2 (New I/O 2)** — API Java modern untuk operasi berkas dan direktori, menggantikan sebagian API `java.io` lama (Bab X).

#### O

<!-- gaya: BukuGlosarium -->
**Objek** — instansiasi nyata dari sebuah kelas, memiliki keadaan (atribut) dan perilaku (*method*) sendiri (Bab I, II).
**Object persistence** — kemampuan menyimpan keadaan objek agar tetap ada melampaui masa hidup program yang membuatnya, misalnya lewat *serialization* atau basis data (Bab X).
**Open-Closed Principle (OCP)** — prinsip SOLID yang menyatakan kelas sebaiknya terbuka untuk diperluas tetapi tertutup untuk dimodifikasi (Bab XIII).
**Overriding** — lihat *Method overriding*.

#### P

<!-- gaya: BukuGlosarium -->
**Package** — mekanisme pengelompokan kelas-kelas yang berkaitan ke dalam satu ruang nama, membantu pengorganisasian dan mencegah tabrakan nama (Bab II).
**Peer assessment** — penilaian kontribusi individu oleh sesama anggota kelompok, umumnya dimoderasi dosen (Bab XV).
**Persistence** — lihat *Object persistence*.
**Pewarisan** — pilar OOP yang memungkinkan sebuah kelas mewarisi atribut dan *method* dari kelas lain (Bab I, V).
**Platform-independent** — sifat program yang dapat dijalankan pada sistem operasi berbeda tanpa perlu ditulis ulang, dimungkinkan oleh JVM (Bab I).
**Polimorfisme** — pilar OOP yang memungkinkan satu perintah/*method* yang sama menghasilkan perilaku berbeda bergantung objek konkret yang memanggilnya (Bab I, VI).
**Primary key** — kolom (atau kombinasi kolom) pada tabel basis data yang nilainya unik dan mengidentifikasi setiap baris secara pasti (Bab XI).

#### R

<!-- gaya: BukuGlosarium -->
**Refactoring** — proses memperbaiki struktur internal kode tanpa mengubah perilaku eksternalnya (Bab XIII).
**Runtime error** — kesalahan yang muncul saat program sedang dijalankan, bukan saat dikompilasi (Bab I).

#### S

<!-- gaya: BukuGlosarium -->
**Serialization** — proses mengubah objek Java menjadi aliran *byte* agar dapat disimpan ke berkas atau dikirim melalui jaringan (Bab X).
**Setter** — *method* yang mengubah nilai sebuah atribut privat, biasanya disertai validasi; bagian dari penerapan enkapsulasi (Bab III).
**Signature (method)** — kombinasi nama *method* beserta jenis dan urutan parameternya, dipakai untuk membedakan *method* yang di-*overload* (Bab VI).
**Single Responsibility Principle (SRP)** — prinsip SOLID yang menyatakan sebuah kelas sebaiknya memiliki hanya satu alasan untuk berubah (Bab XIII).
**Singleton** — *design pattern* yang menjamin sebuah kelas hanya memiliki tepat satu *instance* sepanjang aplikasi berjalan (Bab XIV).
**SOLID** — akronim lima prinsip desain berorientasi objek: *Single Responsibility*, *Open-Closed*, *Liskov Substitution*, *Interface Segregation*, dan *Dependency Inversion* (Bab XIII).
**SQL injection** — teknik peretasan yang menyisipkan perintah SQL berbahaya lewat input pengguna yang tidak divalidasi (Bab XI).
**Stack (struktur memori)** — area memori yang menyimpan variabel lokal dan referensi objek selama pemanggilan *method* berlangsung (Bab II).
**Stack trace** — catatan urutan pemanggilan *method* yang ditampilkan saat *exception* terjadi, membantu menelusuri sumber galat (Bab VIII).
**Static method** — *method* yang dimiliki oleh kelas itu sendiri, dapat dipanggil tanpa membuat *instance*-nya terlebih dahulu (Bab VII).
**Stream (I/O)** — abstraksi aliran data yang mengalir dari atau menuju sumber data, seperti berkas atau jaringan (Bab X).
**Subclass** — kelas yang mewarisi atribut dan *method* dari kelas lain (*superclass*) lewat kata kunci `extends` (Bab V).
**Superclass** — kelas yang diwarisi oleh satu atau lebih *subclass* (Bab V).

#### T

<!-- gaya: BukuGlosarium -->
**Try-with-resources** — konstruksi `try` yang menutup sumber daya (seperti koneksi atau berkas) secara otomatis setelah blok selesai dieksekusi (Bab X).
**Type parameter** — *placeholder* tipe data pada *generics* yang digantikan tipe konkret saat kelas/*method* dipakai (Bab IX).
**Type safety** — jaminan bahwa kesalahan tipe data terdeteksi pada waktu kompilasi, bukan waktu jalan (Bab IX).

#### U

<!-- gaya: BukuGlosarium -->
**Unchecked exception** — *exception* yang tidak wajib ditangani atau dideklarasikan secara eksplisit, umumnya menandakan kesalahan pemrograman (Bab VIII).
**Unified Modeling Language (UML)** — notasi standar untuk memodelkan rancangan sistem berorientasi objek, termasuk diagram kelas (Bab IV).
**Upcasting** — konversi referensi dari tipe *subclass* menuju tipe *superclass*-nya, terjadi secara implisit dan aman (Bab VI).

# LAMPIRAN A. KISI-KISI DAN LATIHAN KOMPREHENSIF UTS

## A.1 Cakupan dan Bentuk Ujian

Ujian Tengah Semester (UTS) dilaksanakan pada Minggu ke-8, mencakup Sub-CPMK1 sampai Sub-CPMK5, yaitu seluruh materi Bab I sampai Bab VII: paradigma OOP, kelas dan objek, enkapsulasi, pemodelan UML, pewarisan, polimorfisme, dan abstraksi. UTS terdiri atas dua bentuk: tes tertulis uraian yang dinilai dengan rubrik R14 (Rubrik Penskoran UTS/UAS Esai/Uraian), dan tes praktik yang dinilai dengan rubrik R10 (Rubrik Analisis Kasus/Berbasis Masalah). Bobot UTS terhadap nilai akhir mata kuliah adalah 15%.

## A.2 Kisi-Kisi Soal

Tabel #kisi-uts. Kisi-kisi soal UTS berdasarkan Sub-CPMK1 sampai Sub-CPMK5

| Sub-CPMK | Indikator | Bab Rujukan | Bentuk Soal |
|---|---|---|---|
| Sub-CPMK1 | Menjelaskan paradigma OOP; menerapkan kelas, objek, atribut, *method*, dan *constructor* | Bab I-II | Uraian |
| Sub-CPMK2 | Menerapkan enkapsulasi dan *information hiding* melalui *access modifier* dan *getter*/*setter* | Bab III | Uraian dan praktik |
| Sub-CPMK3 | Merancang model berorientasi objek dengan diagram kelas UML beserta relasi antarkelas | Bab IV | Praktik (menggambar diagram) |
| Sub-CPMK4 | Mengimplementasikan pewarisan dan polimorfisme dalam bahasa Java | Bab V-VI | Uraian dan praktik |
| Sub-CPMK5 | Menerapkan abstraksi melalui *abstract class* dan *interface* | Bab VII | Uraian dan praktik |

## A.3 Latihan Soal Komprehensif

Latihan berikut disusun agar mahasiswa dapat menguji pemahamannya secara mandiri sebelum UTS, mencakup seluruh Sub-CPMK1 sampai Sub-CPMK5 sekaligus mengaitkannya dengan studi kasus SIP-USG yang telah dibangun sejak Bab II.

1. (Sub-CPMK1) Jelaskan perbedaan paradigma pemrograman prosedural dan berorientasi objek, lalu berikan satu contoh dari SIP-USG yang menunjukkan penerapan paradigma berorientasi objek.
2. (Sub-CPMK1) Rancanglah sebuah kelas Java sederhana bernama `Mahasiswa` dengan atribut `nim`, `nama`, dan `ipk`, beserta *constructor* dan *method getter*/*setter* yang sesuai.
3. (Sub-CPMK2) Jelaskan mengapa atribut sebuah kelas sebaiknya dideklarasikan `private`, lalu tunjukkan bagaimana *getter*/*setter* tetap memungkinkan akses yang terkendali.
4. (Sub-CPMK3) Gambarkan diagram kelas UML sederhana untuk relasi antara kelas `Perpustakaan` dan kelas `Buku`, termasuk kardinalitas hubungannya.
5. (Sub-CPMK4) Jelaskan perbedaan *method overloading* dan *method overriding*, lalu berikan satu contoh masing-masing menggunakan kelas `LibraryItem` dan *subclass*-nya.
6. (Sub-CPMK4) Perhatikan hierarki `LibraryItem`, `Book`, dan `Journal` pada SIP-USG. Jelaskan bagaimana polimorfisme memungkinkan satu larik `LibraryItem[]` menyimpan objek `Book` dan `Journal` sekaligus.
7. (Sub-CPMK5) Jelaskan perbedaan *abstract class* dan *interface*, lalu berikan satu situasi pada SIP-USG yang lebih tepat menggunakan *interface* dibandingkan *abstract class*.
8. (Sub-CPMK5) Implementasikan sebuah *functional interface* sederhana bernama `Validator<T>` dengan satu *method* abstrak `validate(T data)`, lalu tunjukkan cara memakainya dengan ekspresi *lambda*.

Poin kunci jawaban dapat ditelusuri kembali pada bagian isi bab yang bersesuaian: soal 1-2 pada Bab I-II, soal 3 pada Bab III, soal 4 pada Bab IV, soal 5-6 pada Bab V-VI, dan soal 7-8 pada Bab VII.

# LAMPIRAN B. KISI-KISI DAN LATIHAN KOMPREHENSIF UAS

## B.1 Cakupan dan Bentuk Ujian

Ujian Akhir Semester (UAS) dilaksanakan pada Minggu ke-16, mencakup Sub-CPMK6 sampai Sub-CPMK8, yaitu materi Bab VIII sampai Bab XV: penanganan eksepsi, *collection* dan *generics*, operasi berkas, JDBC, GUI, prinsip SOLID, *design pattern*, dan integrasi proyek akhir. UAS terdiri atas tes tertulis uraian untuk Sub-CPMK6 sampai Sub-CPMK8 yang dinilai dengan rubrik R14, serta komponen diseminasi produk Tugas 4 yang turut dinilai secara kualitatif memakai kriteria rubrik R9 (Proyek/Produk Kelompok) dan R8 (Presentasi Kelompok), terpisah dari komponen Hasil Proyek yang berbobot 25% pada Operasionalisasi Bobot RPS. Bobot UAS terhadap nilai akhir mata kuliah adalah 20%.

## B.2 Kisi-Kisi Soal

Tabel #kisi-uas. Kisi-kisi soal UAS berdasarkan Sub-CPMK6 sampai Sub-CPMK8

| Sub-CPMK | Indikator | Bab Rujukan | Bentuk Soal |
|---|---|---|---|
| Sub-CPMK6 | Mengimplementasikan penanganan eksepsi, *collection*, dan *generics* | Bab VIII-IX | Uraian |
| Sub-CPMK7 | Membangun aplikasi terintegrasi dengan operasi berkas, basis data (JDBC/CRUD), dan GUI | Bab X-XII | Uraian dan praktik |
| Sub-CPMK8 | Menerapkan prinsip SOLID/*design pattern*; mengembangkan dan mempresentasikan proyek | Bab XIII-XV | Uraian dan diseminasi produk |

## B.3 Latihan Soal Komprehensif

1. (Sub-CPMK6) Jelaskan perbedaan *checked exception* dan *unchecked exception*, lalu berikan satu contoh masing-masing dari SIP-USG.
2. (Sub-CPMK6) Jelaskan manfaat *generics* pada `Repository<T>`, lalu tunjukkan bagaimana *bounded type parameter* dapat membatasi tipe yang diterima.
3. (Sub-CPMK7) Jelaskan perbedaan *serialization* dan penyimpanan lewat basis data (JDBC) sebagai dua cara mencapai *object persistence*.
4. (Sub-CPMK7) Rancanglah kueri SQL `PreparedStatement` untuk menambah satu baris baru ke tabel `books`, lalu jelaskan mengapa `PreparedStatement` lebih aman dibandingkan `Statement` biasa.
5. (Sub-CPMK7) Jelaskan alur *event handling* saat pengguna menekan tombol "Tambah" pada `BookFormFrame`, dari `ActionListener` hingga tabel diperbarui.
6. (Sub-CPMK8) Jelaskan lima prinsip SOLID secara ringkas, lalu identifikasi satu pelanggaran SOLID pada kode `LibraryServiceBad`.
7. (Sub-CPMK8) Jelaskan bagaimana pola *Singleton* dan *Factory Method* diterapkan pada SIP-USG, beserta manfaat masing-masing.
8. (Sub-CPMK8) Evaluasilah kesiapan sebuah proyek kelompok yang telah mengintegrasikan GUI, basis data, dan pola desain, tetapi dokumentasi kontribusi individunya belum lengkap; kaitkan jawaban dengan rubrik R9 dan R13.

Poin kunci jawaban dapat ditelusuri kembali pada bagian isi bab yang bersesuaian: soal 1-2 pada Bab VIII-IX, soal 3-5 pada Bab X-XII, dan soal 6-8 pada Bab XIII-XV.

# LAMPIRAN C. PANDUAN PROYEK AKHIR

## C.1 Ketentuan Umum Tugas 4

Tugas 4 adalah proyek aplikasi berorientasi objek yang dikerjakan berkelompok (3-4 mahasiswa), dikembangkan bertahap dari Minggu ke-9 sampai Minggu ke-15, dan dipresentasikan pada Minggu ke-16 bersamaan dengan pelaksanaan UAS. Setiap kelompok wajib membangun aplikasi yang mengintegrasikan seluruh materi OOP: kelas dan objek, pewarisan dan polimorfisme, penanganan eksepsi, koleksi/*generics*, antarmuka grafis (GUI), koneksi basis data (JDBC), serta prinsip desain SOLID dan minimal satu *design pattern*.

## C.2 Pilihan Topik Aplikasi

Kelompok tidak diwajibkan melanjutkan studi kasus SIP-USG yang dipakai sepanjang buku ini; SIP-USG hanya berfungsi sebagai contoh acuan yang telah terbukti dapat diselesaikan dengan pola rancangan yang sama. Kelompok dapat memilih topik lain yang setara cakupannya, misalnya sistem informasi inventaris laboratorium, sistem informasi presensi organisasi mahasiswa, atau sistem informasi peminjaman fasilitas kampus, selama aplikasi tersebut tetap mencakup entitas data yang jelas, operasi CRUD lewat basis data, antarmuka grafis, dan penerapan minimal satu prinsip SOLID beserta satu *design pattern*.

## C.3 Struktur Laporan

Laporan proyek (berkas PDF) sekurang-kurangnya memuat: (1) analisis kebutuhan dan ruang lingkup aplikasi; (2) rancangan diagram kelas UML dan skema tabel basis data; (3) penjelasan implementasi tiga lapisan Model-View-Controller beserta penerapan *design pattern* yang dipilih; (4) hasil pengujian, termasuk skenario uji integrasi seperti dicontohkan pada Bab XV bagian C; dan (5) pembagian kontribusi setiap anggota kelompok secara eksplisit.

## C.4 Format Slide dan Demonstrasi

Slide presentasi memuat ringkasan rancangan, cuplikan kode yang mewakili keputusan desain penting (bukan seluruh kode sumber), dan hasil pengujian, mengikuti daftar periksa pada Tabel 11 (Bab XV bagian E). Demonstrasi dilakukan secara langsung terhadap aplikasi yang benar-benar berjalan, bukan sekadar tangkapan layar statis.

## C.5 Jadwal Asistensi dan Progres

Progres proyek diasistensi pada Minggu ke-9 (pembentukan kelompok dan perencanaan) dan Minggu ke-15 (finalisasi dan unggah produk), sebagaimana tercantum pada Matriks Pembelajaran Mingguan RPS. Kelompok yang tidak menunjukkan progres pada kedua titik asistensi tersebut berisiko dinilai rendah pada kriteria "Kualitas laporan/produk dan integritas" rubrik R9.

## C.6 Pembobotan Nilai

Nilai individu proyek = 60% produk aplikasi (rubrik R9) + 25% presentasi (rubrik R8) + 15% kontribusi individu (rubrik R13, *peer assessment* dimoderasi dosen). Ringkasan ketiga rubrik ini tersedia pada Lampiran D.

# LAMPIRAN D. RUBRIK PENILAIAN RINGKAS

## D.1 Skala Kinerja dan Rumus Nilai

Seluruh rubrik (R1, R3, R8, R9, R10, R13, R14) memakai skala kinerja yang sama, dari 0 sampai 4, sebagaimana dirangkum pada Tabel #skala-kinerja.

Tabel #skala-kinerja. Skala kinerja rubrik penilaian RPS

| Skor | Kategori | Makna Umum |
|---|---|---|
| 4 | Sangat Baik | Kinerja memenuhi seluruh unsur kriteria secara tepat, lengkap, mendalam, mandiri, dan didukung bukti yang relevan |
| 3 | Baik | Kinerja memenuhi sebagian besar unsur kriteria secara tepat; terdapat kekurangan kecil yang tidak mengubah substansi |
| 2 | Cukup | Kinerja memenuhi unsur dasar, tetapi masih terdapat kekurangan konsep, kedalaman, konsistensi, atau bukti |
| 1 | Kurang | Kinerja hanya memenuhi sebagian kecil unsur; terdapat kesalahan substansial atau bukti sangat terbatas |
| 0 | Tidak Ada Bukti | Tidak menjawab, tidak menunjukkan kinerja, tidak mengumpulkan, atau produk tidak dapat dinilai |

Rumus nilai setiap rubrik: Nilai Asesmen = Sigma (Skor Kinerja / 4 x Bobot Kriteria), dengan total bobot kriteria pada setiap rubrik berjumlah 100%.

## D.2 Ringkasan Kriteria Setiap Rubrik

Tabel #ringkasan-rubrik. Ringkasan kriteria utama tujuh rubrik RPS (R1, R3, R8, R9, R10, R13, R14)

| Rubrik | Nama | Kriteria Utama (Bobot) |
|---|---|---|
| R1 | Partisipasi dan Diskusi Kelas/Forum | Kesiapan kontribusi (25%), penalaran kritis (25%), interaksi kolaborasi (20%), sikap profesional (15%), konsistensi ketepatan waktu (15%) |
| R3 | Kuis/Tes Tertulis | Ketepatan jawaban (50%), penalaran/aplikasi (25%), kelengkapan (15%), kejelasan jawaban (10%) |
| R8 | Presentasi Kelompok | Penguasaan materi (25%), struktur/media (15%), kejelasan komunikasi (15%), kemampuan menjawab (20%), koordinasi tim (15%), etika presentasi (10%) |
| R9 | Proyek/Produk Kelompok | Kejelasan tujuan/lingkup (10%), kerangka konsep/desain (15%), kualitas data/proses (15%), analisis pemecahan masalah (25%), integrasi pengetahuan (15%), rekomendasi (10%), kualitas laporan/integritas (10%) |
| R10 | Analisis Kasus/Berbasis Masalah | Identifikasi masalah (15%), pemilahan fakta/asumsi (15%), alternatif tindakan (20%), penalaran berbasis bukti (25%), keputusan/etika (15%), kejelasan penyajian (10%) |
| R13 | Kontribusi Individu (Peer Assessment) | Kontribusi substansi (30%), tanggung jawab/ketepatan waktu (25%), kolaborasi (20%), komunikasi (15%), profesionalisme/integritas (10%) |
| R14 | Penskoran UTS/UAS Esai/Uraian | Ketepatan konsep/substansi (40%), analisis/aplikasi (30%), argumentasi/bukti (20%), struktur/kejelasan jawaban (10%) |

## D.3 Konversi Nilai Akhir

Tabel #konversi-nilai. Konversi rentang nilai akhir mata kuliah

| Rentang Nilai Akhir | Huruf | Nilai Mutu |
|---|---|---|
| 86-100 | A | 4,00 |
| 78-85 | AB | 3,50 |
| 70-77 | B | 3,00 |
| 62-69 | BC | 2,50 |
| 54-61 | C | 2,00 |
| 40-53 | D | 1,00 |
| 0-39 | E | 0,00 |

Konversi huruf diterapkan pada nilai akhir mata kuliah setelah seluruh komponen berbobot dijumlahkan, bukan sebagai kolom tingkat kinerja pada setiap rubrik.

## D.4 Hubungan Kriteria Keberhasilan Bab dengan Rubrik Resmi RPS

Blok "Kriteria Keberhasilan (Rubrik)" pada setiap bab buku ini, yang memakai rentang persentase gaya buku ajar (Sangat Baik >= 85, Baik 70-84, Cukup 55-69), adalah gambaran kualitatif tentang kedalaman pemahaman yang diharapkan pada bab tersebut, disusun agar mahasiswa dapat menilai kesiapannya sendiri secara cepat tanpa membuka RPS. Blok ini tidak menggantikan tujuh rubrik resmi (R1, R3, R8, R9, R10, R13, R14) yang dirangkum pada bagian D.2, yang tetap menjadi satu-satunya acuan penilaian sumatif dan formatif oleh dosen sebagaimana ditetapkan RPS. Dengan kata lain, blok Kriteria Keberhasilan menjawab pertanyaan "seberapa dalam saya sudah paham bab ini?", sedangkan rubrik resmi RPS menjawab pertanyaan "berapa nilai yang tercatat pada komponen asesmen tertentu?"; keduanya saling melengkapi, bukan saling menggantikan.

# BIOGRAFI PENULIS

[Pasfoto Penulis]

Muhammad Muchson Attoyibi, S.Pd., M.Pd. adalah dosen pengampu mata kuliah Pemrograman Berorientasi Objek pada Program Studi Sarjana Sistem Informasi, Fakultas Teknologi dan Rekayasa, Universitas Sunan Gresik (USG). Penulis menyelesaikan pendidikan sarjana (S.Pd.) dan magister (M.Pd.) di bidang pendidikan, dengan minat keilmuan yang kemudian berkembang ke arah rekayasa perangkat lunak dan pengajaran pemrograman berorientasi objek berbasis Java.

Sebagai penyusun Rencana Pembelajaran Semester (RPS) sekaligus penulis buku ajar ini, penulis meyakini bahwa pemrograman berorientasi objek paling efektif dipelajari lewat satu studi kasus yang tumbuh bertahap, bukan lewat contoh-contoh terisolasi yang berganti setiap bab. Buku ajar ini disusun berdasarkan keyakinan tersebut, dengan aplikasi Sistem Informasi Perpustakaan USG (SIP-USG) yang dibangun bab demi bab sebagai benang merah dari konsep kelas dan objek yang paling sederhana hingga arsitektur *Model-View-Controller* dan proyek akhir yang utuh. Penulis dapat dihubungi melalui surel resmi muhammadmuchson@gmail.com untuk masukan, koreksi, maupun diskusi lebih lanjut mengenai buku ajar ini.

# SINOPSIS BUKU

Buku ajar ini disusun untuk mata kuliah Pemrograman Berorientasi Objek pada Program Studi Sarjana Sistem Informasi, Universitas Sunan Gresik, mengikuti Rencana Pembelajaran Semester (RPS) yang berlaku secara ketat pada setiap capaian pembelajaran, indikator, dan rubrik penilaiannya. Kelima belas bab dalam buku ini disusun sebagai satu rangkaian yang utuh, bukan kumpulan topik yang berdiri sendiri: seluruhnya dibangun di atas satu studi kasus yang sama, Sistem Informasi Perpustakaan USG (SIP-USG), yang tumbuh bertahap dari kelas dan objek paling sederhana pada Bab II, menembus pewarisan, polimorfisme, dan abstraksi, terhubung ke basis data sungguhan dan antarmuka grafis, hingga akhirnya dirapikan dengan prinsip SOLID dan *design pattern* serta dirakit menjadi satu aplikasi utuh pada Bab XV.

Setiap bab ditulis agar dapat dipelajari secara mandiri tanpa kehadiran dosen: penjelasan konsep disertai analogi dari kehidupan sehari-hari, diagram visual untuk konsep yang rumit, kode Java yang telah benar-benar diuji kompilasi dan dijalankan pada JDK 21, serta latihan soal berjenjang dari tingkat pemahaman hingga evaluasi. Buku ini ditujukan bagi mahasiswa yang ingin memahami pemrograman berorientasi objek secara mendalam dan aplikatif, sekaligus menjadi bekal langsung untuk menyelesaikan proyek aplikasi berorientasi objek yang terintegrasi dengan basis data dan antarmuka grafis sebagai produk akhir pembelajaran.
