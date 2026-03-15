package lab2.Problem5;
public abstract class Person {
    private String name; private Animal pet;
    public Person(String n) { name=n; }
    public void assignPet(Animal p) { this.pet = p; }
    public Animal getPet() { return pet; }
    public abstract String getOccupation();
}