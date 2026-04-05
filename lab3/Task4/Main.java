package Task4;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Employee e1 = new Employee("Aidan", 50000, new GregorianCalendar(2020, Calendar.JANUARY, 1).getTime(), "KZ123");
        Employee e2 = new Employee("Zhenis", 60000, new GregorianCalendar(2021, Calendar.JUNE, 10).getTime(), "KZ456");
        Manager m1 = new Manager("Boss", 60000, new GregorianCalendar(2015, Calendar.MARCH, 5).getTime(), "KZ999", 5000);
        
        m1.addEmployee(e1);
        m1.addEmployee(e2);

        System.out.println("Test Equals: " + e1.equals(e2));
        
        Manager m2 = m1.clone();
        System.out.println("Test Clone: " + (m1 != m2 && m1.equals(m2)));

        List<Employee> list = Arrays.asList(e2, e1, m1);
        Collections.sort(list); // Sort by Salary
        System.out.println("By Salary: " + list);
        
        list.sort(new NameComparator());
        System.out.println("By Name: " + list);
    }
}
