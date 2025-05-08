import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.ArrayDeque;


public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static ArrayList<ArrayList<Integer>> adj, revAdj;
    static int N, M;

    public static void main(String[] args) throws Exception{
        N = Integer.parseInt(br.readLine());
        // 1. initialize adj & rev adj list
        adj = new ArrayList<>();
        revAdj = new ArrayList<>();
        for (int i = 0; i < N; i ++) {
            adj.add(new ArrayList<>());
            revAdj.add(new ArrayList<>());
        }
        // 2. read edges
        M = Integer.parseInt(br.readLine());
        for (int n = 0; n < M; n ++) {
            String[] line = br.readLine().split(" ");
            int s = Integer.parseInt(line[0]) - 1;
            int e = Integer.parseInt(line[1]) - 1;
            adj.get(s).add(e);
            revAdj.get(e).add(s);
        }
        for (int node : solve()) {
            System.out.println(node);
        }
    }

    public static int[] solve() {
        int[] result = new int[N];
        for (int node = 0; node < N; node ++) {
            int comparable = bfs(node, adj) + bfs(node, revAdj);
            result[node] = N - comparable - 1;
        }
        return result;
    }

    public static int bfs(int s, ArrayList<ArrayList<Integer>> adj_list) {
        int[] visited = new int[N];
        visited[s] = 1;
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(s);
        int cnt = 0;
        while (!q.isEmpty()) {
            int node = q.poll();
            for (int adjNode : adj_list.get(node)) {
                if (visited[adjNode] == 1) {
                    continue;
                }
                visited[adjNode] = 1;
                cnt++;
                q.add(adjNode);
            }
        }
        return cnt;
    }
}
