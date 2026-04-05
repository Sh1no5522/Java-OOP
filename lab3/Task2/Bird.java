package Task2;

public class Bird implements Flyable {
    @Override public void move() { System.out.println("Bird hops."); }
    @Override public void fly() { System.out.println("Bird flies in the sky."); }
}
