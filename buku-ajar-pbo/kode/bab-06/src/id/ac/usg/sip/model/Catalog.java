package id.ac.usg.sip.model;

public class Catalog {
    private String catalogName;
    private LibraryItem[] items;

    public Catalog(String catalogName,
            LibraryItem[] items) {
        this.catalogName = catalogName;
        this.items = items;
    }

    public LibraryItem search(int index) {
        return items[index];
    }

    public LibraryItem search(String title) {
        for (LibraryItem it : items) {
            boolean cocok = it.getTitle()
                .equalsIgnoreCase(title);
            if (cocok) {
                return it;
            }
        }
        return null;
    }

    public void displayAll() {
        System.out.println("Katalog: " + catalogName);
        for (LibraryItem it : items) {
            System.out.println(
                "- " + it.getSummary());
        }
    }
}
