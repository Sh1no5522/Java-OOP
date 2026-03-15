package programming.Java;

public class PalindromeCheck {

    public static boolean isPalindrome(String word) {
        String reversed = "";

        for (int i = word.length() - 1; i >= 0; i--) {
            reversed += word.charAt(i);
        }
        return word.equals(reversed);
    }

    public static void main(String[] args) {

        String text = "racecar";

        if (isPalindrome(text))
            System.out.println("Palindrome");
        else
            System.out.println("Not Palindrome");
    }
}