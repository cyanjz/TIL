import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int x, y, T;
    public static void main(String[] args) throws Exception {
        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            System.out.println(solve(x, y));
        }
    }

    public static int solve(int x, int y) {
        int diff = y-x;
        int result;
        // 1 : 1, 2 : 1 1 , 3 : 1 1 1, 4: 1 2 1, 5 : 1 2 1 1, 6 : 1 2 2 1, 7 : 1 2 2 1 1
        int k = (int) Math.sqrt(diff);
        if (k * k  == diff) {
            result = 2 * k - 1;
        }
        else if (k * k < diff && diff <= k * (k+1)){
            result = 2 * k;
        }
        else {
            result = 2 * k + 1;
        }
        return result;
    }
}