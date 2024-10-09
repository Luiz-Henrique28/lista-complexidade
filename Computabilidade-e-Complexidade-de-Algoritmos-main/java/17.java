public class AFNTermina01 {
    public static boolean termina01(String s) {
        return s.endsWith("01");
    }

    public static void main(String[] args) {
        System.out.println(termina01("1101"));  // True
        System.out.println(termina01("1000"));  // False
    }
}
