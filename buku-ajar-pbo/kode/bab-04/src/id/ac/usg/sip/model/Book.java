package id.ac.usg.sip.model;

public class Book {
    private String title;
    private String author;
    private Isbn isbn;
    private int publicationYear;
    private boolean available;

    public Book() {
        this.available = true;
    }

    public Book(String title, String author,
            String isbnValue, int publicationYear) {
        setTitle(title);
        this.author = author;
        this.isbn = new Isbn(isbnValue);
        setPublicationYear(publicationYear);
        this.available = true;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        if (title == null || title.isBlank()) {
            throw new IllegalArgumentException(
                "Judul tidak boleh kosong");
        }
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public Isbn getIsbn() {
        return isbn;
    }

    public int getPublicationYear() {
        return publicationYear;
    }

    public void setPublicationYear(int year) {
        if (year < 1450 || year > 2100) {
            throw new IllegalArgumentException(
                "Tahun terbit tidak valid: " + year);
        }
        this.publicationYear = year;
    }

    public boolean isAvailable() {
        return available;
    }

    public void setAvailable(boolean available) {
        this.available = available;
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
