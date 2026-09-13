package id.ac.usg.sip.model;

import java.sql.SQLException;
import java.util.List;

public interface BookDAO {
    void insert(Book book) throws SQLException;

    Book findByCode(String itemCode)
        throws SQLException;

    List<Book> findAll() throws SQLException;

    void update(Book book) throws SQLException;

    void delete(String itemCode)
        throws SQLException;
}
