import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;

public class DisplayImage {
    public static void main(String[] args) {
        // Path to the PNG image
        String imagePath = "checker_bilevel.png"; // Assuming the image is in the current directory

        try {
            // Load the image
            BufferedImage img = ImageIO.read(new File(imagePath));

            // Create a JFrame to display the image
            JFrame frame = new JFrame("Display PNG Image");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            // Create a JLabel with the image
            JLabel label = new JLabel(new ImageIcon(img));
            frame.add(label);

            // Pack the frame to fit the image size
            frame.pack();

            // Center the frame on screen
            frame.setLocationRelativeTo(null);

            // Make the frame visible
            frame.setVisible(true);

        } catch (IOException e) {
            System.err.println("Error loading image: " + e.getMessage());
        }
    }
}