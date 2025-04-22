import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Stack;
import java.io.FileInputStream;
import java.io.PrintStream;

class Main {
    static int[][] arr;
    static int N, W, H;
    static int[][] ds = new int[][] { { 0, 1 }, { 1, 0 }, { -1, 0 }, { 0, -1 } };
    static int totalBlocks;
    static int ans;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("sample_input.txt"));
        System.setOut(new PrintStream("output.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 1. 입력 읽어오기.
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            String[] line = br.readLine().split(" ");
            N = Integer.parseInt(line[0]);
            W = Integer.parseInt(line[1]);
            H = Integer.parseInt(line[2]);
            arr = new int[H][W];
            initArr(br);
            totalBlocks = 0;
            ans = 0;
            for (int r = 0; r < H; r++) {
                for (int c = 0; c < W; c++) {
                    if (arr[r][c] != 0) {
                        totalBlocks++;
                    }
                }
            }
            // 2. solve 함수 호출.
            solve();

            // 3. 출력.
            System.out.printf("#%d %d\n", t+1, totalBlocks - ans);
        }
    }

    // 디버깅용
    private static void printArr(int[][] arrPrint) {
        System.out.println("#####################");
        for (int i = 0; i < H; i ++) {
            for (int j = 0; j < W; j ++) {
                System.out.print(arrPrint[i][j]);
            }
            System.out.print("\n");
        }
    }

    private static void solve() {
        callDfs(0, 0);
    }

    // permutation을 구해야함. -> 재귀로 해결하자.
    // 1. 종료 조건
    //  1) depth == N : N번의 공을 모두 떨어뜨린 경우
    //  2) cnt == totalBlock : 블럭이 남아있지 않은 경우
    //  3) 블럭이 안부서진 경우
    // 2. 전달할 값
    //  1) depth : 현재까지 굴린 구슬의 수
    //  2) cnt : 현재까지 부순 블럭의 수
    // 3. 재귀 호출
    //  0) 재귀 호출이 끝난 후에 배열을 복구하기 위해 backup 형성
    //  1) c 열에 구슬을 떨어뜨렸을 때 어디까지 떨어지는지 확인.
    //  2) dfs를 통해 블럭을 부수고, 떨어뜨리기
    //  3) 재귀 호출하기. depth + 1, cnt + breaks
    //  4) 재귀 호출이 끝났으니 백업을 사용해서 원래대로 되돌리기.
    private static void callDfs(int depth, int cnt) {
        // 1-1. 종료조건 : N개의 공을 모두 떨어뜨림.
        if (depth == N) {
            ans = Math.max(cnt, ans);
        }

        // 1-2. 종료조건: 더 이상 블록이 없으면 재귀 호출할 필요가 없다.
        else if (cnt == totalBlocks) {
            ans = totalBlocks;
        }

        else {
            // 3-0. 현재 상태 백업.
            int[][] backup = new int[H][W];
            for (int i = 0; i < H; i ++) {
                for (int j = 0; j < W; j ++) {
                    backup[i][j] = arr[i][j];
                }
            }
            for (int c = 0; c < W; c ++) {
                if (ans == totalBlocks) {
                    return;
                }
                // 3-1. 구슬이 c에 떨어지면 어디까지 떨어지는지 확인.
                int r = 0;
                while (r < H && arr[r][c] == 0) {
                    r++;
                }
                // 1-3. 종료조건 : 블럭이 안 부서졌으면 탐색 더 안함.
                if (r == H) {
                    ans = Math.max(cnt, ans);
                    continue;
                }

                // 3-2. dfs
                int breaks = dfs(r, c, arr);

                // 3-3. call recur function
                callDfs(depth+1, cnt+breaks);

                // 3-4. deepcopy of backup
                for (int i = 0; i < H; i ++) {
                    for (int j = 0; j < W; j ++) {
                        arr[i][j] = backup[i][j];
                    }
                }
            }
        }
    }

    private static int dfs(int r, int c, int[][] temp) {
        // dfs1. dfs 변수 선언
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[] { r, c, temp[r][c]});
        temp[r][c] = 0;
        int cnt = 0;                // 이번 블록 부수기에서 깨진 블록의 수를 추적할 변수.

        // dfs2. run dfs
        while (!stack.isEmpty()) {
            int[] cur_loc = stack.pop(); // pop
            int dist = cur_loc[2]; // 현재 칸의 숫자, 탐색할 범위
            cnt += 1;
            for (int d = 1; d < dist; d++) { // dist 순회
                for (int i = 0; i < 4; i++) { // dir
                    int[] dir = ds[i];
                    int nr = cur_loc[0] + dir[0] * d;
                    int nc = cur_loc[1] + dir[1] * d;
                    if (0 <= nr && nr < H && 0 <= nc && nc < W) { // 인접한 칸들이 맵 안에 있어야함.
                        if (temp[nr][nc] == 0) { // 인접한 칸이 0이면 탐색 안함.
                            continue;
                        }
                        stack.push(new int[] { nr, nc, temp[nr][nc]});
                        temp[nr][nc] = 0;
                    }
                }
            }
        }
        
        // dfs3. 블록 부쉈으니 떨어뜨리기.
        for (int cw = 0; cw < W; cw++) {
            int top = H-1;
            for (int ch = H-1; ch >= 0; ch--) {
                if (temp[ch][cw] != 0) {
                    temp[top][cw] = temp[ch][cw];
                    if (top != ch) {
                        temp[ch][cw] = 0;
                    }
                    top -= 1;
                }
            }  
        }
        return cnt;
    }

    private static void initArr(BufferedReader br) throws IOException {
        for (int r = 0; r < H; r++) {
            String[] line = br.readLine().split(" ");
            for (int c = 0; c < W; c++) {
                arr[r][c] = Integer.parseInt(line[c]);
            }
        }
    }
}