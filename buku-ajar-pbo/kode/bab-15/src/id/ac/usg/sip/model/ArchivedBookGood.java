package id.ac.usg.sip.model;

public class ArchivedBookGood
        implements Printable {
    private String title;
    private String itemCode;

    public ArchivedBookGood(String title,
            String itemCode) {
        this.title = title;
        this.itemCode = itemCode;
    }

    @Override
    public String getSummary() {
        return title + " [" + itemCode
            + ", Arsip]";
    }
}
