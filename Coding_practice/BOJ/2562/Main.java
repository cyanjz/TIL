import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maximum = 0;
        int maxIdx = 0;
        for (int i = 0; i < 9; i ++) {
            int number = Integer.parseInt(br.readLine());
            if (number > maximum) {
                maximum = number;
                maxIdx = i+1;
            }
        }
        System.out.println(maximum);
        System.out.println(maxIdx);
    }
}