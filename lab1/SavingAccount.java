package programming.Java;

public class SavingAccount {
    public static void main(String[] args) {

        double balance = 10000;   // initial balance
        double interestRate = 0.05; // 5%

        double interest = balance * interestRate;
        double newBalance = balance + interest;

        System.out.println("Initial balance: " + balance);
        System.out.println("Interest: " + interest);
        System.out.println("New balance: " + newBalance);
    }
}