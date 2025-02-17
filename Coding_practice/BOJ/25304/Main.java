import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long X = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        long Y = 0L;
        for (int i = 0; i < N; i++) {
            String[] inputString = br.readLine().split(" ");
            Y += Integer.parseInt(inputString[0]) * Integer.parseInt(inputString[1]);
        }
        if (X==Y) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}