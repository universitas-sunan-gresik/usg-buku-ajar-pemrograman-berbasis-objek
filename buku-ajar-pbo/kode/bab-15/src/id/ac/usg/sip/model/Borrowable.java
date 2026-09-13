package id.ac.usg.sip.model;

public interface Borrowable {
    boolean isAvailable();

    void borrow() throws BookNotAvailableException;

    void returnItem();
}
