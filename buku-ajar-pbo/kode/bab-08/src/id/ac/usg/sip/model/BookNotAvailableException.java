package id.ac.usg.sip.model;

public class BookNotAvailableException
        extends Exception {
    public BookNotAvailableException(
            String message) {
        super(message);
    }
}
