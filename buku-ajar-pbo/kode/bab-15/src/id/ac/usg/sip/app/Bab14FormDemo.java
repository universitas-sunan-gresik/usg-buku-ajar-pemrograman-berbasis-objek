package id.ac.usg.sip.app;

import id.ac.usg.sip.view.BookFormFrame;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class Bab14FormDemo {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BookFormFrame form = new BookFormFrame();
            form.setDefaultCloseOperation(
                JFrame.EXIT_ON_CLOSE);
            form.setVisible(true);
            System.out.println(
                "Form MVC telah ditampilkan");
        });
    }
}
