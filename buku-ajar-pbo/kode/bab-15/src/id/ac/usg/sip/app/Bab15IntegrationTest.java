package id.ac.usg.sip.app;

import id.ac.usg.sip.controller.BookController;

public class Bab15IntegrationTest {
    public static void main(String[] args)
            throws Exception {
        BookController controller =
            new BookController();

        int sebelum =
            controller.semuaBuku().size();
        System.out.println(
            "Jumlah buku sebelum: " + sebelum);

        controller.tambahBuku(
            "Rekayasa Perangkat Lunak", "B900",
            "Pressman, R.",
            "978-0-07-337597-7", 2015);
        System.out.println(
            "B900 berhasil ditambahkan");

        int sesudahTambah =
            controller.semuaBuku().size();
        System.out.println(
            "Jumlah buku sesudah tambah: "
            + sesudahTambah);

        controller.hapusBuku("B900");
        int sesudahHapus =
            controller.semuaBuku().size();
        System.out.println(
            "Jumlah buku sesudah hapus: "
            + sesudahHapus);
    }
}
