package lab2.Problem1.c;
import java.util.Objects;
public class Employee extends Person {
    private String id;
    public Employee(String n, int a, String i) { super(n, a); id=i; }
    public boolean equals(Object o) {
        if (!super.equals(o)) return false;
        Employee e = (Employee) o; return Objects.equals(id, e.id);
    }
    public int hashCode() { return Objects.hash(super.hashCode(), id); }
}