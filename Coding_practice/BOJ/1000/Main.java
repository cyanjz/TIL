import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;


public class Main {
    public static int addNums(int num1, int num2) {
        return num1 + num2;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String text = br.readLine();
        System.out.println(text.charAt(0) - '0' + text.charAt(2) - '0');
    }
}