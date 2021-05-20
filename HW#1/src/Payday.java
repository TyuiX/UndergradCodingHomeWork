import java.util.Scanner;


public class Payday {
    public static void main(String[] args){
        System.out.println("222");
        Scanner user_input = new Scanner(System.in);
        System.out.println("Choose employee type: (m) manager (h) hourly (c) commission (p) pieceworker:");
        String employee = user_input.nextLine();
        if (employee.equals('m')) {
            System.out.println("Enter weekly Salary: ");
            Double wPay = user_input.nextDouble();
            System.out.println("Gross pay: $" + wPay);
            System.out.println("Taxes: $" + (wPay * 0.125));
            System.out.println("Net pay: $" + (wPay - (wPay * 0.125)));
        }


    }
}
