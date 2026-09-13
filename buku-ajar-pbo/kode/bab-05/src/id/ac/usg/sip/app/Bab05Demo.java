package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.Catalog;
import id.ac.usg.sip.model.DigitalItem;
import id.ac.usg.sip.model.Journal;
import id.ac.usg.sip.model.LibraryItem;
import id.ac.usg.sip.model.Loan;
import id.ac.usg.sip.model.Member;

public class Bab05Demo {
    public static void main(String[] args) {
        Book b1 = new Book("Basis Data", "B001",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        Journal j1 = new Journal(
            "Jurnal SI", "J001",
            "USG Press", 12);
        DigitalItem d1 = new DigitalItem(
            "E-Modul Java Dasar", "D001",
            "PDF", 4.5);

        Catalog katalog = new Catalog(
            "Rak Ilmu Komputer",
            new LibraryItem[] {b1, j1, d1});
        katalog.displayAll();

        Member m1 = new Member("20240001",
            "Nadia Ramadhani", "nadia@usg.ac.id");
        Loan pinjaman = new Loan(m1, j1,
            "2026-09-14");
        System.out.println(pinjaman.getSummary());
    }
}
