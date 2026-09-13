package id.ac.usg.sip.view;

import id.ac.usg.sip.controller.BookController;
import id.ac.usg.sip.model.Book;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableModel;

public class BookFormFrame extends JFrame {
    private final BookController controller =
        new BookController();
    private final JTextField kodeField =
        new JTextField(5);
    private final JTextField judulField =
        new JTextField(10);
    private final JTextField penulisField =
        new JTextField(8);
    private final JTextField isbnField =
        new JTextField(12);
    private final JTextField tahunField =
        new JTextField(4);
    private final String[] kolom =
        {"Kode", "Judul", "Penulis", "Tahun"};
    private final DefaultTableModel model =
        new DefaultTableModel(kolom, 0);
    private final JTable tabel = new JTable(model);

    public BookFormFrame() {
        super("SIP-USG - Data Buku (MVC)");
        setLayout(new BorderLayout());
        add(buatPanelForm(), BorderLayout.NORTH);
        add(new JScrollPane(tabel),
            BorderLayout.CENTER);
        setSize(560, 360);
        muatUlang();
    }

    private JPanel buatPanelForm() {
        JPanel baris1 = new JPanel(new FlowLayout());
        baris1.add(kodeField);
        baris1.add(judulField);
        baris1.add(penulisField);
        baris1.add(isbnField);
        baris1.add(tahunField);

        JButton tambah = new JButton("Tambah");
        tambah.addActionListener(e -> tambahBuku());
        JButton hapus = new JButton("Hapus");
        hapus.addActionListener(e -> hapusBuku());
        JButton muat = new JButton("Muat Ulang");
        muat.addActionListener(e -> muatUlang());

        JPanel baris2 = new JPanel(new FlowLayout());
        baris2.add(tambah);
        baris2.add(hapus);
        baris2.add(muat);

        JPanel panel = new JPanel(
            new GridLayout(2, 1));
        panel.add(baris1);
        panel.add(baris2);
        return panel;
    }

    private void tambahBuku() {
        try {
            controller.tambahBuku(
                judulField.getText(),
                kodeField.getText(),
                penulisField.getText(),
                isbnField.getText(),
                Integer.parseInt(
                    tahunField.getText()));
            muatUlang();
        } catch (Exception ex) {
            System.out.println(
                "Gagal tambah: " + ex.getMessage());
        }
    }

    private void hapusBuku() {
        try {
            controller.hapusBuku(
                kodeField.getText());
            muatUlang();
        } catch (Exception ex) {
            System.out.println(
                "Gagal hapus: " + ex.getMessage());
        }
    }

    private void muatUlang() {
        try {
            model.setRowCount(0);
            for (Book b : controller.semuaBuku()) {
                model.addRow(new Object[] {
                    b.getItemCode(), b.getTitle(),
                    b.getAuthor(),
                    b.getPublicationYear()});
            }
        } catch (Exception ex) {
            System.out.println(
                "Gagal muat: " + ex.getMessage());
        }
    }
}
