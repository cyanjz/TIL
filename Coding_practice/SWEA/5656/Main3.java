// import java.io.PrintStream;
// import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;


// 어떤식으로 입력을 받는게 좋을까?
// N, M, W는 static 변수로 선언.
// static 영역에 최소한의 할당을 위해서 배열은 그냥 읽자.
class Main3 {
    static int N, W, H, ans, totalBlocks;
    static int[][] stack = new int[12*15][3];
    static int[][] ds = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};
    public static void main(String[] args) throws Exception {
        // System.setIn(new FileInputStream("sample_input.txt"));
        // System.setOut(new PrintStream("output.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int[][] arr = new int[15][12];
        int T = Integer.parseInt(st.nextToken());
        // 1. 테케 순회
        for (int t = 0; t < T; t ++) {
            // 2. 입력 받아오기.
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
            totalBlocks = 0;
            for (int r=0; r<H; r++) {
                st = new StringTokenizer(br.readLine());
                for (int c=0; c<W; c++) {
                    int num = Integer.parseInt(st.nextToken());
                    arr[r][c] = num;
                    if (num != 0) {
                        totalBlocks++;
                    }
                }
            }

            // 2-0 디버깅용
            // int[][] dump = new int[H][W];
            // copyArr(dump, arr);
            // System.out.println(dfs(1, 2, dump));
            // printArr(dump);
            // System.out.println(dfs(2, 2, dump));
            // printArr(dump);

            // 3. ans 초기화하고 solve() 수행
            ans = 0;
            solve(0, 0, arr);
            System.out.println(String.format("#%d %d", t+1, totalBlocks-ans));
        }
    }

    public static void printArr(int[][] arr) {
        System.out.println("###########");
        for (int[] row:arr) {
            for (int c = 0; c < W;c ++) {
                System.out.print(row[c]);
            }
            System.out.print("\n");
        }
    }

    public static void solve(int depth, int cnt, int[][] temp) {
        if (ans == totalBlocks) {
            return;
        }
        if (cnt == totalBlocks) {
            ans = totalBlocks;
            return;
        }
        else if (depth == N) {
            // printArr(temp);
            ans = Math.max(ans, cnt);
        }
        else {
            for (int c = 0; c < W; c ++) {
                // 1. c 위치에 구슬을 떨어뜨렸을 때 어디에 떨어지는 지 확인.
                int r = 0;
                while (r < H && temp[r][c] == 0) {
                    r ++;
                }
                if (r == H) {
                    continue;
                }

                // 2. 해당 위치에 대해서 dfs를 수행하고, 부서진 블럭의 수를 계산
                int[][] dump = new int[H][W];
                copyArr(dump, temp);
                int breaks = dfs(r, c, dump);
                
                // 3. 해당 배열을 재귀적으로 호출
                solve(depth+1, cnt+breaks, dump);
            }
        }
    }

    public static int dfs(int r, int c, int[][] dump) {
        // 1. dfs 변수 초기화
        int cnt = 0;
        int top = 0;
        stack[top][0] = r;
        stack[top][1] = c;
        stack[top][2] = dump[r][c];
        dump[r][c] = 0;

        // 2. dfs 수행
        while (top != -1) {
            int cr = stack[top][0];
            int cc = stack[top][1];
            int dist = stack[top--][2];
            cnt++;
            for (int d = 1; d < dist; d ++) {
                for (int i = 0; i < 4; i ++) {
                    int nr = cr + ds[i][0] * d;
                    int nc = cc + ds[i][1] * d;
                    if (nr < 0 || nr >= H || nc < 0 || nc >= W) {
                        continue;
                    }
                    if (dump[nr][nc] != 0) {
                        stack[++top][0] = nr;
                        stack[top][1] = nc;
                        stack[top][2] = dump[nr][nc];
                        dump[nr][nc] = 0;
                    }
                }
            }
        }
        
        // 3. 블록 아래로 내리기.
        for (int ch = 0; ch < W; ch ++) {
            top = H-1;
            for (int cr = H-1; cr >= 0; cr--) {
                if (dump[cr][ch] == 0) {
                    continue;
                }
                dump[top][ch] = dump[cr][ch];
                if (top != cr) {
                    dump[cr][ch] = 0;
                }
                top--;
            }
        }
        return cnt;
    }

    public static void copyArr(int[][] a, int[][] b) {
        for (int r = 0; r < H; r ++) {
            for (int c = 0; c < W; c ++) {
                a[r][c] = b[r][c];
            }
        }
    }

}
