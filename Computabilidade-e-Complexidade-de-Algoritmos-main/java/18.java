public class AFDImparZerosUns {
    public static boolean imparZerosUns(String s) {
        int count0 = 0, count1 = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') count0++;
            else if (c == '1') count1++;
        }
        return count0 % 2 != 0 && count1 % 2 != 0;
    }

    public static void main(String[] args) {
        System.out.println(imparZerosUns("101"));   // True
        System.out.println(imparZerosUns("1100"));  // False
    }
}
