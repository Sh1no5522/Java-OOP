package lab2.Problem2;
public abstract class Piece {
    protected Position a;
    public Piece(Position a) { this.a = a; }
    public abstract boolean isLegalMove(Position b);
}