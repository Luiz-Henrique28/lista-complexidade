public class AFDExatamenteUmAb {
    public static boolean exatamenteUmAb(String s) {
        int countAb = s.split("ab", -1).length - 1;
        return countAb == 1;
    }

    public static void main(String[] args) {
        System.out.println(exatamenteUmAb("abab"));  // False
        System.out.println(exatamenteUmAb("aab"));   // True
    }
}
