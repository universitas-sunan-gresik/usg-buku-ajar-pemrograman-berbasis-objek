package id.ac.usg.sip.model;

public class Loan {
    private Member member;
    private Book book;
    private String loanDate;

    public Loan(Member member, Book book,
            String loanDate) {
        this.member = member;
        this.book = book;
        this.loanDate = loanDate;
    }

    public String getSummary() {
        return member.getName() + " meminjam "
            + book.getTitle() + " pada "
            + loanDate;
    }
}
