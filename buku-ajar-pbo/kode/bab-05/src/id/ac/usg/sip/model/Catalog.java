package id.ac.usg.sip.model;

public class Catalog {
    private String catalogName;
    private LibraryItem[] items;

    public Catalog(String catalogName,
            LibraryItem[] items) {
        this.catalogName = catalogName;
        this.items = items;
    }

    public void displayAll() {
        System.out.println("Katalog: " + catalogName);
        for (LibraryItem it : items) {
            System.out.println(
                "- " + it.getSummary());
        }
    }
}
