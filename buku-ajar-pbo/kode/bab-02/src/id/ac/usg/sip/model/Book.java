package id.ac.usg.sip.model;

public class Book {
    String title;
    String author;
    String isbn;
    int publicationYear;
    boolean available;

    public Book() {
        this.available = true;
    }

    public Book(String title, String author,
            String isbn, int publicationYear) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.publicationYear = publicationYear;
        this.available = true;
    }

    public String getSummary() {
        String status =
            available ? "Tersedia" : "Dipinjam";
        return title + " (" + publicationYear
            + ") oleh " + author
            + " [" + status + "]";
    }

    public boolean isPublishedAfter(int year) {
        return publicationYear > year;
    }

    public void displayInfo() {
        System.out.println(getSummary());
    }
}
