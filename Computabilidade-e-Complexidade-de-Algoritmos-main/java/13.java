public class AFDMaisUns {
    public static boolean maisUns(String s) {
        int count1 = 0, count0 = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') count1++;
            else if (c == '0') count0++;
        }
        return count1 > count0;
    }

    public static void main(String[] args) {
        System.out.println(maisUns("110"));    // True
        System.out.println(maisUns("10100"));  // False
    }
}
