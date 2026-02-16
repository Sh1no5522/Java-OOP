package programming.Java;

public class Time {
    private int hour;
    private int minute;
    private int second;

    // Constructor with parameters
    public Time(int hour, int minute, int second) {
        setTime(hour, minute, second);
    }

    // Method to validate and set time
    public void setTime(int hour, int minute, int second) {
        if (hour >= 0 && hour < 24 && minute >= 0 && minute < 60 && second >= 0 && second < 60) {
            this.hour = hour;
            this.minute = minute;
            this.second = second;
        } else {
            // Default to 0 if invalid, just to be safe
            this.hour = 0; this.minute = 0; this.second = 0;
        }
    }

    // Convert to Universal format (23:05:06)
    public String toUniversal() {
        return String.format("%02d:%02d:%02d", this.hour, this.minute, this.second);
    }

    // Convert to Standard format (11:05:06 PM)
    public String toStandard() {
        int h = (this.hour == 0 || this.hour == 12) ? 12 : this.hour % 12;
        String period = (this.hour < 12) ? "AM" : "PM";
        return String.format("%02d:%02d:%02d %s", h, this.minute, this.second, period);
    }

    // Add method to add two time objects
    public void add(Time t) {
        this.second += t.second;
        this.minute += this.second / 60;
        this.second %= 60;

        this.minute += t.minute;
        this.hour += this.minute / 60;
        this.minute %= 60;

        this.hour = (this.hour + t.hour) % 24;
    }

    public static void main(String[] args) {
        // EXACT usage from the problem description [cite: 26-31]
        Time t = new Time(23, 5, 6);
        System.out.println(t.toUniversal()); // prints "23:05:06"
        System.out.println(t.toStandard());  // prints "11:05:06 PM"
        
        Time t2 = new Time(4, 24, 33);
        t.add(t2);
        
        // I added these print statements so you can see the result of the addition
        System.out.println("After adding t2:");
        System.out.println(t.toUniversal());
    }
}