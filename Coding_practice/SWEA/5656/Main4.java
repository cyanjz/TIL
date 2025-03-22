import java.io.PrintStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;


// 어떤식으로 입력을 받는게 좋을까?
// N, M, W는 static 변수로 선언.
// static 영역에 최소한의 할당을 위해서 배열은 그냥 읽자.
class Main4 {
    static int N, W, H, ans, totalBlocks;
    static int[][] ds = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};
    static int[] path = new int[4];
    static int[][] arr, dump;
    static int cnt;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("sample_input.txt"));
        System.setOut(new PrintStream("output.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        // 1. 테케 순회
        for (int t = 0; t < T; t ++) {
            // 2. 입력 받아오기.
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
            arr = new int[H][W];
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
            // printArr(arr);
            // dump = new int[H][W];
            // copyArr(dump, arr);
            // printArr(dump);
            // explode(1, 2);
            // dropBlocks();
            // printArr(dump);
            // explode(2, 2);
            // dropBlocks();
            // printArr(dump);
            // System.err.println(cnt);

            // 3. ans 초기화하고 solve() 수행
            ans = 0;
            solve(0);
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

    public static void solve(int depth) {
        if (depth == N) {
            dump = new int[H][W];
            copyArr(dump, arr);
            cnt = 0;
            for (int i = 0; i < N; i ++) {
                int c = path[i];
                // 1. c 위치에 구슬을 떨어뜨렸을 때 어디에 떨어지는지 확인.
                int r = getPos(c);
                if (r == H) {
                    continue;
                }

                // 2. 블록 부수기
                explode(r, c);

                // 3. 블록 떨어뜨리기
                dropBlocks();
            }
            ans = Math.max(cnt, ans);
        }
        else {
            for (int c = 0; c < W; c ++) {
                path[depth] = c;
                solve(depth+1);
            }
        }
    }

    public static int getPos(int c) {
        int r = 0;
        if (c >= W) {
            System.out.println(c);
        }
        while (r < H && dump[r][c] == 0) {
            r ++;
        }
        return r;
    }

    public static void explode(int r, int c) {
        int dist = dump[r][c];
        dump[r][c] = 0;
        cnt++;
        for (int d = 1; d < dist; d ++) {
            for (int i = 0; i < 4; i ++) {
                int nr = r + ds[i][0]*d;
                int nc = c + ds[i][1]*d;
                if (nr < 0 || nr > H-1 || nc < 0 || nc > W-1) {
                    continue;
                }
                if (dump[nr][nc] != 0) {
                    explode(nr, nc);
                }
            }
        }
    }

    public static void dropBlocks() {
        for (int ch = 0; ch < W; ch ++) {
            int top = H-1;
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
    }

    public static void copyArr(int[][] a, int[][] b) {
        for (int r = 0; r < H; r ++) {
            for (int c = 0; c < W; c ++) {
                a[r][c] = b[r][c];
            }
        }
    }

}
