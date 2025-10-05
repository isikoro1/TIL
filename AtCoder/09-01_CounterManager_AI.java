package AtCoder_2025;
import java.io.BufferedReader;
import java.io.InputStreamReader;

// 過去のAtCorderの提出コードをChatGPTにリファクタリングしてもらったコード
class CounterManager_AI  {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());
        long prev = Long.parseLong(br.readLine().trim());

        StringBuilder out = new StringBuilder();

        for (int i = 1; i < n; i++) {
            long cur = Long.parseLong(br.readLine().trim());
            if (cur == prev) {
                out.append("stay\n");
            } else if (cur > prev) {
                out.append("up").append(cur - prev).append('\n');
            } else {
                out.append("down").append(prev - cur).append('\n');
            }
            prev = cur;
        }
        
        System.out.print(out.toString());
    }
}
