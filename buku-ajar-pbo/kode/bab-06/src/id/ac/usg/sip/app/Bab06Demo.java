package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.Catalog;
import id.ac.usg.sip.model.DigitalItem;
import id.ac.usg.sip.model.Journal;
import id.ac.usg.sip.model.LibraryItem;

public class Bab06Demo {
    public static void main(String[] args) {
        Book b1 = new Book("Basis Data", "B001",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        Journal j1 = new Journal(
            "Jurnal SI", "J001",
            "USG Press", 12);
        DigitalItem d1 = new DigitalItem(
            "E-Modul Java Dasar", "D001",
            "PDF", 4.5);
        LibraryItem[] semua = {b1, j1, d1};
        Catalog katalog = new Catalog(
            "Rak Ilmu Komputer", semua);
        System.out.println(
            "Overload search(int): "
            + katalog.search(1).getTitle());
        System.out.println(
            "Overload search(String): "
            + katalog.search("Jurnal SI")
                .getItemCode());
        System.out.println("--- Denda 5 hari ---");
        for (LibraryItem it : semua) {
            double denda = it.calculateFine(5);
            System.out.println(
                it.getTitle() + ": Rp" + denda);
            if (it instanceof Book bk) {
                System.out.println(
                    "  Penulis: " + bk.getAuthor());
            }
        }
    }
}
