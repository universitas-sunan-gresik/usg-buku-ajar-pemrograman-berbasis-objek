package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.BookDAO;
import id.ac.usg.sip.model.BookDAOImpl;
import java.util.List;

public class Bab11Demo {
    public static void main(String[] args)
            throws Exception {
        BookDAO dao = new BookDAOImpl();
        dao.delete("B001");

        Book b1 = new Book("Basis Data", "B001",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        dao.insert(b1);
        System.out.println("-- Setelah insert --");
        System.out.println(
            dao.findByCode("B001").getSummary());

        b1.borrow();
        dao.update(b1);
        Book hasil = dao.findByCode("B001");
        System.out.println("-- Setelah update --");
        System.out.println(hasil.getSummary());

        List<Book> semua = dao.findAll();
        System.out.println(
            "Jumlah baris: " + semua.size());

        dao.delete("B001");
        System.out.println("Setelah hapus: "
            + dao.findByCode("B001"));
    }
}
