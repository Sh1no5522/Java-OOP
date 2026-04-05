package prac4.Task2;

public class Main {
    public static void main(String[] args) {
        Restaurant restaurant = new Restaurant();
        restaurant.servePizza(new Cat());
        restaurant.servePizza(new Student());
    }
}
