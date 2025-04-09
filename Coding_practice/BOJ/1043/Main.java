import java.util.Scanner;
import java.util.ArrayList;


public class Main {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        String[] line = sc.nextLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        int[][] input = getAdjMat(N, M);
    }

    public static int[][] readLines(int N, int M) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        for (int i = 0; i < N; i ++) {
            String[] line = sc.nextLine().split(" ");
            int num = Integer.parseInt(line[0]);
            int[] info = new int[num];
            for (int j = 0; j < num; j ++) {
                info[j] = Integer.parseInt(line[j]);
            }
            
        }
        return 
    }
}
