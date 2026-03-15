package lab2.Problem1.a;

public class Cube extends Shape3D {
    private double side;
    public Cube(double s) { this.side = s; }
    public double volume() { return Math.pow(side, 3); }
    public double surfaceArea() { return 6 * Math.pow(side, 2); }
}