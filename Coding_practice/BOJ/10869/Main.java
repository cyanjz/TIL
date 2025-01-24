import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] inputList = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(Calculator.addition(inputList[0], inputList[1]));
        System.out.println(Calculator.substraction(inputList[0], inputList[1]));
        System.out.println(Calculator.multiplication(inputList[0], inputList[1]));
        System.out.println(Calculator.division(inputList[0], inputList[1]));
        System.out.println(Calculator.divMod(inputList[0], inputList[1]));
    }
}

class Calculator {
    public static int division(int a, int b) {
        return a/b;
    }
    public static int divMod(int a, int b) {
        return a%b;
    }
    public static int addition(int a, int b) {
        return a + b;
    }
    public static int substraction(int a, int b) {
        return a - b;
    }
    public static int multiplication(int a, int b) {
        return a * b;
    }

}