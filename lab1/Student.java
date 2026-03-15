package programming.Java;

public class Student {
    private String name;
    private String id;
    private int yearOfStudy;

    public Student(String name, String id) {
        this.name = name;
        this.id = id;
        this.yearOfStudy = 1; 
    }

    public String getName() { return name; }
    public String getId() { return id; }
    public int getYearOfStudy() { return yearOfStudy; }

    public void incrementYear() {
        this.yearOfStudy++;
    }

    public static void main(String[] args) {
        Student s = new Student("User", "2026-ID");
        System.out.println("Student: " + s.getName());
        s.incrementYear();
        System.out.println("Year after increment: " + s.getYearOfStudy());
    }
}