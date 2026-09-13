package id.ac.usg.sip.model;

import java.io.Serializable;

public abstract class LibraryItem
        implements Borrowable, Printable,
        Serializable {
    private static final long
        serialVersionUID = 1L;
    private String title;
    private String itemCode;
    private boolean available;

    public LibraryItem(String title, String code) {
        if (title == null || title.isBlank()) {
            throw new IllegalArgumentException(
                "Judul tidak boleh kosong");
        }
        this.title = title;
        this.itemCode = code;
        this.available = true;
    }

    public String getTitle() {
        return title;
    }

    public String getItemCode() {
        return itemCode;
    }

    @Override
    public boolean isAvailable() {
        return available;
    }

    @Override
    public void borrow()
            throws BookNotAvailableException {
        if (!available) {
            throw new BookNotAvailableException(
                title + " sedang tidak tersedia");
        }
        available = false;
    }

    @Override
    public void returnItem() {
        available = true;
    }

    // Akses default (sepaket): hanya dipakai
    // lapisan DAO untuk merekonstruksi status
    // dari basis data, bukan kontrak publik.
    void setAvailable(boolean available) {
        this.available = available;
    }

    public abstract double calculateFine(
        long daysLate);

    @Override
    public String getSummary() {
        String s =
            available ? "Tersedia" : "Dipinjam";
        return title + " [" + itemCode
            + ", " + s + "]";
    }

    public void displayInfo() {
        System.out.println(getSummary());
    }
}
