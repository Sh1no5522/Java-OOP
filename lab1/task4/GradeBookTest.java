package programming.Java.lab1.task4;

import java.util.Scanner;

public class GradeBookTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        Course course = new Course("CS101", "Object-oriented Programming", 5, "None");
        GradeBook gb = new GradeBook(course);

        gb.displayMessage();
        
        System.out.println("Please, input grades for students (type 'Q' to finish):");

        while (true) {
            System.out.print("Student Name: ");
            String name = sc.next();
            if (name.equalsIgnoreCase("Q")) break;

            System.out.print("Grade: ");
            if (sc.hasNextInt()) {
                int grade = sc.nextInt();
                gb.addStudent(new Student(name, grade));
            } else {
                sc.next();
                break;
            }
        }

        gb.displayGradeReport();
        sc.close();
    }
}