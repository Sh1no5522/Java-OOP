package Task1;

interface Playable {
    // Contract for unrelated classes
    void play();
}

class Guitar implements Playable {
    @Override public void play() { System.out.println("Strumming guitar"); }
}

class VideoGame implements Playable {
    @Override public void play() { System.out.println("Playing video game"); }
}
