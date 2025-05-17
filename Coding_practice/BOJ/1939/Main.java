import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.PriorityQueue;


public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, M, s, e;
    static ArrayList<ArrayList<Edge>> edges;
    static int MAX_WEIGHT = 1000000000;

    public static void main(String[] args) throws Exception {
        // 1. read input
        readInput();
        // 2. run solve
        int ans = solve();
        // 3. print ans
        System.out.println(ans);
    }

    // Method to read Inputs
    public static void readInput() throws Exception {
        // 1. read N & M
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 2. initialize edges
        edges = new ArrayList<>(N);
        for (int i = 0; i < N; i ++) {
            edges.add(new ArrayList<>());
        }

        // 3. read edges
        for (int m = 0; m < M; m ++) {
            String[] line = br.readLine().split(" ");
            int start = Integer.parseInt(line[0])-1;
            int end = Integer.parseInt(line[1])-1;
            int weight = Integer.parseInt(line[2]);
            edges.get(start).add(new Edge(end, weight));
            edges.get(end).add(new Edge(start, weight));
        }

        // 4. read start, end
        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken()) - 1;
        e = Integer.parseInt(st.nextToken()) - 1;
    }

    public static int solve() {
        // Dijkstra와 유사하게 갑니다!
        PriorityQueue<Edge> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(-o1.weight, -o2.weight));
        pq.add(new Edge(s, MAX_WEIGHT));
        int[] ansArray = new int[N];
        ansArray[s] = MAX_WEIGHT;
        while (!pq.isEmpty()) {
            Edge temp = pq.poll();
            int node = temp.to;
            int curWeight = temp.weight;
            // 이미 도착 지점을 찾았으면서 curWeight가 더 작은 경우.
            if (ansArray[e] != 0 && curWeight <= ansArray[e]) {
                return ansArray[e];
            }
            // 이미 더 하중이 큰 경우를 다른 경로에서 찾은 경우는 더 이상 안봐도 됨.
            if (ansArray[node] > curWeight) {
                continue;
            }
            for (Edge edge : edges.get(node)) {
                // 다음 weight는 현재까지의 weight와 edge의 weight의 최솟값
                int nextWeight = Math.min(edge.weight, curWeight);
                // 정답 배열의 weight가 현재까지의 weight보다 크면 q에 넣지 않음.
                if (ansArray[edge.to] >= nextWeight) {
                    continue;
                }
                ansArray[edge.to] = nextWeight;
                pq.add(new Edge(edge.to, nextWeight));
            }
        }
        return ansArray[e];
    }
}


class Edge {
    int to;
    int weight;

    Edge(int to, int weight) {
        this.to = to;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "(" + to + ", " + weight + ")";
    }
}
