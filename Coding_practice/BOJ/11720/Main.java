import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String line = br.readLine();
        int ans = 0;
        for (int i = 0; i < N; i++) ans += line.charAt(i)&15;
        System.out.println(ans);
    }
}