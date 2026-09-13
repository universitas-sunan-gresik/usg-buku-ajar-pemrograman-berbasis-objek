package id.ac.usg.sip.app;

import id.ac.usg.sip.model.ArchivedBookGood;
import id.ac.usg.sip.model.BookDAO;
import id.ac.usg.sip.model.BookDAOImpl;
import id.ac.usg.sip.model.LibraryService;
import id.ac.usg.sip.model.LoanValidator;

public class Bab13Demo {
    public static void main(String[] args)
            throws Exception {
        BookDAO dao = new BookDAOImpl();
        LoanValidator validator =
            new LoanValidator();
        LibraryService layanan =
            new LibraryService(dao, validator);

        layanan.processLoan("B002", "Nadia");

        try {
            layanan.processLoan("B002", "Bima");
        } catch (Exception ex) {
            System.out.println("Ditolak: "
                + ex.getMessage());
        }

        ArchivedBookGood arsip =
            new ArchivedBookGood(
                "Skripsi 2015", "S001");
        System.out.println(arsip.getSummary());
    }
}
