package id.ac.usg.sip.app;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class Bab12Demo {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BookFormFrame form = new BookFormFrame();
            form.setDefaultCloseOperation(
                JFrame.EXIT_ON_CLOSE);
            form.setVisible(true);
            System.out.println(
                "Form SIP-USG telah ditampilkan");
        });
    }
}
