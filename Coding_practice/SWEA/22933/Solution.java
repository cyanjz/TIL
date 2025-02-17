import java.util.Scanner;

public class Solution {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args){
        // read input
        int T = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < T; i ++) {
            System.out.printf("#%d %d\r\n", i+1, solve());
        }
    }

    private static int solve() {
        // input read part
        int N = Integer.parseInt(sc.nextLine());
        int[][] arr = new int[N][N];
        for (int r = 0; r < N; r ++) {
            String[] line = sc.nextLine().split(" ");
            for (int c = 0; c < N; c ++){
                arr[r][c] = Integer.parseInt(line[c]);
            }
        }
        // aps part
        int maxArea = 0;
        int cnt = 0;
        for (int r = 0; r < N; r ++) {
            for (int c = 0; c < N; c ++) {
                int curNum = arr[r][c];
                // r, c 이후의 idx들을 순회하면서 같은 숫자를 찾으면 넓이를 구하기.
                for (int i = r; i < N; i ++) {
                    for (int j = c; j < N; j ++){
                        if (curNum == arr[r][c]) {
                            int curArea = (i-r+1)*(j-c+1);
                            if (maxArea < curArea){
                                maxArea = curArea;
                                cnt = 1;
                            }
                            else if (maxArea == curArea){
                                cnt += 1;
                            }
                        }
                    }
                }
            }
        }
        return cnt;
    }
}