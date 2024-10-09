public class AFDBlocosDeZeros {
    public static boolean blocosDeZeros(String s) {
        String estado = "q0";
        for (char c : s.toCharArray()) {
            if (estado.equals("q0") && c == '0') {
                estado = "q1";
            } else if (estado.equals("q1")) {
                if (c == '1') estado = "q2";
            } else if (estado.equals("q2") && c == '0') {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(blocosDeZeros("00111"));  // True
        System.out.println(blocosDeZeros("010"));    // False
    }
}
