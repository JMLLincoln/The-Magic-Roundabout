package pixelchanger;

import java.awt.Dimension;
import javax.swing.JFrame;

/**
 * Pixel Changer. Changes each pixel in an image
 * 
 * if the value is between 0 and 80,
 *      set the value 0
 * if the value is between 81 and 170,
 *	set the value to 127
 * if the value is between 171 and 255,
 *	set the value to 255
 * 
 * @author Studdy
 */
public class PixelChanger extends JFrame{

    public static void main(String[] args) throws Exception {
        
        JFrame application = new JFrame("Pixel Changer");
        pixelPanel panel = new pixelPanel();
        application.add(panel);
        application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        application.setResizable(true);
        application.setSize(new Dimension(500, 500));
        application.setLocationRelativeTo(null);
        application.setVisible(true);
        
    }
    
}
