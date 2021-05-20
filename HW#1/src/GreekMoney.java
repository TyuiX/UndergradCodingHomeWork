import java.util.Scanner;

public class GreekMoney {
    public static void main(String[] args) {
        Scanner uoboloi = new Scanner(System.in);
        System.out.println("enter number of obloi");
        String oo = uoboloi.nextLine();
        int obloi = Integer.parseInt(oo), drachma = obloi/ 6, minae = drachma/70, talent = minae/60;
        minae = minae % 60;
        drachma = drachma % 70;
        obloi = obloi % 6;
        System.out.println("talent:" + talent);
        System.out.println("minae:" + minae);
        System.out.println("drachma:" + drachma);
        System.out.println("obloi:" + obloi);



    }
}
