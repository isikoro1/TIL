package AtCoder;

import java.util.*;

class ABC422A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] S = sc.nextLine().split("-");
        int n = Integer.parseInt(S[0]);
        int m = Integer.parseInt(S[1]);

        if (n == 8) {
            m++;
            System.out.println(n + "-" + m);
        } else {
            if (m == 8) {
                m = 1;
                n++;
                System.out.println(n + "-" + m);
            } else {
                m++;
                System.out.println(n + "-" + m);
            }
        }
        sc.close();

    }
}
