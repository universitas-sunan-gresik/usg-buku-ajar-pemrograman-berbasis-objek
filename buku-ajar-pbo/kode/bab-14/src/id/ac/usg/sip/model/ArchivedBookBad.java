package id.ac.usg.sip.model;

public class ArchivedBookBad extends Book {
    public ArchivedBookBad(String title,
            String itemCode, String author,
            String isbnValue, int year) {
        super(title, itemCode, author,
            isbnValue, year);
    }

    @Override
    public void borrow()
            throws BookNotAvailableException {
        throw new UnsupportedOperationException(
            "Arsip tidak dapat dipinjam");
    }
}
