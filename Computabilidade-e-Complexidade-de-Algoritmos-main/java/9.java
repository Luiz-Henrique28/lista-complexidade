public class AFDContem101 {
    public static boolean contem101(String s) {
        return s.contains("101");
    }

    public static void main(String[] args) {
        System.out.println(contem101("1101"));  // True
        System.out.println(contem101("1110"));  // False
    }
}
