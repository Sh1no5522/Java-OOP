package programming.Java.lab1.task4;

public class Student {
    private String name;
    private int grade;
    private int id;
    private static int nextId = 1;

    public Student(String name, int grade) {
        this.name = name;
        this.grade = grade;
        this.id = nextId++;
    }

    public int getGrade() {
        return grade;
    }

    public String toString() {
        return name + " (id: " + id + ")";
    }
}