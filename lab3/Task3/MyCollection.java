package Task3;

// Maximum general (abstract) collection possible[cite: 76].
public interface MyCollection<E> {
    boolean add(E element);
    boolean remove(Object o);
    boolean contains(Object o);
    boolean isEmpty();
    int size();
    void clear();
}
