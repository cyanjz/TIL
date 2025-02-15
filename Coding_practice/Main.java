import java.io.IOException;

public class Main {
    static byte[] input = new byte[2000003];
    static int bytesRead = 0;
    public static void main(String[] args) throws IOException {
        bytesRead = System.in.read(input); // 읽어들인 byte 수.
        int[] counts = new int[26];
        for (int i = 0; i < bytesRead; i ++) {
            int c = input[i];
            if (c == 13 | c == 10) break; // \r이나 \n이 발견되면 종료.
            System.out.println(c);
        }
    }
}