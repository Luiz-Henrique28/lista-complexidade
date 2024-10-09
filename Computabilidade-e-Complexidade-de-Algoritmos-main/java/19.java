public class AFNContem010 {
    public static boolean contem010(String s) {
        return s.contains("010");
    }

    public static void main(String[] args) {
        System.out.println(contem010("001010"));  // True
        System.out.println(contem010("1101"));    // False
    }
}
