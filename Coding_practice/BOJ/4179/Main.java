import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;


public class Main {
    static Scanner sc = new Scanner(System.in);
    // 지훈이 미로, 불 미로.
    static int[][] mazej, mazef;
    // char 형태로 들어오는 값을 int로 변환하여 저장하는 함수.
    static int maxtime = 1000*1000;
    static HashMap<Character, Integer> hm = new HashMap<>() {{
        put('#', -1);
        put('J', 0);
        put('F', 0);
        put('.', 0);
    }};
    static int[][] ds = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    static ArrayList<int[]> firststart = new ArrayList<>();
    static int[] jstart;
    public static void main(String[] args) {
        // 0. read input
        String[] line = sc.nextLine().split(" ");
        int R = Integer.parseInt(line[0]);
        int C = Integer.parseInt(line[1]);
        mazej = new int[R][C];
        mazef = new int[R][C];
        for (int r = 0; r < R; r ++) {
            String rowline = sc.nextLine();
            for (int c = 0; c < C; c ++) {
                char elem = rowline.charAt(c);
                if (elem == 'J') {
                    jstart = new int[]{r, c};
                };
                if (elem == 'F') {
                    firststart.add(new int[]{r, c});
                };
                mazej[r][c] = hm.get(elem);
                mazef[r][c] = hm.get(elem);
            }
        }
        if (jstart[0] == 0 || jstart[0] == R-1 || jstart[1] == 0 || jstart[1] == C-1) {
            System.out.println(1);
            return;
        }
        // 1. fire spreads
        ArrayDeque<int[]> q = new ArrayDeque<>();
        for (int[] sp : firststart) {
            q.add(sp);
            mazef[sp[0]][sp[1]] = 1;
        }
        while (!q.isEmpty()) {
            int[] coords = q.poll();
            int cr = coords[0];
            int cc = coords[1];
            for (int[] d : ds) {
                int nr = cr + d[0];
                int nc = cc + d[1];
                if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                    if (mazef[nr][nc] != 0) {
                        continue;
                    }
                    mazef[nr][nc] = mazef[cr][cc] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        int ans = solve(R, C);
        // printmaze(mazef);
        // printmaze(mazej);
        if (ans == -1) {
            System.out.println("IMPOSSIBLE");
        }
        else {
            System.out.println(ans);
        }
    }


    public static int solve(int R, int C) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(jstart);
        mazej[jstart[0]][jstart[1]] = 1;
        while (!q.isEmpty()) {
            int[] coords = q.poll();
            int cr = coords[0];
            int cc = coords[1];
            for (int[] d : ds) {
                int nr = cr + d[0];
                int nc = cc + d[1];
                if (0 <= nr && nr < R && 0 <= nc && nc < C && mazej[nr][nc] == 0) {
                    // 불이 더 빨리 번져 그 곳으로 갈 수 없음.
                    if (mazef[nr][nc] != 0 && mazej[cr][cc] + 1 >= mazef[nr][nc]) {
                        continue;
                    }
                    if (nr == R-1 || nc == C-1 || nr == 0 || nc == 0) return mazej[cr][cc] + 1;
                    mazej[nr][nc] = mazej[cr][cc] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        return -1;
    }


    public static void printmaze(int[][] maze) {
        for (int[] row : maze) {
            System.out.println(Arrays.toString(row));
        }
    }
}