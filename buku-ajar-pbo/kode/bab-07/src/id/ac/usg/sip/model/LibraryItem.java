package id.ac.usg.sip.model;

public abstract class LibraryItem
        implements Borrowable, Printable {
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
    public void borrow() {
        available = false;
    }

    @Override
    public void returnItem() {
        available = true;
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
