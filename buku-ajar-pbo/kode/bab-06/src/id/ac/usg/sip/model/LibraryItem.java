package id.ac.usg.sip.model;

public class LibraryItem {
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
    public boolean isAvailable() {
        return available;
    }
    public void setAvailable(boolean available) {
        this.available = available;
    }
    public double calculateFine(long daysLate) {
        return Math.max(0, daysLate) * 500.0;
    }
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
