public class AFNContem110 {
    public static boolean contem110(String s) {
        return s.contains("110");
    }

    public static void main(String[] args) {
        System.out.println(contem110("1110"));  // True
        System.out.println(contem110("1011"));  // False
    }
}
