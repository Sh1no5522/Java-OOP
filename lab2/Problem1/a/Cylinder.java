package lab2.Problem1.a;

public class Cylinder extends Shape3D {
    private double radius, height;
    public Cylinder(double r, double h) { this.radius = r; this.height = h; }
    public double volume() { return Math.PI * radius * radius * height; }
    public double surfaceArea() { return 2 * Math.PI * radius * (radius + height); }
}