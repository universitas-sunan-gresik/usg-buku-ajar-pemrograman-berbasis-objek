package id.ac.usg.sip.model;

public class Bab02Demo {
    public static void main(String[] args) {
        Book b1 = new Book();
        b1.title = "Basis Data";
        b1.author = "Kadir, A.";
        b1.publicationYear = 2012;

        Book b2 = new Book("Struktur Data",
            "Sedgewick, R.", "978-1", 2016);

        b1.displayInfo();
        b2.displayInfo();
        System.out.println("Terbit setelah 2015? "
            + b2.isPublishedAfter(2015));

        Member m1 = new Member("A0001",
            "Nadia Ramadhani", "nadia@usg.ac.id");
        m1.displayInfo();
        System.out.println("Boleh pinjam lagi? "
            + m1.canBorrow(2));
    }
}
