package lab2.Problem1.c;
import java.util.Objects;
public class Person {
    private String name; private int age;
    public Person(String n, int a) { name=n; age=a; }
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person p = (Person) o; return age == p.age && Objects.equals(name, p.name);
    }
    public int hashCode() { return Objects.hash(name, age); }
}