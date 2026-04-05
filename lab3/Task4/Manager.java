package Task4;
import java.util.Date;
import java.util.Vector;

public class Manager extends Employee {
    public double bonus;
    public Vector<Employee> team;

    public Manager(String name, double salary, Date hireDate, String nin, double bonus) {
        super(name, salary, hireDate, nin);
        this.bonus = bonus;
        this.team = new Vector<>();
    }

    public void addEmployee(Employee e) { team.add(e); }

    @Override public String toString() {
        return super.toString() + " Manager[bonus=" + bonus + ", teamSize=" + team.size() + "]";
    }

    @Override public boolean equals(Object o) {
        if (!super.equals(o)) return false;
        if (!(o instanceof Manager)) return false;
        Manager manager = (Manager) o;
        return Double.compare(manager.bonus, bonus) == 0;
    }

    @Override public int compareTo(Employee other) {
        int res = super.compareTo(other);
        if (res == 0 && other instanceof Manager) {
            return Double.compare(this.bonus, ((Manager) other).bonus);
        }
        return res;
    }

    @Override public Manager clone() {
        Manager cloned = (Manager) super.clone();
        cloned.team = new Vector<>();
        for (Employee e : this.team) {
            cloned.team.add(e.clone()); // Deep cloning team
        }
        return cloned;
    }
}
