import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;


public class Main {
    public static void main(String[] args) {
        // read input
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int E = Integer.parseInt(line[1]);
        ArrayList<ArrayList<int[]>> adj_mat = new ArrayList<>();
        for (int i = 0; i < N; i ++) {
            adj_mat.add(new ArrayList<int[]>());
        }
        int s, e, w;
        for (int i = 0; i < E; i ++) {
            line = sc.nextLine().split(" ");
            s = Integer.parseInt(line[0]);
            e = Integer.parseInt(line[1]);
            w = Integer.parseInt(line[2]);
            int[] edge = {e-1, w};
            adj_mat.get(s-1).add(edge);
            int[] rev_edge = {s-1, w};
            adj_mat.get(e-1).add(rev_edge);
        }
        // for (ArrayList<Integer[]> row : adj_mat){
        //     for (Integer[] edge : row) {
        //         System.out.printf("%d %d\n", edge[0], edge[1]);
        //     }
        // }
        line = sc.nextLine().split(" ");
        int u1 = Integer.parseInt(line[0])-1;
        int u2 = Integer.parseInt(line[1])-1;
        System.out.println(solve(N, E, u1, u2, adj_mat));
    }

    public static int solve(int N, int E, int u1, int u2, ArrayList<ArrayList<int[]>> adj_mat) {
        int[] d1 = dijstra(0, N, adj_mat);
        int[] d2 = dijstra(u1, N, adj_mat);
        int[] d3 = dijstra(u2, N, adj_mat);
        // 0 -> u1 -> u2 -> N, 0 -> u2 -> u1 -> N
        if (d1[u1] == Integer.MAX_VALUE || d2[u2] == Integer.MAX_VALUE || d3[N-1] == Integer.MAX_VALUE) {
            return -1;
        }
        if (d1[u2] == Integer.MAX_VALUE || d3[u1] == Integer.MAX_VALUE || d2[N-1] == Integer.MAX_VALUE) {
            return -1;
        }
        int u1first = d1[u1] + d2[u2] + d3[N-1];
        int u2first = d1[u2] + d3[u1] + d2[N-1];
        int ans = (u1first > u2first)? u2first : u1first;
        // System.out.println(Arrays.toString(d1));
        // System.out.println(Arrays.toString(d2));
        // System.out.println(Arrays.toString(d3));
        // System.out.println(ans);
        return ans;
    }

    public static int[] dijstra(int s, int N, ArrayList<ArrayList<int[]>> adj_mat){
        int[] D = new int[N];
        Arrays.fill(D, Integer.MAX_VALUE);
        D[s] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a->a[0]));
        pq.add(new int[]{0, s});
        while (!pq.isEmpty()) {
            int[] cursor = pq.poll();
            int cost = cursor[0];
            int node = cursor[1];
            if (D[node] < cost) continue;
            for (int[] edge : adj_mat.get(node)) {
                int next = edge[0];
                int nextcost = edge[1];
                if (D[next] <= cost + nextcost) continue;
                D[next] = cost + nextcost;
                pq.add(new int[]{D[next], next});
            }
        }
        return D;
    }
}
