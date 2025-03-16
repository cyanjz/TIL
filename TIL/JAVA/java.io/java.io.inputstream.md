# 개요
- java에서 다양하게 입출력을 처리하는 방법을 다룹니다.

# 파일 입출력
## 파일 입출력 기본
- 아래 코드를 작성하면 buffered reader를 사용하여 파일 입출력을 받을 수 있다.
```java
import java.io.FileInputStream;
import java.io.PrintStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;


class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        System.setOut(new PrintStream("output.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    }
}
```