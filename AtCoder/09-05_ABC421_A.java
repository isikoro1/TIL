package AtCoder_2025;
// 解説の実装例の写経
// 提出時はMain.javaにしないと実行エラーとなるので、class に publicを除外
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = Integer.parseInt(scanner.nextLine());
        String[] S = new String[N];
        for (int i = 0; i < N; i++) {
            S[i] = scanner.nextLine();
        }

        String[] XY = scanner.nextLine().split(" ");
        int X = Integer.parseInt(XY[0]);
        String Y = XY[1];

        if (S[X-1].equals(Y)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}