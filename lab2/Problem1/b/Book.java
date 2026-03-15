package lab2.Problem1.b;

public class Book extends LibraryItem {
    private int pages;
    public Book(String t, String a, int y, int p) { super(t, a, y); pages=p; }
    public String toString() { return super.toString() + " - " + pages + " pages"; }
}