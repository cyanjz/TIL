import java.io.IOException;

class Main {
    public static void main(String[] args) throws IOException {
        int T = read();
        StringBuilder sb = new StringBuilder();
        int[][] dp = new int[2][100000];
        for (int t = 0; t < T; t++) {
            int N = read();
            for (int i = 0; i < N; i ++) dp[0][i] = read();
            for (int i = 0; i < N; i ++) dp[1][i] = read();
            if (N==1) {
                sb.append(Math.max(dp[0][0], dp[1][0])).append("\n");
                continue;
            }
            dp[0][1] += dp[1][0];
            dp[1][1] += dp[0][0];
            for (int c = 2; c < N; c ++) {
                dp[0][c] += Math.max(dp[1][c-2], dp[1][c-1]);
                dp[1][c] += Math.max(dp[0][c-2], dp[0][c-1]);
            }
            sb.append(Math.max(dp[0][N-1], dp[1][N-1])).append("\n");
        }
        System.out.println(sb);
    }

    private static int read() throws IOException {
        int c, n = System.in.read() & 15;
        while((c=System.in.read()) > 32){
            n = (n << 3) + (n << 1) + (c & 15);
        }
        return n;
    }
}
