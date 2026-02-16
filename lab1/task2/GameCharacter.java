package programming.Java.lab1.task2;

public class GameCharacter {

    enum Type {
        WARRIOR, MAGE, ARCHER
    }

    private String name;
    private Type type;
    
    private static int totalCharacters;
    
    private final int id;

    static {
        totalCharacters = 0;
        System.out.println("GameCharacter class loaded. Getting ready!");
    }

    public GameCharacter() {
        this("Unknown", Type.WARRIOR);
    }

    public GameCharacter(String name, Type type) {
        this.name = name;
        this.type = type;
        
        totalCharacters++;
        this.id = totalCharacters;
    }

    public void printInfo() {
        System.out.println("ID: " + id + " | " + name + " (" + type + ")");
    }

    public void printInfo(String prefix) {
        System.out.print(prefix + ": ");
        printInfo();
    }

    public static void main(String[] args) {
        GameCharacter p1 = new GameCharacter("Aragorn", Type.WARRIOR);
        GameCharacter p2 = new GameCharacter("Legolas", Type.ARCHER);
        GameCharacter p3 = new GameCharacter();

        p1.printInfo();
        p2.printInfo("Elf");
        p3.printInfo();

        System.out.println("Total characters: " + GameCharacter.totalCharacters);
    }
}