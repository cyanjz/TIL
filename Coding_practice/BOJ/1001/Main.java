import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static int substraction(int a, int b) {
        return a - b;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input_line = br.readLine();
        String[] sList = input_line.split(" ");
        System.out.println(substraction(Integer.valueOf(sList[0]), Integer.valueOf(sList[1])));
    }
}