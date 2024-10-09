public class AFDDoisUns {
    public static boolean doisUns(String s) {
        String estado = "q0";
        for (char c : s.toCharArray()) {
            if (estado.equals("q0") && c == '1') {
                estado = "q1";
            } else if (estado.equals("q1") && c == '1') {
                estado = "q2";
            } else if (estado.equals("q2") && c == '1') {
                estado = "q3";
            }
        }
        return estado.equals("q2");
    }

    public static void main(String[] args) {
        System.out.println(doisUns("1100"));  // True
        System.out.println(doisUns("111"));   // False
    }
}
