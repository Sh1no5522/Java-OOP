package lab2.Problem5;
public class PhDStudent extends Person {
    public PhDStudent(String n) { super(n); }
    public String getOccupation() { return "PhD Student"; }
    @Override
    public void assignPet(Animal p) {
        if(p instanceof Dog) throw new IllegalArgumentException("PhD students cannot have dogs.");
        super.assignPet(p);
    }
}