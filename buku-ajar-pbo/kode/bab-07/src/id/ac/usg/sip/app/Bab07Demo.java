package id.ac.usg.sip.app;

import id.ac.usg.sip.model.Book;
import id.ac.usg.sip.model.DueDateReminder;
import id.ac.usg.sip.model.Journal;
import id.ac.usg.sip.model.Printable;

public class Bab07Demo {
    public static void main(String[] args) {
        Book b1 = new Book("Basis Data", "B001",
            "Kadir, A.", "978-602-04-0001-1", 2012);
        Journal j1 = new Journal(
            "Jurnal SI", "J001",
            "USG Press", 12);

        b1.printLabel();
        System.out.println(
            Printable.formatCode(b1.getItemCode()));

        System.out.println(
            "Tersedia? " + b1.isAvailable());
        b1.borrow();
        System.out.println(
            "Tersedia? " + b1.isAvailable());
        b1.returnItem();

        DueDateReminder pengingat =
            (nama, judul) -> System.out.println(
                nama + ", segera kembalikan "
                + judul);
        pengingat.remind("Nadia", j1.getTitle());
    }
}
