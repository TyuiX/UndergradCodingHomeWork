import java.util.Scanner;
/* Jason Zhang
112710259
CSE 114
Homework#1

 */
public class DayOfWeek {
    public static void main(String[] args) {
        Scanner user_input = new Scanner(System.in);
        System.out.print("Enter year (e.g, 1918): ");
        int year = user_input.nextInt();
        int k = year % 100;
        int j = year/100;
        System.out.print("Enter month (1-12): ");
        int month = user_input.nextInt();
        System.out.print("Enter day of the month (1-31): ");
        int day = user_input.nextInt();
        if (month == 1){
            month += 12;
            k -= 1;
        }
        else if(month == 2){
            month += 12;
            k-= 1;
        }
        int dayw = (day + ((13 * (month+1))/5) + k + (k/4) + (j/4) + (5*j)) % 7;
        String todayText = null;
        switch (dayw){
            case 1 : todayText = "Sunday" ;
                break;
            case 2 : todayText = "Monday";
                break;
            case 3 : todayText = "Tuesday";
                break;
            case 4 : todayText = "Wednesday";
                break;
            case 5 : todayText = "Thursday";
                break;
            case 6 : todayText = "Friday";
                break;
            case 0 : todayText = "Saturday";
                break;
        }
        System.out.println("The day of the week is " + todayText);

    }
}
