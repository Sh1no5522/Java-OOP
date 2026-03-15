package programming.Java.lab1.task1;

public class Data {

    private double sum;
    private double max;
    private int count;

    public Data() {
        sum = 0;
        max = -999999999;
        count = 0;
    }

    public void add(double value) {
        sum += value;

        if (value > max) {
            max = value;
        }

        count++;
    }

    public double average() {
        if (count == 0)
            return 0;

        return sum / count;
    }

    public double max() {
        if (count == 0)
            return 0;

        return max;
    }
}

