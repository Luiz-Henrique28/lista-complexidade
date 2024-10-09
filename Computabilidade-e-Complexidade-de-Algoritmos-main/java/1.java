public class AFDTerminaCom1 {
    public static boolean terminaCom1(String s) {
        String estado = "q0";
        for (char c : s.toCharArray()) {
            if (estado.equals("q0")) {
                if (c == '0') estado = "q0";
                else if (c == '1') estado = "q1";
            } else if (estado.equals("q1")) {
                if (c == '0') estado = "q0";
                else if (c == '1') estado = "q1";
            }
        }
        return estado.equals("q1");
    }

    public static void main(String[] args) {
        System.out.println(terminaCom1("101"));  // True
        System.out.println(terminaCom1("100"));  // False
    }
}
