import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.Buffer;
import java.io.InputStreamReader;
import java.io.BufferedReader;

class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        System.setOut(new PrintStream(new FileOutputStream("output.txt")));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(br.readLine());
    }
}