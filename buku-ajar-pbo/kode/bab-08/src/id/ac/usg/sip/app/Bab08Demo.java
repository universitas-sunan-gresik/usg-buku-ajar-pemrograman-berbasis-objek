package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.BookNotAvailableException;
import id.ac.usg.sip.model.Loan;
import id.ac.usg.sip.model.LoanService;
import id.ac.usg.sip.model.LoanSession;
import id.ac.usg.sip.model.Member;

public class Bab08Demo {
    public static void main(String[] args) {
        Book b1 = new Book("Basis Data", "B001",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        Member m1 = new Member("20240001",
            "Nadia Ramadhani", "nadia@usg.ac.id");
        LoanService layanan = new LoanService();

        try {
            Loan p1 = layanan.borrowItem(
                m1, b1, "2026-09-14");
            System.out.println(p1.getSummary());
        } catch (BookNotAvailableException e) {
            System.out.println("Gagal: "
                + e.getMessage());
        }

        try {
            layanan.borrowItem(
                m1, b1, "2026-09-15");
        } catch (BookNotAvailableException e) {
            System.out.println("Gagal: "
                + e.getMessage());
        }

        try (LoanSession sesi =
                new LoanSession("Nadia")) {
            sesi.process();
        }
    }
}
