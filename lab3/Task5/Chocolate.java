package Task5;

public class Chocolate implements Comparable<Chocolate> {
    public double weight;
    public String name;

    public Chocolate(String name, double weight) {
        this.name = name;
        this.weight = weight;
    }

    @Override public String toString() { return name + "(" + weight + "g)"; }

    @Override public int compareTo(Chocolate other) {
        return Double.compare(this.weight, other.weight);
    }
}
