public class AFNSem11Ou00 {
    public static boolean sem11Ou00(String s) {
        return !s.contains("11") && !s.contains("00");
    }

    public static void main(String[] args) {
        System.out.println(sem11Ou00("1010"));  // True
        System.out.println(sem11Ou00("1100"));  // False
    }
}
