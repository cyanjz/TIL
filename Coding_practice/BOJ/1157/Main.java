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
            int idx = ((int)c)&31;
            counts[idx-1] += 1;
        }
        int maxCount = 0;
        int maxIdx = 0;
        boolean duplicated = false;
        for (int i = 0; i < 26; i++) {
            if (counts[i] > maxCount) {
                maxCount = counts[i];
                maxIdx = i;
                duplicated = false;
            }
            else if (counts[i] == maxCount) duplicated = true;
        }
        if (duplicated) {
            System.out.println('?');
            // for (Integer num : counts) {
            //     System.out.print(num + " ");
            // }
        }
        else System.out.println((char) (maxIdx+65));
    }
}