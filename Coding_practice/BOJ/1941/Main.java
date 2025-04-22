import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;


public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static String[] classroom;
  static int[] ds = {1, 0, 0, 1, -1, 0, 0, -1};
  static int ans = 0;
  public static void main(String[] args) throws Exception {
    classroom = new String[5];
    for (int i = 0; i < 5; i ++) {
      classroom[i] = br.readLine();
    }
    int[][] selected = new int[5][5];
    solve(selected, 0, 0, 0);
    System.out.println(ans);
  }

  static void solve(int[][] selected, int depth, int cnt, int idx) {
    if (depth == 7) {
      if (cnt >= 4 && check(selected)) {
        ans++;
      }
    }
    if (depth-cnt > 3) {
      return;
    }
    else {
      for (int i = idx; i < 25; i ++) {
        int r = i / 5;
        int c = i % 5;
        selected[r][c] = 1;
        if (classroom[r].charAt(c) == 'S') {
          solve(selected, depth+1, cnt+1, i+1);
        }
        else {
          solve(selected, depth+1, cnt, i+1);
        }
        selected[r][c] = 0;
      }
    }
  }

  static int[] getidx(int[][] selected) {
    for (int r = 0; r < 5; r ++) {
      for (int c = 0; c < 5; c ++) {
        if (selected[r][c] == 1) {
          return new int[] {r, c};
        }
      }
    }
    return new int[] {-1, -1};
  }

  static boolean check(int[][] selected) {
    int cnt = 0;
    ArrayDeque<int[]> q = new ArrayDeque<>();
    int[][] visited = new int[5][5];
    int[] start = getidx(selected);
    visited[start[0]][start[1]] = 1;
    q.add(start);

    while (!q.isEmpty()) {
      int[] coordinate = q.pop();
      int cr = coordinate[0];
      int cc = coordinate[1];
      cnt++;
      for (int i = 0; i < 4; i ++) {
        int dr = ds[2*i];
        int dc = ds[2*i+1];
        int nr = cr + dr;
        int nc = cc + dc;
        if (0 <= nr && nr < 5 && 0 <= nc && nc < 5) {
          if (selected[nr][nc] == 0 || visited[nr][nc] == 1) {
            continue;
          }
          q.add(new int[] {nr, nc});
          visited[nr][nc] = 1;
        }
      }
    }
    return cnt == 7;
  }
}