package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.Catalog;
import id.ac.usg.sip.model.Loan;
import id.ac.usg.sip.model.Member;

public class Bab04Demo {
    public static void main(String[] args) {
        Book b1 = new Book("Basis Data",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        Book b2 = new Book("Struktur Data",
            "Sedgewick, R.", "978-602-04-0002-8",
            2016);

        Catalog katalog = new Catalog(
            "Rak Ilmu Komputer",
            new Book[] {b1, b2});
        katalog.displayAll();
        System.out.println(
            "ISBN b1: " + b1.getIsbn());

        Member m1 = new Member("20240001",
            "Nadia Ramadhani", "nadia@usg.ac.id");

        Loan pinjaman = new Loan(m1, b1,
            "2026-09-14");
        System.out.println(pinjaman.getSummary());
    }
}
