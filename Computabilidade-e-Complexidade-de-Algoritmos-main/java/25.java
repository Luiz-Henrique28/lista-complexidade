public class AFNAAntesDeB {
    public static boolean aAntesDeB(String s) {
        return !s.contains("ba");
    }

    public static void main(String[] args) {
        System.out.println(aAntesDeB("aaabbb"));  // True
        System.out.println(aAntesDeB("abba"));    // False
    }
}
