// union versus bfs/dfs
// union이 훨씬 빠름.
import java.util.Scanner;


public class Main {
  static Scanner sc = new Scanner(System.in);
  static int[][] adj_mat;
  static int[] parents;
  public static void main(String[] args) {
    int N = Integer.parseInt(sc.nextLine());
    int M = Integer.parseInt(sc.nextLine());
    adj_mat = new int[N][N];
    parents = new int[N];
    for (int i = 0; i < N; i ++) {
      parents[i] = i;
    }
    for (int i = 0; i < N; i ++) {
      String[] line = sc.nextLine().split(" ");
      for (int j = 0; j < N; j ++) {
        if (line[j].equals("1")) {
          union(i, j);
        }
      }
    }
    String[] plan = sc.nextLine().split(" ");
    for (int m = 0; m < M-1; m ++) {
      int start = Integer.parseInt(plan[m])-1;
      int end = Integer.parseInt(plan[m+1])-1;
      if (get_ref(start) != get_ref(end)) {
        System.out.println("NO");
        return;
      }
    }
    System.out.println("YES");
  }

  public static int get_ref(int a) {
    if (parents[a] == a) {
      return parents[a];
    }
    else {
      parents[a] = parents[parents[a]];
      return get_ref(parents[a]);
    }
  }

  public static void union(int a, int b) {
    int a_ref = get_ref(a);
    int b_ref = get_ref(b);
    if (a_ref == b_ref) {
      return;
    }
    else {
      if (a_ref < b_ref) {
        parents[b_ref] = a_ref;
      }
      else {
        parents[a_ref] = b_ref;
      }
    }
  }
}