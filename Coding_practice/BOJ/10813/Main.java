import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        int[] baskets = new int[N];
        for (int i = 0; i < N; i ++) {
            baskets[i] = i+1;
        }
        for (int i = 0; i < M; i ++) {
            String[] swapLine = br.readLine().split(" ");
            int num1 = Integer.parseInt(swapLine[0])-1;
            int num2 = Integer.parseInt(swapLine[1])-1;
            int temp = baskets[num1];
            baskets[num1] = baskets[num2];
            baskets[num2] = temp;
        }
        StringBuilder sb = new StringBuilder();
        for (int ball : baskets) sb.append(ball).append(" ");
        System.out.println(sb);
    }
}