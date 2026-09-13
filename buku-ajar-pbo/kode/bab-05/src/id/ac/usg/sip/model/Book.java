package id.ac.usg.sip.model;

public class Book extends LibraryItem {
    private String author;
    private Isbn isbn;
    private int publicationYear;

    public Book(String title, String itemCode,
            String author, String isbnValue,
            int publicationYear) {
        super(title, itemCode);
        this.author = author;
        this.isbn = new Isbn(isbnValue);
        setPublicationYear(publicationYear);
    }
    public String getAuthor() {
        return author;
    }
    public Isbn getIsbn() {
        return isbn;
    }
    public int getPublicationYear() {
        return publicationYear;
    }
    public final void setPublicationYear(int year) {
        if (year < 1450 || year > 2100) {
            throw new IllegalArgumentException(
                "Tahun tidak valid: " + year);
        }
        this.publicationYear = year;
    }
    public boolean isPublishedAfter(int year) {
        return publicationYear > year;
    }
    @Override
    public String getSummary() {
        return super.getSummary() + " oleh "
            + author + " (" + publicationYear + ")";
    }
}
