package prac4.Task4;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Student> list = new ArrayList<>();
        list.add(new Student("Zhenis", 3.2));
        list.add(new Student("Aidan", 3.8));
        
        Collections.sort(list);
        System.out.println("By GPA: " + list);
        
        Collections.sort(list, new NameComparator());
        System.out.println("By Name: " + list);
    }
}
