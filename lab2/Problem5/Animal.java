package lab2.Problem5;
public abstract class Animal {
    private String name; private int age;
    public Animal(String n, int a) { name=n; age=a; }
    public abstract String getSound();
}