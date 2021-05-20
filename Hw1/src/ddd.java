import java.util.Scanner;
public class ddd {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.print("Enter an integer to be a limit of the pattern:");
        int limit = input.nextInt();
        for (int a = 1; a <= limit; a++) {
            for (int a2 = 1; a2 <= a; a2++) {
                System.out.print(a2 + " ");
            }
            System.out.println();
        }
        for (int b = limit; b >= 1; b--) {
            for (int b2 = b; b2 >= 1; b2--) {
                System.out.print(b2 + " ");
            }
            System.out.println();
        }
        for (int b = limit; b >= 1; b--) {
            for (int b2 = b; b2 >= 1; b2--) {
                System.out.print(b2 + " ");
            }
            System.out.println();
        }
        System.out.println("Pattern C");
        for (int c = 1; c <= limit; c++) {
            for (int c2 = limit; c2 >= 1; c2--) {
                if (c2 > c) {
                    System.out.print(" ");
                } else {
                    System.out.print(c2);
                }
            }
            System.out.println();
        }
        System.out.println("Pattern D");
        for (int i = 0; i < limit; i++) {

            for (int j = 1 - i; j <= limit - i; j++) {

                if (j < 1) System.out.print(" ");
                else System.out.print(j + " ");

            }

            System.out.println();

        }

    }
}


