public class AFNDivisivelPor3Zeros {
    public static boolean divisivelPor3Zeros(String s) {
        int countZeros = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') countZeros++;
        }
        return countZeros % 3 == 0;
    }

    public static void main(String[] args) {
        System.out.println(divisivelPor3Zeros("000111"));  // True
        System.out.println(divisivelPor3Zeros("0011"));    // False
    }
}
