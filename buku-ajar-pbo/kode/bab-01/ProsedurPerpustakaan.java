public class ProsedurPerpustakaan {
    static String[] judul =
        {"Basis Data", "Struktur Data"};
    static String[] penulis =
        {"Kadir, A.", "Sedgewick, R."};
    static boolean[] tersedia = {true, true};

    static void tampilkanBuku(int i) {
        String s =
            tersedia[i] ? "tersedia" : "dipinjam";
        System.out.println(judul[i] + " - "
            + penulis[i] + " [" + s + "]");
    }

    static void pinjamBuku(int i) {
        if (tersedia[i]) {
            tersedia[i] = false;
            System.out.println(
                "Dipinjam: " + judul[i]);
        } else {
            System.out.println(
                "Ditolak, sudah dipinjam: "
                + judul[i]);
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < judul.length; i++) {
            tampilkanBuku(i);
        }
        pinjamBuku(0);
        pinjamBuku(0);
    }
}
