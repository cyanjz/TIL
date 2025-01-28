import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t ++) {
            String[] testLine = br.readLine().split(" ");
            String tString = testLine[1];
            int tStringLength = tString.length();
            for (int r = 0; r < Integer.parseInt(testLine[0]); r++) {
                char target = tString.charAt(r);
                for (int j = 0; j < tStringLength; j ++) {
                    sb.append(target);
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}