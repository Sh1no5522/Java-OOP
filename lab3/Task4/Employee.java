package Task4;
import java.util.Date;
import java.util.Objects;

public class Employee extends Person implements Comparable<Employee>, Cloneable {
    public double salary;
    public Date hireDate;
    public String nationalInsuranceNumber;

    public Employee(String name, double salary, Date hireDate, String nin) {
        super(name);
        this.salary = salary;
        this.hireDate = hireDate;
        this.nationalInsuranceNumber = nin;
    }

    @Override public String toString() {
        return "Employee[" + name + ", salary=" + salary + ", hired=" + hireDate + ", NIN=" + nationalInsuranceNumber + "]";
    }

    @Override public boolean equals(Object o) {
        if (!super.equals(o)) return false;
        if (!(o instanceof Employee)) return false;
        Employee emp = (Employee) o;
        return Double.compare(emp.salary, salary) == 0 &&
               Objects.equals(hireDate, emp.hireDate) &&
               Objects.equals(nationalInsuranceNumber, emp.nationalInsuranceNumber);
    }

    @Override public int compareTo(Employee other) {
        return Double.compare(this.salary, other.salary);
    }

    @Override public Employee clone() {
        try {
            Employee cloned = (Employee) super.clone();
            cloned.hireDate = (Date) this.hireDate.clone(); // Deep clone for Date
            return cloned;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
