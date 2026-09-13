package id.ac.usg.sip.app;

import id.ac.usg.sip.model.DatabaseConnection;
import id.ac.usg.sip.model.LibraryItem;
import id.ac.usg.sip.model.LibraryItemFactory;

public class Bab14Demo {
    public static void main(String[] args) {
        DatabaseConnection c1 =
            DatabaseConnection.getInstance();
        DatabaseConnection c2 =
            DatabaseConnection.getInstance();
        System.out.println(
            "Instance sama? " + (c1 == c2));

        LibraryItem j = LibraryItemFactory
            .createJournal("Jurnal AI", "J002",
                "USG Press", 3);
        System.out.println(j.getSummary());
    }
}
