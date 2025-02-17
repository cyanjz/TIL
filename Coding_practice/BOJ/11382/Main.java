import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strList = br.readLine().split(" ");
        System.out.println(Long.parseLong(strList[0]) + Long.parseLong(strList[1])+ Long.parseLong(strList[2]));
    }
}