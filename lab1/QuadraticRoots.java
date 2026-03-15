package programming.Java;

public class QuadraticRoots {
    public static void main(String[] args) {

        double a = 1;
        double b = -5;
        double c = 6;

        double D = b*b - 4*a*c;

        if (D < 0) {
            System.out.println("No real roots");
        } else {
            double sqrtD = Math.sqrt(D);
            double x1 = (-b + sqrtD) / (2*a);
            double x2 = (-b - sqrtD) / (2*a);

            System.out.println("x1 = " + x1);
            System.out.println("x2 = " + x2);
        }
    }
}