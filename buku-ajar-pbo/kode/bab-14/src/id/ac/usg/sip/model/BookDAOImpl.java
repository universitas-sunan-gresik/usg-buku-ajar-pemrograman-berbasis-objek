package id.ac.usg.sip.model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class BookDAOImpl implements BookDAO {
    private static final String SQL_INSERT =
        "INSERT INTO books (item_code, title, "
        + "author, isbn, publication_year) "
        + "VALUES (?, ?, ?, ?, ?)";
    private static final String SQL_FIND_BY_CODE =
        "SELECT * FROM books WHERE item_code = ?";
    private static final String SQL_FIND_ALL =
        "SELECT * FROM books ORDER BY title";
    private static final String SQL_UPDATE =
        "UPDATE books SET title=?, author=?, "
        + "isbn=?, publication_year=?, "
        + "available=? WHERE item_code=?";
    private static final String SQL_DELETE =
        "DELETE FROM books WHERE item_code = ?";

    @Override
    public void insert(Book book)
            throws SQLException {
        try (Connection conn =
                DatabaseConnection.getInstance()
                    .getConnection();
            PreparedStatement ps = conn
                .prepareStatement(SQL_INSERT)) {
            ps.setString(1, book.getItemCode());
            ps.setString(2, book.getTitle());
            ps.setString(3, book.getAuthor());
            ps.setString(4,
                book.getIsbn().getValue());
            ps.setInt(5,
                book.getPublicationYear());
            ps.executeUpdate();
        }
    }

    @Override
    public Book findByCode(String itemCode)
            throws SQLException {
        try (Connection conn =
                DatabaseConnection.getInstance()
                    .getConnection();
            PreparedStatement ps = conn
                .prepareStatement(
                    SQL_FIND_BY_CODE)) {
            ps.setString(1, itemCode);
            try (ResultSet rs =
                    ps.executeQuery()) {
                return rs.next()
                    ? toBook(rs) : null;
            }
        }
    }

    @Override
    public List<Book> findAll()
            throws SQLException {
        List<Book> hasil = new ArrayList<>();
        try (Connection conn =
                DatabaseConnection.getInstance()
                    .getConnection();
            PreparedStatement ps = conn
                .prepareStatement(SQL_FIND_ALL);
            ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                hasil.add(toBook(rs));
            }
        }
        return hasil;
    }

    @Override
    public void update(Book book)
            throws SQLException {
        try (Connection conn =
                DatabaseConnection.getInstance()
                    .getConnection();
            PreparedStatement ps = conn
                .prepareStatement(SQL_UPDATE)) {
            ps.setString(1, book.getTitle());
            ps.setString(2, book.getAuthor());
            ps.setString(3,
                book.getIsbn().getValue());
            ps.setInt(4,
                book.getPublicationYear());
            ps.setBoolean(5,
                book.isAvailable());
            ps.setString(6, book.getItemCode());
            ps.executeUpdate();
        }
    }

    @Override
    public void delete(String itemCode)
            throws SQLException {
        try (Connection conn =
                DatabaseConnection.getInstance()
                    .getConnection();
            PreparedStatement ps = conn
                .prepareStatement(SQL_DELETE)) {
            ps.setString(1, itemCode);
            ps.executeUpdate();
        }
    }

    private Book toBook(ResultSet rs)
            throws SQLException {
        Book b = new Book(
            rs.getString("title"),
            rs.getString("item_code"),
            rs.getString("author"),
            rs.getString("isbn"),
            rs.getInt("publication_year"));
        b.setAvailable(
            rs.getBoolean("available"));
        return b;
    }
}
