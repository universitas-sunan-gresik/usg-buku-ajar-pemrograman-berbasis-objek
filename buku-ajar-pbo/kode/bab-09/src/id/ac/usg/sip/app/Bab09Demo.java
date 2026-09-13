package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.Catalog;
import id.ac.usg.sip.model.Journal;
import id.ac.usg.sip.model.LibraryItem;
import id.ac.usg.sip.model.Member;
import id.ac.usg.sip.model.Repository;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Bab09Demo {
    public static void main(String[] args) {
        Book b1 = new Book("Jaringan", "B002",
            "Sofana, I.", "978-602-04-0002-8",
            2010);
        Book b2 = new Book("Basis Data", "B001",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        Journal j1 = new Journal("Jurnal SI", "J001",
            "USG Press", 12);

        Catalog katalog =
            new Catalog("Rak Ilmu Komputer");
        katalog.addItem(b1);
        katalog.addItem(b2);
        katalog.addItem(j1);
        katalog.displayAll();
        System.out.println("Cari B001: "
            + katalog.findByCode("B001").getTitle());

        List<Book> daftar = new ArrayList<>();
        daftar.add(b2);
        daftar.add(b1);
        Collections.sort(daftar);
        System.out.println("Urut judul: "
            + daftar.get(0).getTitle());

        daftar.sort(Comparator.comparingInt(
            Book::getPublicationYear));
        System.out.println("Urut tahun: "
            + daftar.get(0).getTitle());

        Repository<Member> anggota =
            new Repository<>();
        anggota.add(new Member("20240001",
            "Nadia Ramadhani", "nadia@usg.ac.id"));
        System.out.println(
            "Jumlah anggota: " + anggota.count());

        List<LibraryItem> semua =
            katalog.sortedByTitle();
        int tersedia =
            Repository.countAvailable(semua);
        System.out.println(
            "Item tersedia: " + tersedia);
    }
}
