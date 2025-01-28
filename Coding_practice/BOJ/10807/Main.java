import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();
        int[] numbers = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        int v = Integer.parseInt(br.readLine());
        int ans = 0;
        for (int number : numbers) {
            if (number == v) {
                ans++;
            }
        }
        System.out.println(ans);
    }
}