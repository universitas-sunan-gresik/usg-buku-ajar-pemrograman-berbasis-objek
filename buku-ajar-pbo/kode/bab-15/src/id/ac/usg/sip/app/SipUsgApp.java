package id.ac.usg.sip.app;

import id.ac.usg.sip.view.BookFormFrame;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;

public class SipUsgApp extends JFrame {
    public SipUsgApp() {
        super("SIP-USG - Sistem Informasi "
            + "Perpustakaan");
        setJMenuBar(buatMenuBar());
        add(buatLabelSambutan());
        setSize(420, 180);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private JMenuBar buatMenuBar() {
        JMenuBar bar = new JMenuBar();
        JMenu menuModul = new JMenu("Modul");

        JMenuItem itemBuku =
            new JMenuItem("Data Buku");
        itemBuku.addActionListener(e ->
            new BookFormFrame()
                .setVisible(true));
        menuModul.add(itemBuku);

        JMenuItem itemKeluar =
            new JMenuItem("Keluar");
        itemKeluar.addActionListener(
            e -> System.exit(0));
        menuModul.add(itemKeluar);

        JMenu menuBantuan = new JMenu("Bantuan");
        JMenuItem itemTentang =
            new JMenuItem("Tentang");
        itemTentang.addActionListener(e ->
            JOptionPane.showMessageDialog(this,
                "SIP-USG dibangun bertahap dari"
                + " Bab II hingga Bab XIV.",
                "Tentang SIP-USG",
                JOptionPane
                    .INFORMATION_MESSAGE));
        menuBantuan.add(itemTentang);

        bar.add(menuModul);
        bar.add(menuBantuan);
        return bar;
    }

    private JLabel buatLabelSambutan() {
        return new JLabel(
            "<html><center>Selamat datang"
            + " di SIP-USG<br>Pilih menu Modul"
            + " untuk memulai</center></html>",
            SwingConstants.CENTER);
    }
}
