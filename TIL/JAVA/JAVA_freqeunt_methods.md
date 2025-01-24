# JAVA freqeuntly used methods
## In/out
- IOException, InputStreamReader, BufferedReader : 이 세 개 사용!
- 문제를 풀 때 많이 사용되는 method.
- Arrays.stream을 사용하면 array의 원소들을 로부터 sequential Stream을 얻을 수 있다.
- 뭔가를 하고 마지막에 toArray를 작성.
```java
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in))
        String text = br.readline();
        int[] int_array = Arrays.stream(text.split()).mapToInt(Integer::parseInt).toArray();
        int[] intArray = Arrays.stream(text.split())
        System.out.println(Arrays.toString(int_array));
    }
}
```