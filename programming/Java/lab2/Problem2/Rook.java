package lab2.Problem2;
public class Rook extends Piece {
    public Rook(Position a) { super(a); }
    public boolean isLegalMove(Position b) { return a.x == b.x || a.y == b.y; }
}