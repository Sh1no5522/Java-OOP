package lab2.Problem3;
public class Account {
    private double balance; private int accNum;
    public Account(int a) { balance = 0.0; accNum = a; }
    public void deposit(double s) { if(s>0) balance+=s; }
    public void withdraw(double s) { if(s>0 && balance>=s) balance-=s; }
    public double getBalance() { return balance; }
    public String toString() { return "Acc " + accNum + ": " + balance; }
}