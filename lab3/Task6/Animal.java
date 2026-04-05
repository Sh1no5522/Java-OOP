package Task6;

public abstract class Animal {
    String type;
    public Animal(String type) { this.type = type; }
}

class Pet extends Animal implements Trainable, Feedable, Comparable<Pet> {
    String name;
    
    public Pet(String type, String name) {
        super(type);
        this.name = name;
    }

    @Override public void doTrick() { System.out.println(name + " did a backflip!"); }
    @Override public void feed() { System.out.println(name + " is eating."); }
    @Override public int compareTo(Pet o) { return this.name.compareTo(o.name); }
}
