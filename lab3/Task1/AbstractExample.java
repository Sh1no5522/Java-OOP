package Task1;

abstract class Animal {
    String name;
    // Shared code for related classes
    public void sleep() { System.out.println("Zzz..."); }
    public abstract void makeSound();
}

class Dog extends Animal {
    @Override public void makeSound() { System.out.println("Woof"); }
}
