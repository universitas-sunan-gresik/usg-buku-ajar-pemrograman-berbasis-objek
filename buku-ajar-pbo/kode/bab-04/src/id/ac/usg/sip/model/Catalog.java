package id.ac.usg.sip.model;

public class Catalog {
    private String catalogName;
    private Book[] books;

    public Catalog(String catalogName, Book[] books) {
        this.catalogName = catalogName;
        this.books = books;
    }

    public void displayAll() {
        System.out.println("Katalog: " + catalogName);
        for (Book b : books) {
            System.out.println("- " + b.getSummary());
        }
    }
}
