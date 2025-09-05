package AtCoder_2025;
import java.util.*;

// AtCoderABC421_B Fibonacci Reversed 提出コード

class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        long x = sc.nextInt();
        long y = sc.nextInt();

        long[] arr = new long[10];
        arr[0] = x;
        arr[1] = y;

        for (int i = 2; i < 10; i++) {
            arr[i] = arr[i - 2] + arr[i - 1];
            arr[i] = reverseNumber(arr[i]);
        }
        System.out.println(arr[9]);
    } 

    static long reverseNumber(long num) {
        long rev = 0;
        while (num > 0) {
            rev = rev * 10 + (num % 10);
            num /= 10;
        }
        return rev;
    }
}