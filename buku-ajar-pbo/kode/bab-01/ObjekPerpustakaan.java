public class ObjekPerpustakaan {
    static class BukuSederhana {
        String judul;
        String penulis;
        boolean tersedia = true;
        void tampilkan() {
            String s =
                tersedia ? "tersedia" : "dipinjam";
            System.out.println(judul + " - "
                + penulis + " [" + s + "]");
        }
        void pinjam() {
            if (tersedia) {
                tersedia = false;
                System.out.println(
                    "Dipinjam: " + judul);
            } else {
                System.out.println(
                    "Ditolak, sudah dipinjam: "
                    + judul);
            }
        }
    }

    public static void main(String[] args) {
        BukuSederhana b1 = new BukuSederhana();
        b1.judul = "Basis Data";
        b1.penulis = "Kadir, A.";

        BukuSederhana b2 = new BukuSederhana();
        b2.judul = "Struktur Data";
        b2.penulis = "Sedgewick, R.";

        b1.tampilkan();
        b2.tampilkan();
        b1.pinjam();
        b1.pinjam();
    }
}
