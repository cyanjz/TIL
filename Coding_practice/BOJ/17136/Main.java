import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] arr = new int[10][10];
    static ArrayList<int[]> targets = new ArrayList<>();
    static int[] papers = {5, 5, 5, 5, 5};
    static int ans = -1;
    
    public static void main(String[] args) throws IOException{
        readInput();
        solve(0, 0, 0);
        System.out.println(ans);
    }

    public static void readInput() throws IOException {
        for (int i = 0; i < 10; i ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 10; j ++) {
                int info = Integer.parseInt(st.nextToken());
                arr[i][j] = info;
                if (info == 1) {
                    targets.add(new int[] {i, j});
                }
            }
        }
    }

    public static void solve(int depth, int cnt, int numPapers) {
        if (cnt == targets.size()) {
            if (ans == -1) {
                ans = numPapers;
            }
            else {
                ans = Math.min(numPapers, ans);
            }
            return;
        }
        else {
            // 1. 현재 좌표 읽기
            int cr = targets.get(depth)[0];
            int cc = targets.get(depth)[1];
            // 2. 배열에서 현재 좌표가 이미 0인 경우
            if (arr[cr][cc] == 0) {
                solve(depth + 1, cnt, numPapers);
                return;
            }
            // 3. 가능한 모든 case 탐색
            for (int i = 0; i < 5; i ++) {
                if (papers[i] != 0 && isPlacable(cr, cc, i+1)) {
                    papers[i] -= 1;
                    updateArray(cr, cc, i+1, 0);
                    solve(depth + 1, cnt + (i+1) * (i+1), numPapers + 1);
                    papers[i] += 1;
                    updateArray(cr, cc, i+1, 1);
                }
            }
        }
    }

    public static boolean isPlacable(int i, int j, int size) {
        for (int r = i; r < i + size; r ++) {
            for (int c = j; c < j + size; c ++) {
                if (r >= 10 || c >= 10) {
                    return false;
                }
                if (arr[r][c] == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void updateArray(int i, int j, int size, int value) {
        for (int r = i; r < i + size; r ++) {
            for (int c = j; c < j + size; c ++) {
                arr[r][c] = value;
            }
        }
    }
}
