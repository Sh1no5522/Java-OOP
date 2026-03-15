package lab2.Problem4;
public class Series extends Circuit {
    private Circuit c1, c2;
    public Series(Circuit c1, Circuit c2) { this.c1 = c1; this.c2 = c2; }
    public double getResistance() { return c1.getResistance() + c2.getResistance(); }
    public double getPotentialDiff() { return c1.getPotentialDiff() + c2.getPotentialDiff(); }
    public void applyPotentialDiff(double V) {
        double current = V / getResistance();
        c1.applyPotentialDiff(current * c1.getResistance());
        c2.applyPotentialDiff(current * c2.getResistance());
    }
}