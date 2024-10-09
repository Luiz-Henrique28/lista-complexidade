public class AFDParDeZeros {
    public static boolean parDeZeros(String s) {
        String estado = "q0";
        for (char c : s.toCharArray()) {
            if (estado.equals("q0")) {
                if (c == '0') estado = "q1";
                else if (c == '1') estado = "q0";
            } else if (estado.equals("q1")) {
                if (c == '0') estado = "q0";
                else if (c == '1') estado = "q1";
            }
        }
        return estado.equals("q0");
    }

    public static void main(String[] args) {
        System.out.println(parDeZeros("101"));  // True
        System.out.println(parDeZeros("100"));  // False
    }
}
