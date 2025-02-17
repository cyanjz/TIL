import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nmLine = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(nmLine[0]);
        int M = Integer.parseInt(nmLine[1]);
        int[] baskets = new int[N];
        for (int m = 0; m < M; m ++) {
            String[] line = br.readLine().split(" ");
            int start = Integer.parseInt(line[0]);
            int end = Integer.parseInt(line[1]);
            int number = Integer.parseInt(line[2]);
            for (int idx = start-1; idx < end; idx ++) {
                baskets[idx] = number;
            }
        }
        for (int num : baskets) {
            sb.append(num).append(" ");
        }
        System.out.print(sb);
    }
}