
import java.util.Scanner;
/* Jason Zhang
112710259
CSE 114
Homework#1

 */

public class BMR {
    public static void main(String[] args) {
        Scanner weight = new Scanner(System.in);
        Scanner height = new Scanner(System.in);
        Scanner age = new Scanner(System.in);
        System.out.print("Enter weight in pound: ");
        String inweight = weight.nextLine();
        System.out.print("Enter height in inches: ");
        String inheight = height.nextLine();
        System.out.print("Enter age: ");
        String inage = age.nextLine();
        double fweight = Double.parseDouble(inweight)*0.453592, fheight = Double.parseDouble(inheight)*2.54;
        int fage = Integer.parseInt(inage);
        System.out.println("BMR for man:" + ((10*fweight) + (6.25*fheight) - 5*fage + 5) + " kcal/day");
        System.out.println("BMR for women:" + ((10*fweight) + (6.25*fheight) - 5*fage - 161) + " kcal/day");




    }

    
}
