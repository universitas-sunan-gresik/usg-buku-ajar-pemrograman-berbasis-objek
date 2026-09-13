package id.ac.usg.sip.model;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Catalog {
    private String catalogName;
    private Map<String, LibraryItem> items =
        new HashMap<>();

    public Catalog(String catalogName) {
        this.catalogName = catalogName;
    }
    public void addItem(LibraryItem item) {
        items.put(item.getItemCode(), item);
    }

    public LibraryItem findByCode(String code) {
        return items.get(code);
    }

    public List<LibraryItem> sortedByTitle() {
        List<LibraryItem> list =
            new ArrayList<>(items.values());
        list.sort(Comparator.comparing(
            LibraryItem::getTitle));
        return list;
    }

    public void displayAll() {
        System.out.println("Katalog: " + catalogName);
        for (LibraryItem it : sortedByTitle()) {
            System.out.println(
                "- " + it.getSummary());
        }
    }
}
