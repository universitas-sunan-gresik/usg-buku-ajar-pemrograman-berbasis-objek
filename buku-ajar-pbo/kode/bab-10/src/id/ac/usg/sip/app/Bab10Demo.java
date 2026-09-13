package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.Catalog;
import id.ac.usg.sip.model.CatalogFileUtil;
import id.ac.usg.sip.model.Journal;
import id.ac.usg.sip.model.LibraryItem;
import java.util.List;

public class Bab10Demo {
    public static void main(String[] args)
            throws Exception {
        Book b1 = new Book("Basis Data", "B001",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        Journal j1 = new Journal("Jurnal SI", "J001",
            "USG Press", 12);

        Catalog katalog =
            new Catalog("Rak Ilmu Komputer");
        katalog.addItem(b1);
        katalog.addItem(j1);
        List<LibraryItem> semua =
            katalog.sortedByTitle();

        CatalogFileUtil.saveItems(
            semua, "katalog.dat");
        CatalogFileUtil.exportTitlesCsv(
            semua, "katalog.csv");
        System.out.println("Tersimpan ke berkas");

        List<LibraryItem> hasilMuat =
            CatalogFileUtil.loadItems(
                "katalog.dat");
        System.out.println("Dimuat dari .dat:");
        for (LibraryItem it : hasilMuat) {
            System.out.println(
                "- " + it.getSummary());
        }

        List<String> judul =
            CatalogFileUtil.readTitlesCsv(
                "katalog.csv");
        System.out.println(
            "Judul dari .csv: " + judul);
    }
}
