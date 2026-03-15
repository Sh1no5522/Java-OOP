package programming.Java;

public class SquareCalc {
    public static void main(String[] args) {

        double a = 5;   // side of square

        double area = a * a;
        double perimeter = 4 * a;
        double diagonal = Math.sqrt(2) * a;

        System.out.println("Side = " + a);
        System.out.println("Area = " + area);
        System.out.println("Perimeter = " + perimeter);
        System.out.println("Diagonal = " + diagonal);
    }
}