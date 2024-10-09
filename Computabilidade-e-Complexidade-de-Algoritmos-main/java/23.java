public class AFNContem101Ou110 {
    public static boolean contem101Ou110(String s) {
        return s.contains("101") || s.contains("110");
    }

    public static void main(String[] args) {
        System.out.println(contem101Ou110("1101"));  // True
        System.out.println(contem101Ou110("1001"));  // False
    }
}
