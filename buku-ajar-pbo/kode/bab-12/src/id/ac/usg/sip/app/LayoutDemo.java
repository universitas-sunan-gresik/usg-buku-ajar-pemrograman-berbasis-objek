package id.ac.usg.sip.app;

import java.awt.BorderLayout;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class LayoutDemo {
    public static void main(String[] args) {
        JPanel panel = new JPanel(
            new BorderLayout());
        panel.add(new JLabel("Judul Form"),
            BorderLayout.NORTH);
        panel.add(new JLabel("Tabel Data"),
            BorderLayout.CENTER);
        panel.add(new JLabel("Tombol Aksi"),
            BorderLayout.SOUTH);
        System.out.println(
            "Komponen ditambahkan: "
            + panel.getComponentCount());
    }
}
