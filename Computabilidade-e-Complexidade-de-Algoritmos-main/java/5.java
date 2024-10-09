public class AFDInicioFimIgual {
    public static boolean inicioFimIgual(String s) {
        if (s.length() < 1) return false;
        return s.charAt(0) == s.charAt(s.length() - 1);
    }

    public static void main(String[] args) {
        System.out.println(inicioFimIgual("101"));  // True
        System.out.println(inicioFimIgual("100"));  // False
    }
}
