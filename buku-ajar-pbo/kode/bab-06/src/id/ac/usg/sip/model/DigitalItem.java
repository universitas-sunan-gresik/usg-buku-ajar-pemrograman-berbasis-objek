package id.ac.usg.sip.model;

public class DigitalItem extends LibraryItem {
    private String format;
    private double fileSizeMb;

    public DigitalItem(String title, String itemCode,
            String format, double fileSizeMb) {
        super(title, itemCode);
        this.format = format;
        this.fileSizeMb = fileSizeMb;
    }

    public String getFormat() {
        return format;
    }

    public double getFileSizeMb() {
        return fileSizeMb;
    }

    @Override
    public String getSummary() {
        return super.getSummary() + " ("
            + format + ", " + fileSizeMb + " MB)";
    }

    @Override
    public double calculateFine(long daysLate) {
        return 0.0;
    }
}
