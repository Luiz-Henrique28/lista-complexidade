public class AFDImparAs {
    public static boolean imparAs(String s) {
        String estado = "q0";
        for (char c : s.toCharArray()) {
            if (estado.equals("q0") && c == 'a') {
                estado = "q1";
            } else if (estado.equals("q1") && c == 'a') {
                estado = "q0";
            }
        }
        return estado.equals("q1");
    }

    public static void main(String[] args) {
        System.out.println(imparAs("a"));    // True
        System.out.println(imparAs("aa"));   // False
        System.out.println(imparAs("aba"));  // True
    }
}
