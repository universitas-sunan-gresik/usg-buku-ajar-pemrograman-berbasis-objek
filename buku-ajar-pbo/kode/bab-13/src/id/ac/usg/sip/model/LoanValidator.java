package id.ac.usg.sip.model;

public class LoanValidator {
    public void validate(LibraryItem item)
            throws BookNotAvailableException {
        if (item == null) {
            throw new IllegalArgumentException(
                "Item tidak ditemukan");
        }
        if (!item.isAvailable()) {
            throw new BookNotAvailableException(
                item.getTitle()
                + " tidak tersedia");
        }
    }
}
