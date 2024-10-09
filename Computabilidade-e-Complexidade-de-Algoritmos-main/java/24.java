public class AFDDuasVezes010 {
    public static boolean duasVezes010(String s) {
        int count010 = s.split("010", -1).length - 1;
        return count010 >= 2;
    }

    public static void main(String[] args) {
        System.out.println(duasVezes010("0101010"));  // True
        System.out.println(duasVezes010("101010"));   // False
    }
}
