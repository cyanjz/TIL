# 기본적인 형태
```java
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
```
- 여기서 bytes에 하나씩 저장되려면 Ascii 형식에 해당하는 character가 들어와야함.
- 기본적으로 char는 2byte이지만, Ascii 형식은 1byte로 표현 가능하므로, 1byte에 표현된다.
- 그렇지 않을 경우에는 여러 byte에 걸쳐서 할당된다.