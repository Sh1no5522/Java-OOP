import os
import shutil

# This matches your folder structure: programming/Java/lab2
base_dir = "programming/Java/lab2"
old_dir = "programming/Java/lab 2"

# 1. Clean up old folders to prevent conflicts
if os.path.exists(old_dir):
    shutil.rmtree(old_dir)
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
os.makedirs(base_dir)

# 2. All files with correct package declarations
files = {
    # Problem 1a: 3D Shapes [cite: 32, 33, 34]
    "Problem1/a/Shape3D.java": 'package lab2.Problem1.a;\n\npublic abstract class Shape3D {\n    public abstract double volume();\n    public abstract double surfaceArea();\n}',
    "Problem1/a/Cylinder.java": 'package lab2.Problem1.a;\n\npublic class Cylinder extends Shape3D {\n    private double radius, height;\n    public Cylinder(double r, double h) { this.radius = r; this.height = h; }\n    public double volume() { return Math.PI * radius * radius * height; }\n    public double surfaceArea() { return 2 * Math.PI * radius * (radius + height); }\n}',
    "Problem1/a/Sphere.java": 'package lab2.Problem1.a;\n\npublic class Sphere extends Shape3D {\n    private double r;\n    public Sphere(double r) { this.r = r; }\n    public double volume() { return (4.0/3.0) * Math.PI * Math.pow(r, 3); }\n    public double surfaceArea() { return 4 * Math.PI * Math.pow(r, 2); }\n}',
    "Problem1/a/Cube.java": 'package lab2.Problem1.a;\n\npublic class Cube extends Shape3D {\n    private double side;\n    public Cube(double s) { this.side = s; }\n    public double volume() { return Math.pow(side, 3); }\n    public double surfaceArea() { return 6 * Math.pow(side, 2); }\n}',

    # Problem 1b: Library System [cite: 53, 56, 58]
    "Problem1/b/LibraryItem.java": 'package lab2.Problem1.b;\n\npublic abstract class LibraryItem {\n    private String title, author;\n    private int year;\n    public LibraryItem(String t, String a, int y) { title=t; author=a; year=y; }\n    public String toString() { return title + " by " + author + " (" + year + ")"; }\n}',
    "Problem1/b/Book.java": 'package lab2.Problem1.b;\n\npublic class Book extends LibraryItem {\n    private int pages;\n    public Book(String t, String a, int y, int p) { super(t, a, y); pages=p; }\n    public String toString() { return super.toString() + " - " + pages + " pages"; }\n}',

    # Problem 1c: Person & Employee [cite: 73, 74, 84]
    "Problem1/c/Person.java": 'package lab2.Problem1.c;\nimport java.util.Objects;\npublic class Person {\n    private String name; private int age;\n    public Person(String n, int a) { name=n; age=a; }\n    public boolean equals(Object o) {\n        if (this == o) return true;\n        if (o == null || getClass() != o.getClass()) return false;\n        Person p = (Person) o; return age == p.age && Objects.equals(name, p.name);\n    }\n    public int hashCode() { return Objects.hash(name, age); }\n}',
    "Problem1/c/Employee.java": 'package lab2.Problem1.c;\nimport java.util.Objects;\npublic class Employee extends Person {\n    private String id;\n    public Employee(String n, int a, String i) { super(n, a); id=i; }\n    public boolean equals(Object o) {\n        if (!super.equals(o)) return false;\n        Employee e = (Employee) o; return Objects.equals(id, e.id);\n    }\n    public int hashCode() { return Objects.hash(super.hashCode(), id); }\n}',

    # Problem 2: Chess [cite: 96, 97, 100]
    "Problem2/Position.java": 'package lab2.Problem2;\npublic class Position {\n    public int x, y;\n    public Position(int x, int y) { this.x = x; this.y = y; }\n}',
    "Problem2/Piece.java": 'package lab2.Problem2;\npublic abstract class Piece {\n    protected Position a;\n    public Piece(Position a) { this.a = a; }\n    public abstract boolean isLegalMove(Position b);\n}',
    "Problem2/Rook.java": 'package lab2.Problem2;\npublic class Rook extends Piece {\n    public Rook(Position a) { super(a); }\n    public boolean isLegalMove(Position b) { return a.x == b.x || a.y == b.y; }\n}',

    # Problem 3: Bank [cite: 106, 113, 134]
    "Problem3/Account.java": 'package lab2.Problem3;\npublic class Account {\n    private double balance; private int accNum;\n    public Account(int a) { balance = 0.0; accNum = a; }\n    public void deposit(double s) { if(s>0) balance+=s; }\n    public void withdraw(double s) { if(s>0 && balance>=s) balance-=s; }\n    public double getBalance() { return balance; }\n    public String toString() { return "Acc " + accNum + ": " + balance; }\n}',
    "Problem3/CheckingAccount.java": 'package lab2.Problem3;\npublic class CheckingAccount extends Account {\n    private int count; private static final double FEE = 0.02;\n    public CheckingAccount(int a) { super(a); }\n    public void deposit(double s) { super.deposit(s); count++; }\n    public void withdraw(double s) { super.withdraw(s); count++; }\n    public void deductFee() { if(count > 3) super.withdraw((count-3)*FEE); count=0; }\n}',

    # Problem 4: Electrical Circuit [cite: 142, 145, 147, 158]
    "Problem4/Circuit.java": 'package lab2.Problem4;\npublic abstract class Circuit {\n    public abstract double getResistance();\n    public abstract double getPotentialDiff();\n    public abstract void applyPotentialDiff(double V);\n    public double getPower() { return Math.pow(getPotentialDiff(), 2) / getResistance(); }\n    public double getCurrent() { return getPotentialDiff() / getResistance(); }\n}',
    "Problem4/Resistor.java": 'package lab2.Problem4;\npublic class Resistor extends Circuit {\n    private double resistance, potentialDiff;\n    public Resistor(double r) { this.resistance = r; }\n    public double getResistance() { return resistance; }\n    public double getPotentialDiff() { return potentialDiff; }\n    public void applyPotentialDiff(double V) { this.potentialDiff = V; }\n}',
    "Problem4/Series.java": 'package lab2.Problem4;\npublic class Series extends Circuit {\n    private Circuit c1, c2;\n    public Series(Circuit c1, Circuit c2) { this.c1 = c1; this.c2 = c2; }\n    public double getResistance() { return c1.getResistance() + c2.getResistance(); }\n    public double getPotentialDiff() { return c1.getPotentialDiff() + c2.getPotentialDiff(); }\n    public void applyPotentialDiff(double V) {\n        double current = V / getResistance();\n        c1.applyPotentialDiff(current * c1.getResistance());\n        c2.applyPotentialDiff(current * c2.getResistance());\n    }\n}',
    "Problem4/Parallel.java": 'package lab2.Problem4;\npublic class Parallel extends Circuit {\n    private Circuit c1, c2;\n    public Parallel(Circuit c1, Circuit c2) { this.c1 = c1; this.c2 = c2; }\n    public double getResistance() { return 1.0 / (1.0/c1.getResistance() + 1.0/c2.getResistance()); }\n    public double getPotentialDiff() { return c1.getPotentialDiff(); }\n    public void applyPotentialDiff(double V) {\n        c1.applyPotentialDiff(V);\n        c2.applyPotentialDiff(V);\n    }\n}',

    # Problem 5: Pets [cite: 183, 187, 198, 201]
    "Problem5/Animal.java": 'package lab2.Problem5;\npublic abstract class Animal {\n    private String name; private int age;\n    public Animal(String n, int a) { name=n; age=a; }\n    public abstract String getSound();\n}',
    "Problem5/Dog.java": 'package lab2.Problem5;\npublic class Dog extends Animal {\n    public Dog(String n, int a) { super(n, a); }\n    public String getSound() { return "Woof"; }\n}',
    "Problem5/Person.java": 'package lab2.Problem5;\npublic abstract class Person {\n    private String name; private Animal pet;\n    public Person(String n) { name=n; }\n    public void assignPet(Animal p) { this.pet = p; }\n    public Animal getPet() { return pet; }\n    public abstract String getOccupation();\n}',
    "Problem5/PhDStudent.java": 'package lab2.Problem5;\npublic class PhDStudent extends Person {\n    public PhDStudent(String n) { super(n); }\n    public String getOccupation() { return "PhD Student"; }\n    @Override\n    public void assignPet(Animal p) {\n        if(p instanceof Dog) throw new IllegalArgumentException("PhD students cannot have dogs.");\n        super.assignPet(p);\n    }\n}'
}

# 3. Create folders and write files
for path, content in files.items():
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Recreated lab2 with all problems (1-5) and fixed package names.")