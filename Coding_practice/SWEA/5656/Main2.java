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

    private static void printArr(int[][] arrPrint) {
        for (int i = 0; i < H; i ++) {
            for (int j = 0; j < W; j ++) {
                System.out.print(arrPrint[i][j]);
            }
            System.out.print("\n");
        }
    }

    private static void solve() {
        // 3. 재귀 호출?
        // 이거 어케 해요?
        // N만큼 순회하면서, 각각의 case에서 값을 계산해줘야함.
        // N만큼 순회하면
        callDfs(0, 0, arr);
    }

    // permutation을 구해야함. -> 재귀로 해결하자.
    // 1. 종료 조건
    //  1) depth == N : N번의 공을 모두 떨어뜨린 경우
    //  2) cnt == totalBlock : 블럭이 남아있지 않은 경우
    //  3) 블럭이 안부서진 경우
    //  4) 
    // 2. 전달할 값
    //  1) depth : 현재까지 굴린 구슬의 수
    //  2) cnt : 현재까지 부순 블럭의 수
    //  3) map : 현재 플레이맵의 상태.
    // 3. 재귀 호출
    // 1) 0 ~ W의 위치에 구슬을 떨어뜨려야함.
    private static void callDfs(int depth, int cnt, int[][] curArr) {
        if (depth == N) {
            // System.out.println("depth end reached");
            // System.out.println(cnt);
            ans = Math.max(cnt, ans);
        }
        else if (cnt == totalBlocks) {
            ans = totalBlocks;
        }
        else {
            int[][] temp = new int[H][W];
            for (int c = 0; c < W; c ++) {
                if (ans == totalBlocks) {
                    return;
                }
                // 3-1. 구슬이 c에 떨어지면 어디까지 떨어지는지 확인.
                int r = 0;
                while (r < H && curArr[r][c] == 0) {
                    r++;
                }
                if (r == H) {
                    continue;
                }

                // 3-2. deepcopy of arr & initialize visited
                int[][] visited = new int[H][W];
                for (int i = 0; i < H; i ++) {
                    for (int j = 0; j < W; j ++) {
                        temp[i][j] = curArr[i][j];
                    }
                }

                // 3-3. dfs
                int breaks = dfs(r, c, visited, temp);

                // 3-4. call recur function
                callDfs(depth+1, cnt+breaks, temp);
            }
        }
    }

    private static int dfs(int r, int c, int[][] visited, int[][] temp) {
        // dfs1. dfs 변수 선언
        Stack<Integer[]> stack = new Stack<>();
        stack.push(new Integer[] { r, c });
        int cnt = 0;

        // dfs2. run dfs
        while (!stack.isEmpty()) {
            Integer[] cur_loc = stack.pop(); // pop
            // System.out.printf("%d %d %d %d", cur_loc[0], cur_loc[1], H, W);
            int dist = temp[cur_loc[0]][cur_loc[1]]; // 현재 칸의 숫자, 탐색할 범위
            temp[cur_loc[0]][cur_loc[1]] = 0;
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
                        if (visited[nr][nc] != 1) { // 방문한적 없으면 push
                            visited[nr][nc] = 1;
                            stack.push(new Integer[] { nr, nc });
                        }
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