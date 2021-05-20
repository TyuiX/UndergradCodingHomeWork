import java.util.Scanner;  // Import the Scanner class

public class IceCream {
    public static void main(String[] args) {
        Scanner radius = new Scanner(System.in);
        Scanner height = new Scanner(System.in);
        System.out.println("Enter radius");
        String urad = radius.nextLine();  // Read user input for radius
        System.out.println("Enter height");
        String uhei = height.nextLine();//Read user input for height
        double rad = Double.parseDouble(urad);
        double hei = Double.parseDouble(uhei);
        double volume = ((Math.PI * Math.pow(rad, 2) * hei)/3) + ((2 * Math.PI * Math.pow(rad, 3))/3);
        System.out.println("volume:" + volume);

    }
}