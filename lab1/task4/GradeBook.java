package programming.Java.lab1.task4;

import java.util.ArrayList;

public class GradeBook {
    private Course course;
    private ArrayList<Student> students;

    public GradeBook(Course course) {
        this.course = course;
        this.students = new ArrayList<>();
    }

    public void addStudent(Student s) {
        students.add(s);
    }

    public void displayMessage() {
        System.out.println("Welcome to the grade book for " + course.toString() + "!");
    }

    public void displayGradeReport() {
        if (students.isEmpty()) return;

        double sum = 0;
        Student low = students.get(0);
        Student high = students.get(0);

        for (Student s : students) {
            sum += s.getGrade();
            if (s.getGrade() < low.getGrade()) low = s;
            if (s.getGrade() > high.getGrade()) high = s;
        }

        System.out.printf("Class average is %.2f. Lowest grade is %d (%s). Highest grade is %d (%s).\n",
                (sum / students.size()), low.getGrade(), low, high.getGrade(), high);
        
        outputBarChart();
    }

    private void outputBarChart() {
        System.out.println("Grades distribution:");
        int[] dist = new int[11];
        for (Student s : students) {
            dist[Math.min(s.getGrade() / 10, 10)]++;
        }

        for (int i = 0; i < dist.length; i++) {
            if (i == 10) System.out.print("  100: ");
            else System.out.printf("%02d-%02d: ", i * 10, i * 10 + 9);
            
            for (int j = 0; j < dist[i]; j++) System.out.print("*");
            System.out.println();
        }
    }
}