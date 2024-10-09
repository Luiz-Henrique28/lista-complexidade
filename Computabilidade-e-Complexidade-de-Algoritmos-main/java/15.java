public class AFNComprimentoPar {
    public static boolean comprimentoPar(String s) {
        return s.length() % 2 == 0;
    }

    public static void main(String[] args) {
        System.out.println(comprimentoPar("ab"));   // True
        System.out.println(comprimentoPar("aba"));  // False
    }
}
