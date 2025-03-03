import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
    static int BUFFERSIZE = 1000;
    static int[][] buffer = new int[BUFFERSIZE][2];

    private static int dist(int r, int c, int N) {
        // r -> 1st car c -> 2nd car
        if (r == -1) {
            int r1 = 1;
            int c1 = 1;
            int r2 = buffer[c][0];
            int c2 = buffer[c][1];
            return Math.abs(r1-r2) + Math.abs(c1-c2);
        }
        else if (c == -1) {
            int r2 = N;
            int c2 = N;
            int r1 = buffer[r][0];
            int c1 = buffer[r][1];
            return Math.abs(r1-r2) + Math.abs(c1-c2);
        }
        else {
            int r1 = buffer[r][0];
            int c1 = buffer[r][1];
            int r2 = buffer[c][0];
            int c2 = buffer[c][1];
            return Math.abs(r1-r2) + Math.abs(c1-c2);
        }
    }
    private static void print(int[][] arr) {
        for (int[] row : arr) {
            for(int num : row) {
                System.out.printf("%d ", num);
            }
            System.out.println();
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int W = Integer.parseInt(br.readLine());
        for (int w = 0; w < W; w ++) {
            String[] line = br.readLine().split(" ");
            buffer[w][0] = Integer.parseInt(line[0]);
            buffer[w][1] = Integer.parseInt(line[1]);
        }
        int[][] dp = new int[W+1][W+1];
        int[][] trace = new int[W+1][W+1];
        // update dp. dp[i][j] is... remaining distance.
        // cordinate of the i-th state is buffer[5*i], buffer[5*i+2]
        for (int i = W-1; i >= 0; i--) {
            for (int j = 0; j <= i; j ++) {
                // dp[i][j].
                int n = Math.max(i, j) + 1;
                int cand1 = dp[n][j]+dist(i-1, n-1, N);
                int cand2 = dp[i][n]+dist(n-1, j-1, N);
                int cand3 = dp[n][i]+dist(j-1, n-1, N);
                int cand4 = dp[j][n]+dist(n-1, i-1, N);
                if (cand1 > cand2) {
                    dp[i][j] = cand2;
                    trace[i][j] = 2;
                }
                else {
                    dp[i][j] = cand1;
                    trace[i][j] = 1;
                }
                if (cand3 > cand4) {
                    dp[j][i] = cand4;
                    trace[j][i] = 2;
                }
                else {
                    dp[j][i] = cand3;
                    trace[j][i] = 1;
                }
                // dp[i][j] = Math.min(dp[n][j]+dist(i-1, n-1, N), dp[i][n]+dist(n-1, j-1, N));
                // dp[j][i] = Math.min(dp[n][i]+dist(j-1, n-1, N), dp[j][n]+dist(n-1, i-1, N));
            }
        }
        System.out.println(dp[0][0]);
        int i = 0;
        int j = 0;
        for (int w = 0; w < W; w ++) {
            System.out.println(trace[i][j]);
            int next = Math.max(i, j) + 1;
            if (trace[i][j] == 1) {
                i = next;
            }
            else {
                j = next;
            }
        }
    }
}