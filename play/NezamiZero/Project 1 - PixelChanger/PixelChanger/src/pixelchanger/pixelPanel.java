package pixelchanger;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

/**
 *
 * @author Studdy
 */
public class pixelPanel extends JPanel {

    JButton loadImage;
    JButton changePixels;
    boolean imageLoaded = false;
    Color c;
    int average;
    int[][] pixels;

    BufferedImage img;

    pixelPanel() throws Exception {

        loadImage = new JButton("Load Image");
        add(loadImage);
        loadImage.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent ae) {

                try {
                    loadImage(JOptionPane.showInputDialog("Enter full image URL: "));
                } catch (Exception ex) {
                    Logger.getLogger(pixelPanel.class.getName()).log(Level.SEVERE, null, ex);
                }
                imageLoaded = true;
                repaint();

            }

        });

        changePixels = new JButton("Change Pixels");
        add(changePixels);
        changePixels.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent ae) {

                if (imageLoaded) {
                    pixels = new int[img.getWidth()][img.getHeight()];
                    for (int i = 0; i < img.getWidth(); i++) {
                        for (int j = 0; j < img.getHeight(); j++) {
                            pixels[i][j] = img.getRGB(i, j);
                            c = new Color(pixels[i][j]);                
                            
                            average = (c.getRed() + c.getGreen() + c.getBlue()) / 3;
                            if(average <= 80){
                                c = new Color(90, 30, 30, 255);
                            } else if (average >= 81 && average <= 170){
                                c = new Color(90, 45, 45, 255);
                            } else if (average >= 171 && average <= 255){
                                c = new Color(255, 60, 60, 255);
                            }
                            
                            int RGB = c.getRGB();
                            img.setRGB(i, j, RGB);
                            
                        }
                    }
                repaint();
                }

            }

        });

    }

    public BufferedImage loadImage(String s) throws Exception {

        URL url = new URL(s);
        img = toBufferedImage(ImageIO.read(url));
        return img;

    }

    public static BufferedImage toBufferedImage(Image img) {

        if (img instanceof BufferedImage) {
            return (BufferedImage) img;
        }

        BufferedImage bImage = new BufferedImage(img.getWidth(null),
                img.getHeight(null), BufferedImage.TYPE_INT_ARGB);

        Graphics2D bGr = bImage.createGraphics();
        bGr.drawImage(img, 0, 0, null);
        bGr.dispose();

        return bImage;

    }

    public void paint(Graphics g) {
        super.paint(g);

        g.drawImage(img, 0, 40, this);
    }

}
