package programming.Java.lab1.task5;

import java.util.Vector;
import java.util.Scanner;

public class DragonLaunch {
    private Vector<Person> people;

    public DragonLaunch() {
        people = new Vector<>();
    }

    public void kidnap(Person p) {
        people.add(p);
    }

    public boolean willDragonEatOrNot() {
        int boysWaiting = 0;
        
        for (Person p : people) {
            if (p.getGender() == Gender.BOY) {
                boysWaiting++;
            } else {
                if (boysWaiting > 0) {
                    boysWaiting--;
                } else {
                    return true;
                }
            }
        }
        
        return boysWaiting != 0;
    }

    public static void main(String[] args) {
        DragonLaunch dl = new DragonLaunch();
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter order of students (B for Boy, G for Girl, Q to finish):");
        
        while (true) {
            String input = sc.next().toUpperCase();
            if (input.equals("Q")) break;
            
            if (input.equals("B")) {
                dl.kidnap(new Person(Gender.BOY));
            } else if (input.equals("G")) {
                dl.kidnap(new Person(Gender.GIRL));
            } else {
                System.out.println("Invalid input! Use B or G.");
            }
        }
        
        if (dl.willDragonEatOrNot()) {
            System.out.println("The Dragon will have a launch!");
        } else {
            System.out.println("No one left for launch. The students vanished!");
        }
        
        sc.close();
    }
}