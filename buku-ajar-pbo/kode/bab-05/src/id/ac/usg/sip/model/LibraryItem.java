package id.ac.usg.sip.model;

public class LibraryItem {
    private String title;
    private String itemCode;
    private boolean available;

    public LibraryItem(String title,
            String itemCode) {
        if (title == null || title.isBlank()) {
            throw new IllegalArgumentException(
                "Judul tidak boleh kosong");
        }
        this.title = title;
        this.itemCode = itemCode;
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

    public String getSummary() {
        String status =
            available ? "Tersedia" : "Dipinjam";
        return title + " [" + itemCode + ", "
            + status + "]";
    }
    public void displayInfo() {
        System.out.println(getSummary());
    }
}
