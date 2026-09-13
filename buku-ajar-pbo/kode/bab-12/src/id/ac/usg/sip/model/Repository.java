package id.ac.usg.sip.model;

import java.util.ArrayList;
import java.util.List;

public class Repository<T> {
    private List<T> data = new ArrayList<>();

    public void add(T item) {
        data.add(item);
    }

    public T getAt(int index) {
        return data.get(index);
    }

    public List<T> getAll() {
        return data;
    }

    public int count() {
        return data.size();
    }

    public static <E extends LibraryItem>
            int countAvailable(List<E> items) {
        int total = 0;
        for (E it : items) {
            if (it.isAvailable()) {
                total++;
            }
        }
        return total;
    }
}
