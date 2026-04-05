package Task4;
import java.util.Objects;

public class Person {
    public String name;

    public Person(String name) { this.name = name; }

    @Override public String toString() { return "Person: " + name; }

    @Override public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Person)) return false;
        Person person = (Person) o;
        return Objects.equals(name, person.name);
    }
}
