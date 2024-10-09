public class AFNZeroSeguidoUm {
    public static boolean zeroSeguidoUm(String s) {
        return s.contains("01");
    }

    public static void main(String[] args) {
        System.out.println(zeroSeguidoUm("101"));  // True
        System.out.println(zeroSeguidoUm("111"));  // False
    }
}
