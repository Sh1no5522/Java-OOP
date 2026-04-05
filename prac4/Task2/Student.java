package prac4.Task2;

public class Student extends Person implements CanHavePizza, CanHaveRetake, Movable {
    @Override public void eatPizza() { System.out.println("eat Pizza"); }
    @Override public void retakeExam() { System.out.println("retakeExam"); }
    @Override public void move() { System.out.println("move"); }
}
