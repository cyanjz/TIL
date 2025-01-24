import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num1 = Integer.parseInt(br.readLine());
        String num2 = br.readLine();
        int first = num1 * (num2.charAt(2) - '0');
        int second = num1 * (num2.charAt(1) - '0');
        int third = num1 * (num2.charAt(0) - '0');
        System.out.println(first);
        System.out.println(second);
        System.out.println(third);
        System.out.println(first + second * 10 + third * 100);
    }
}