import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N;
    static int MAX_HEIGHT = 11;
    static int[][] parents;

    // 1. parents 배열 만들기
    public static void init() throws Exception {
        N = Integer.parseInt(br.readLine());
        // parents i, j -> 2^j-th parent of i-th node
        parents = new int[N+1][MAX_HEIGHT];
        String[] line = br.readLine().split(" ");
        // root = 0으로 가자.
        for (int i = 0; i < line.length; i ++) {
            parents[i+2][0] = i+2;
            parents[i+2][1] = Integer.parseInt(line[i]);
        }
        for (int i = 0; i < MAX_HEIGHT; i ++) {
            parents[1][i] = 1;
        }
        // parents 배열 초기화
        // root node -> leaf node 순으로 업데이트
        // 0은 무조건 자기자신.
        // 0 -> 자기자신, 1 -> 2 ^ (1-1) th parent, ...
        // 어떤 노드의 2^j 번째 부모는 해당 노드의 2^j-1 번째 부모의 2^j-1번째 부모와 같다.
        for (int j = 2; j < N; j ++) {
            for (int k = 2; k < MAX_HEIGHT; k ++) {
                parents[j][k] = parents[parents[j][k-1]][k-1];
            }
        }
    }


    // 2. main 함수
    public static void main(String[] args) throws Exception{
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t ++) {
            init();
            System.out.println("##################");
            for (int[] row : parents) {
                for (int p : row) {
                    System.out.print(p);
                }
                System.out.print('\n');
            }
        }
    }
}