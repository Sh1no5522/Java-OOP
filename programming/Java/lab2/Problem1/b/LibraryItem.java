package lab2.Problem1.b;

public abstract class LibraryItem {
    private String title, author;
    private int year;
    public LibraryItem(String t, String a, int y) { title=t; author=a; year=y; }
    public String toString() { return title + " by " + author + " (" + year + ")"; }
}