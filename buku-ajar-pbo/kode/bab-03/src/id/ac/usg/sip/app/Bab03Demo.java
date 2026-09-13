package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.Isbn;
import id.ac.usg.sip.model.Member;

public class Bab03Demo {
    public static void main(String[] args) {
        Book b = new Book("Basis Data",
            "Kadir, A.", "978-1", 2012);
        b.displayInfo();

        try {
            b.setPublicationYear(3000);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: "
                + e.getMessage());
        }

        try {
            Member m = new Member("A1",
                "Nadia", "nadia@usg.ac.id");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: "
                + e.getMessage());
        }

        Member m2 = new Member("20240001",
            "Nadia Ramadhani", "nadia@usg.ac.id");
        m2.displayInfo();

        Isbn kode = new Isbn("978-602-04-1234-5");
        System.out.println("ISBN: " + kode);
    }
}
