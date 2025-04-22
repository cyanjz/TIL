import java.util.Scanner;
import java.io.FileInputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;


public class Solution {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("input.txt"));
        System.setOut(new PrintStream("o.txt"));
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for (int t = 0; t < T; t ++) {
            int N = Integer.parseInt(sc.nextLine());
            ArrayList<Long> XList = new ArrayList<>();
            for (String num : sc.nextLine().split(" ")) {
                XList.add(Long.parseLong(num));
            }
            ArrayList<Long> YList = new ArrayList<>();
            for (String num : sc.nextLine().split(" ")) {
                YList.add(Long.parseLong(num));
            }
            double E = Double.parseDouble(sc.nextLine());
            Double[][] adjMat = calculateEdges(XList, YList, N, E);
            // pm(adjMat);
            int ans = (int) prim(adjMat, E, N);
            System.out.println(String.format("#%d %d", t+1, ans));
        }
        sc.close();
    }

    public static void pm(Long[][] arr) {
        int N = arr[0].length;
        for (int r = 0; r < N; r ++) {
            for (int c = 0; c < N; c ++) {
                System.out.printf("%d ", arr[r][c]);
            }
            System.out.print("\n");
        }
    }

    public static Double[][] calculateEdges(ArrayList<Long> xs, ArrayList<Long> ys, int N, double E) {
        Double[][] adjMat = new Double[N][N];
        for (int r = 0; r < N; r ++) {
            for (int c = 0; c < N; c ++) {
                adjMat[r][c] = (xs.get(r) - xs.get(c)) * (xs.get(r) - xs.get(c)) + (ys.get(r) - ys.get(c)) * (ys.get(r) - ys.get(c)) * E;
            }
        }
        return adjMat;
    }

    public static double prim(Double[][] adjMat, double E, int N) {
        PriorityQueue<Double[]> pq = new PriorityQueue<>(Comparator.comparingDouble(a-> (double) a[1]));
        int[] MST = new int[N];
        MST[0] = 1;
        double[] ds = new double[N];
        for (int idx = 0; idx < N; idx ++) {
            ds[idx] = Double.MAX_VALUE;
        }
        for (int c = 0; c < N; c++) {
            pq.add(new Double[] {(double) c, adjMat[0][c]});
        }
        double minCost = 0;
        while (!pq.isEmpty()) {
            // node, nextnode, cost
            Double[] temp = pq.poll();
            int node = temp[0].intValue();
            double cost = temp[1];

            if (MST[node] == 1) {
                continue;
            }

            MST[node] = 1;
            minCost += cost;
            for (int nextNode = 0; nextNode < N; nextNode ++) {
                double nextCost = adjMat[node][nextNode];
                if (MST[nextNode] == 1 || ds[nextNode] <= nextCost) {
                    continue;
                }
                ds[nextNode] = nextCost;
                pq.add(new Double[] {(double) nextNode, nextCost});
            }
        }
        return minCost;
    }

    public static int kruskal() {
        return 1;
    }
}
