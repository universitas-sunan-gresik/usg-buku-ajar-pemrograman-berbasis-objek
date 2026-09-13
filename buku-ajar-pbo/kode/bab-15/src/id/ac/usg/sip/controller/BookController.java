package id.ac.usg.sip.controller;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.BookDAO;
import id.ac.usg.sip.model.BookDAOImpl;
import id.ac.usg.sip.model.LibraryItemFactory;
import java.util.List;

public class BookController {
    private final BookDAO dao = new BookDAOImpl();

    public List<Book> semuaBuku()
            throws Exception {
        return dao.findAll();
    }

    public void tambahBuku(String judul,
            String kode, String penulis,
            String isbn, int tahun)
            throws Exception {
        Book b = (Book) LibraryItemFactory
            .createBook(judul, kode,
                penulis, isbn, tahun);
        dao.insert(b);
    }

    public void hapusBuku(String kode)
            throws Exception {
        dao.delete(kode);
    }
}
