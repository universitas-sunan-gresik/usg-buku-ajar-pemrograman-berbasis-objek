package id.ac.usg.sip.app;

import javax.swing.JButton;

public class EventDemo {
    public static void main(String[] args) {
        JButton tombolSimpan =
            new JButton("Simpan");
        tombolSimpan.addActionListener(
            e -> System.out.println(
                "Tombol Simpan ditekan"));

        System.out.println("Simulasi klik:");
        tombolSimpan.doClick();
    }
}
