package programming.Java.lab1.task1;

import java.util.Scanner;

public class Analyzer {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Data data = new Data();

        while (true) {

            System.out.print("Enter number (Q to quit): ");
            String input = scanner.next();

            if (input.equalsIgnoreCase("Q"))
                break;

            try {
                double value = Double.parseDouble(input);
                data.add(value);

            } catch (NumberFormatException e) {
                System.out.println("Invalid input!");
            }
        }

        System.out.println("Average = " + data.average());
        System.out.println("Maximum = " + data.max());

        scanner.close();
    }
}
