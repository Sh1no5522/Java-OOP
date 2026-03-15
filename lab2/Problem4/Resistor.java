package lab2.Problem4;
public class Resistor extends Circuit {
    private double resistance, potentialDiff;
    public Resistor(double r) { this.resistance = r; }
    public double getResistance() { return resistance; }
    public double getPotentialDiff() { return potentialDiff; }
    public void applyPotentialDiff(double V) { this.potentialDiff = V; }
}