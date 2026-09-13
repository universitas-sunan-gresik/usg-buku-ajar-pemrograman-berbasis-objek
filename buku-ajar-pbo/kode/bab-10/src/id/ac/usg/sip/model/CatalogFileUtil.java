package id.ac.usg.sip.model;

import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class CatalogFileUtil {
    public static void saveItems(
            List<LibraryItem> items, String path)
            throws IOException {
        try (ObjectOutputStream out =
                new ObjectOutputStream(
                    new FileOutputStream(path))) {
            out.writeObject(items);
        }
    }

    @SuppressWarnings("unchecked")
    public static List<LibraryItem> loadItems(
            String path)
            throws IOException,
            ClassNotFoundException {
        try (ObjectInputStream in =
                new ObjectInputStream(
                    new FileInputStream(path))) {
            return (List<LibraryItem>)
                in.readObject();
        }
    }

    public static void exportTitlesCsv(
            List<LibraryItem> items, String path)
            throws IOException {
        Path tujuan = Path.of(path);
        try (BufferedWriter w =
                Files.newBufferedWriter(tujuan)) {
            w.write("itemCode,title");
            w.newLine();
            for (LibraryItem it : items) {
                w.write(it.getItemCode() + ","
                    + it.getTitle());
                w.newLine();
            }
        }
    }

    public static List<String> readTitlesCsv(
            String path) throws IOException {
        List<String> baris =
            Files.readAllLines(Path.of(path));
        List<String> judul = new ArrayList<>();
        for (int i = 1; i < baris.size(); i++) {
            String[] kolom = baris.get(i).split(",");
            judul.add(kolom[1]);
        }
        return judul;
    }
}
