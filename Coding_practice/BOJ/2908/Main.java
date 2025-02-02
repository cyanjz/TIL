import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] numbers = br.readLine().split(" ");
        int num1 = Integer.parseInt(new StringBuilder(numbers[0]).reverse().toString());
        int num2 = Integer.parseInt(new StringBuilder(numbers[1]).reverse().toString());
        if (num1 > num2) {
            System.out.println(num1);
        } else {
            System.out.println(num2);
        }
    }
}