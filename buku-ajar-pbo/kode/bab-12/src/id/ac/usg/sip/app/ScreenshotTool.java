package id.ac.usg.sip.app;

import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;
import java.io.File;

public class ScreenshotTool {
    public static void main(String[] args)
            throws Exception {
        BookFormFrame[] holder =
            new BookFormFrame[1];
        SwingUtilities.invokeAndWait(() -> {
            BookFormFrame form = new BookFormFrame();
            form.setDefaultCloseOperation(
                JFrame.DISPOSE_ON_CLOSE);
            form.setLocation(80, 80);
            form.setVisible(true);
            holder[0] = form;
        });
        Thread.sleep(1500);
        BookFormFrame form = holder[0];
        Rectangle bounds;
        Rectangle[] boundsHolder = new Rectangle[1];
        SwingUtilities.invokeAndWait(() ->
            boundsHolder[0] = form.getBounds());
        bounds = boundsHolder[0];
        Robot robot = new Robot();
        BufferedImage img =
            robot.createScreenCapture(bounds);
        ImageIO.write(img, "png",
            new File(args[0]));
        System.out.println("Tersimpan: " + args[0]);
        SwingUtilities.invokeAndWait(form::dispose);
        System.exit(0);
    }
}
