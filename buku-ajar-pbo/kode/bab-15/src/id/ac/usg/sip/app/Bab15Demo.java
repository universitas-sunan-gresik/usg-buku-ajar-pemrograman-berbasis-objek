package id.ac.usg.sip.app;

import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import javax.swing.SwingUtilities;

public class Bab15Demo {
    public static void main(String[] args)
            throws Exception {
        SipUsgApp app = new SipUsgApp();
        SwingUtilities.invokeLater(() ->
            app.setVisible(true));
        Thread.sleep(1500);

        Robot robot = new Robot();
        Rectangle area = app.getBounds();
        BufferedImage img =
            robot.createScreenCapture(area);
        ImageIO.write(img, "png",
            new File("sip-usg-app.png"));
        System.out.println(
            "SipUsgApp telah ditampilkan"
            + " dan ditangkap layarnya");
        System.exit(0);
    }
}
