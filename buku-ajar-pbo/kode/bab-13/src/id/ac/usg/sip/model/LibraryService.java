package id.ac.usg.sip.model;

public class LibraryService {
    private final BookDAO dao;
    private final LoanValidator validator;

    public LibraryService(BookDAO dao,
            LoanValidator validator) {
        this.dao = dao;
        this.validator = validator;
    }

    public void processLoan(String itemCode,
            String memberName) throws Exception {
        Book b = dao.findByCode(itemCode);
        validator.validate(b);
        b.borrow();
        dao.update(b);
        double denda = b.calculateFine(1);
        System.out.println(memberName
            + " pinjam " + b.getTitle()
            + ", denda/hari Rp" + denda);
    }
}
