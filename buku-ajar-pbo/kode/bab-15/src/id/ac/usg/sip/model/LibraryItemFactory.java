package id.ac.usg.sip.model;

public class LibraryItemFactory {
    public static LibraryItem createBook(
            String title, String code,
            String author, String isbn, int year) {
        return new Book(title, code, author,
            isbn, year);
    }

    public static LibraryItem createJournal(
            String title, String code,
            String publisher, int issue) {
        return new Journal(title, code,
            publisher, issue);
    }

    public static LibraryItem createDigital(
            String title, String code,
            String format, double sizeMb) {
        return new DigitalItem(title, code,
            format, sizeMb);
    }
}
