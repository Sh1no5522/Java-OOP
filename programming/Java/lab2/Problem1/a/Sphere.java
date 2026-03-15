package lab2.Problem1.a;

public class Sphere extends Shape3D {
    private double r;
    public Sphere(double r) { this.r = r; }
    public double volume() { return (4.0/3.0) * Math.PI * Math.pow(r, 3); }
    public double surfaceArea() { return 4 * Math.PI * Math.pow(r, 2); }
}