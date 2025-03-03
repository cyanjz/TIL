import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> hs = new HashSet<Integer>();
        for (int i = 0; i < 10 ; i++) {
            int num = Integer.parseInt(br.readLine());
            hs.add(num%42);
        }
        System.out.printf("%d", hs.size());
    }
}