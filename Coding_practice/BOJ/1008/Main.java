import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static double division(int a, int b) {
        return (double) a / b;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputList = br.readLine().split(" ");
        System.out.println(division(Integer.parseInt(inputList[0]), Integer.parseInt(inputList[1])));
    }
}