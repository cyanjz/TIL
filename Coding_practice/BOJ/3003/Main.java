import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] correctNumbers = {1, 1, 2, 2, 2, 8};
        for (int i = 0; i < 6; i++) {
            sb.append(correctNumbers[i]-Integer.parseInt(st.nextToken()));
            sb.append(" ");
        }
        System.out.println(sb);
    }
}