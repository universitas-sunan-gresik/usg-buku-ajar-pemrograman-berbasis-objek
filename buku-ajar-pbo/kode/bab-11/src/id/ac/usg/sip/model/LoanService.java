package id.ac.usg.sip.model;

public class LoanService {
    public Loan borrowItem(Member member,
            LibraryItem item, String loanDate)
            throws BookNotAvailableException {
        item.borrow();
        return new Loan(member, item, loanDate);
    }
}
