public class AFDAoMenosUmZero {
    public static boolean aoMenosUmZero(String s) {
        String estado = "q0";
        for (char c : s.toCharArray()) {
            if (estado.equals("q0") && c == '0') {
                estado = "q1";
            }
        }
        return estado.equals("q1");
    }

    public static void main(String[] args) {
        System.out.println(aoMenosUmZero("110"));  // True
        System.out.println(aoMenosUmZero("111"));  // False
    }
}
