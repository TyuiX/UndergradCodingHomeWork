import java.util.Scanner;
/* Jason Zhang
112710259
CSE 114
Homework#1

 */
public class GreekMoney {
    public static void main(String[] args) {
        Scanner uoboloi = new Scanner(System.in);
        System.out.print("Enter number of oboloi: ");
        String oo = uoboloi.nextLine();
        int obloi = Integer.parseInt(oo), drachma = obloi/ 6, minae = drachma/70, talent = minae/60;
        minae = minae % 60;
        drachma = drachma % 70;
        obloi = obloi % 6;
        System.out.println("That number of oboloi is equal to: ");
        System.out.println(talent + " talents");
        System.out.println(minae + " minae");
        System.out.println(drachma + " drachmae");
        System.out.println(obloi + " oboloi");



    }
}
