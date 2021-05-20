import java.util.Scanner;
/* Jason Zhang
112710259
CSE 114
Homework#1

 */

public class Payday {
    public static void main(String[] args){
        double grosspay;
        Scanner user_input = new Scanner(System.in);
        System.out.print("Choose employee type: (m) manager (h) hourly (c) commission (p) pieceworker: ");
        String employee = user_input.nextLine();
        if (employee.equals("m")) {
            System.out.print("Enter weekly Salary: ");
            Double wPay = user_input.nextDouble();
            System.out.printf("Gross pay: $" + "%.2f", wPay);
            System.out.printf("\n"+"Taxes: $" + "%.2f", (wPay*0.125));
            System.out.printf("\n"+"Net pay: $" + "%.2f", (wPay-(wPay*0.125)));

        }
        else if (employee.equals("h")){
            System.out.print("Enter hourly wage: ");
            double hourlywage = user_input.nextDouble();
            System.out.print("Enter hours worked: ");
            double hoursworked = user_input.nextDouble();
            if (hoursworked <= 35) {
                grosspay = (hoursworked * hourlywage);
            }
            else {
                grosspay = (hourlywage*35)+((hoursworked - 35)*(hourlywage*2));
            }
            System.out.printf("Gross pay: $" + "%.2f", grosspay);
            System.out.printf("\n"+"Taxes: $" + "%.2f", (grosspay*0.125));
            System.out.printf("\n"+"Net pay: $" + "%.2f", (grosspay-(grosspay*0.125)));


        }
        else if (employee.equals("c")){
            System.out.print("Enter Weekly sales: ");
            double sales = user_input.nextDouble();
            grosspay = 250 + sales*0.057;
            System.out.printf("Gross pay: $" + "%.2f", grosspay);
            System.out.printf("\n"+"Taxes: $" + "%.2f", (grosspay*0.125));
            System.out.printf("\n"+"Net pay: $" + "%.2f", (grosspay-(grosspay*0.125)));

        }
        else if (employee.equals("p")){
            System.out.print("Enter pieces produced: ");
            double quanity = user_input.nextDouble();
            System.out.print("Enter pay per piece: ");
            double price = user_input.nextDouble();
            grosspay = quanity*price;
            System.out.printf("Gross pay: $" + "%.2f", grosspay);
            System.out.printf("\n"+"Taxes: $" + "%.2f", (grosspay*0.125));
            System.out.printf("\n"+"Net pay: $" + "%.2f", (grosspay-(grosspay*0.125)));
        }


    }
}
