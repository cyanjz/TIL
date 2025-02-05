import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;

class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in))
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int[][] dp = {
                {0, 0},
                {0, 0}
            };
            int N = Integer.parseInt(br.readLine());
            StringTokenizer row1 = new StringTokenizer(br.readLine());
            StringTokenizer row2 = new StringTokenizer(br.readLine());
            dp[0][0] = Integer.parseInt(row1.nextToken());
            dp[1][0] = Integer.parseInt(row2.nextToken());
            dp[0][1] = Integer.parseInt(row1.nextToken()) + dp[1][0];
            dp[1][1] = Integer.parseInt(row2.nextToken()) + dp[0][0];
            for (int c = 2; c < N; c ++) {
                int temp = 0;
                for (int r = 0; r < 2; r++) {
                    for (int i = 0; i < 2; i++) temp += dp[0][i]
                }
                temp = dp[0];
            }
        }
    }
}