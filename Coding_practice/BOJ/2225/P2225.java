import java.util.Scanner;

public class P2225 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int div = 1000000000;
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] dp = new int[N+1];
        dp[0] = 1;
        for (int k = 1; k <= K; k ++) {
            for (int n = 1; n <= N; n ++) {
                dp[n] = (dp[n] + dp[n-1]) % div;
            }
        }
        System.out.println(dp[N]);
    }
}