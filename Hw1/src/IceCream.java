import java.util.Scanner;
/* Jason Zhang
112710259
CSE 114
Homework#1

 */
public class IceCream {
    public static void main(String[] args) {
        Scanner radius = new Scanner(System.in);
        Scanner height = new Scanner(System.in);
        System.out.print("Enter radius of ice cream and cone (in inches): ");
        double rad = radius.nextDouble();  // Read user input for radius
        System.out.print("Enter height of cone (in inches): ");
        String uhei = height.nextLine();//Read user input for height
        double hei = Double.parseDouble(uhei);
        double volume = ((Math.PI * Math.pow(rad, 2) * hei)/3) + ((2 * Math.PI * Math.pow(rad, 3))/3);
        System.out.println("Volume of ice cream (in cubic inches): " + volume);

    }
}