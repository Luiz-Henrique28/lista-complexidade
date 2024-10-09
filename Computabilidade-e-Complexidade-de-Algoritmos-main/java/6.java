public class AFNPeloMenosUmZero {
    public static boolean peloMenosUmZero(String s) {
        return s.contains("0");
    }

    public static void main(String[] args) {
        System.out.println(peloMenosUmZero("101"));  // True
        System.out.println(peloMenosUmZero("111"));  // False
    }
}
