package prac4.Bonus;
import java.util.Arrays;

public class CountingSort {
    public static void sort(int[] arr) {
        int[] count = new int[11];
        for (int x : arr) count[x]++;
        int index = 0;
        for (int i = 0; i < count.length; i++) {
            while (count[i] > 0) {
                arr[index++] = i;
                count[i]--;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {10, 2, 5, 2, 1, 0, 9};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
