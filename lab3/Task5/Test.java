package Task5;
import java.util.Arrays;
import Task4.Employee; // Reusing Employee from Task4
import java.util.Date;

public class Test {
    public static void main(String[] args) {
        Chocolate[] chocs = {new Chocolate("Mars", 50), new Chocolate("Twix", 45)};
        Sort.bubbleSort(chocs);
        System.out.println("Sorted Chocolates: " + Arrays.toString(chocs));

        Time[] times = {new Time(10, 30, 0), new Time(8, 15, 0)};
        Sort.selectionSort(times);
        System.out.println("Sorted Times: " + Arrays.toString(times));
        
        Employee[] emps = {
            new Employee("Zhenis", 60000, new Date(), "123"),
            new Employee("Aidan", 50000, new Date(), "456")
        };
        Sort.bubbleSort(emps);
        System.out.println("Sorted Employees: " + Arrays.toString(emps));
    }
}
