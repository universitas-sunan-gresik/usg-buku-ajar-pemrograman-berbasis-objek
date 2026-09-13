package id.ac.usg.sip.model;

public class Loan {
    private Member member;
    private LibraryItem item;
    private String loanDate;

    public Loan(Member member, LibraryItem item,
            String loanDate) {
        this.member = member;
        this.item = item;
        this.loanDate = loanDate;
    }

    public String getSummary() {
        return member.getName() + " meminjam "
            + item.getTitle() + " pada "
            + loanDate;
    }
}
