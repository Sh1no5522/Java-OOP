package lab2.Problem3;
public class CheckingAccount extends Account {
    private int count; private static final double FEE = 0.02;
    public CheckingAccount(int a) { super(a); }
    public void deposit(double s) { super.deposit(s); count++; }
    public void withdraw(double s) { super.withdraw(s); count++; }
    public void deductFee() { if(count > 3) super.withdraw((count-3)*FEE); count=0; }
}