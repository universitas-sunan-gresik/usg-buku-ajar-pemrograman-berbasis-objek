package id.ac.usg.sip.app;

import id.ac.usg.sip.model.AksesModel;

public class AksesDemo {
    public static void main(String[] args) {
        AksesModel a = new AksesModel();
        a.tampilkanSemua();

        // Dari paket lain, hanya atribut public
        // yang boleh diakses langsung seperti ini:
        System.out.println("Diakses langsung: "
            + a.publik);

        // Baris berikut SENGAJA tidak dituliskan
        // karena tidak akan berhasil dikompilasi:
        // a.rahasia    -> private, beda kelas
        // a.sepaket    -> default, beda paket
        // a.turunan    -> protected, bukan subclass
    }
}
