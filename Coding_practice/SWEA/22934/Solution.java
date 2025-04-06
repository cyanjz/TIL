import java.io.FileInputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;


public class Solution {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("input.txt"));
        System.setOut(new PrintStream("out.txt"));
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine().split(" ")[0]);
        for (int t = 0; t < T; t ++) {
            int ans = solve(sc);
            System.out.println(String.format("#%d %d", t+1, ans));
        }
    }

    public static int solve(Scanner sc) {
        // read input
        String[] line1 = sc.nextLine().split(" ");
        String[] line2 = sc.nextLine().split(" ");
        int V = Integer.parseInt(line1[0]);
        int E = Integer.parseInt(line1[1]);
        // make adjList & inorder
        int[] inorder = new int[V];
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < V; i ++) {
            adjList.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < E; i ++) {
            int s = Integer.parseInt(line2[2*i])-1;
            int e = Integer.parseInt(line2[2*i+1])-1;
            adjList.get(s).add(e);
            inorder[e]++;
        }
        // find roots & initialize depth
        Queue<Integer> queue = new LinkedList<>();
        int[] depths = new int[V];
        for (int i = 0; i < V; i ++) {
            if (inorder[i] == 0) {
                queue.offer(i);
                depths[i] = 1;
            }
        }
        // run bfs with topological sort
        while (!queue.isEmpty()) {
            int cur_node = queue.poll();
            for (Integer nextNode : adjList.get(cur_node)) {
                inorder[nextNode]--;
                if (inorder[nextNode] == 0) {
                    queue.offer(nextNode);
                    depths[nextNode] = Math.max(depths[cur_node] + 1, depths[nextNode]);
                }
            }
        }

        return getMax(depths);
    }

    public static int getMax(int[] depths) {
        int maxDepth = 0;
        for (int depth : depths) {
            maxDepth = depth > maxDepth ? depth : maxDepth;
        }
        return maxDepth;
    }
}
