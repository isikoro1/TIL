package AtCoder_2025;
import java.util.Scanner;

// AtCoderでの過去の提出コードの写経
class CounterManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int backNum = -1;
        int[] days = new int[n];

        for (int i=0; i<n; i++) {
            days[i] = sc.nextInt();
        }
        sc.close();

        for (int i=0; i<n; i++) {
            
            if (backNum != -1) {
                if (days[i] == backNum) {
                    System.out.println("stay");
                } else if (days[i] < backNum) {
                    int x = backNum - days[i];
                    System.out.println("down " + x);
                } else {
                    int x = days[i] - backNum;
                    System.out.println("up " + x);
                }
            }
            backNum = days[i];
        }

    }

}