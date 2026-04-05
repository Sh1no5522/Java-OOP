package Task6;

// Implementing existing Comparable and Cloneable interfaces
public class Person implements Comparable<Person>, Cloneable {
    String name;
    public Person(String name) { this.name = name; }
    
    @Override public int compareTo(Person o) { return this.name.compareTo(o.name); }
    @Override public Person clone() throws CloneNotSupportedException { return (Person) super.clone(); }
}
