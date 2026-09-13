package id.ac.usg.sip.model;

public class Journal extends LibraryItem {
    private String publisher;
    private int issueNumber;

    public Journal(String title, String itemCode,
            String publisher, int issueNumber) {
        super(title, itemCode);
        this.publisher = publisher;
        this.issueNumber = issueNumber;
    }

    public String getPublisher() {
        return publisher;
    }

    public int getIssueNumber() {
        return issueNumber;
    }

    @Override
    public String getSummary() {
        return super.getSummary() + " - "
            + publisher + ", edisi "
            + issueNumber;
    }
}
