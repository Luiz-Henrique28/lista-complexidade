public class AFN01Termina10 {
    public static boolean comeca01Termina10(String s) {
        return s.startsWith("01") && s.endsWith("10");
    }

    public static void main(String[] args) {
        System.out.println(comeca01Termina10("0110"));  // True
        System.out.println(comeca01Termina10("0100"));  // False
    }
}
