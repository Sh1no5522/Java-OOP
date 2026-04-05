package Task4;
import java.util.Comparator;

class NameComparator implements Comparator<Employee> {
    @Override public int compare(Employee e1, Employee e2) {
        return e1.name.compareTo(e2.name);
    }
}

class HireDateComparator implements Comparator<Employee> {
    @Override public int compare(Employee e1, Employee e2) {
        return e1.hireDate.compareTo(e2.hireDate);
    }
}
