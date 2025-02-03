
# Primitives
## Numericals
1. 표현 범위

| 자료형  | 표현 범위                                |
|---------|------------------------------------------|
| int     | -2147483648 ~ 2147483647                |
| long    | -9223372036854775808 ~ 9223372036854775807 |
| byte    | -128 ~ 127                              |
| short   | -32768 ~ 32767                          |
| float   | -3.4e38 ~ 3.4e38                        |
| double  | -1.7e308 ~ 1.7e308                      |

2. 16진수/8진수
```java
// 0으로 시작하면 8진수
int oct = 023
// 0x로 시작하면 16진수
int hex = 0xC3
```

## Boolean
- true, false

## Character
1. 문자
```java
char a1 = 'a'; // 문자로 표현
char a2 = 97; // ASCII code
char a3 = '\u0061' // unicode
```

# Non-primitives
## Strings (java.lang.String)
- immutable
- methods
```java
String test = "1 2 3 4 5";
String[] test0 = test.split(" "); // ["1", "2", "3", "4", "5"]
Char test1 = test.charAt(idx);
test.compareTo("string"); // compares two string lexicographically(alphabetic order).
test.concat(" 6 7 8 9"); // "1 2 3 4 5 6 7 8 9"
test.join(sep, String1, String2, ...); // String1{sep}String2{sep}...
test.substring(int start, int end);
test.indexOf(3); // 4
```
- window의 경우에는 줄바꿈에서 \r과 \n이 같이 입력된다.

# Collections
## Primitive Array
- int[], bool[], ...
- 크기를 늘릴 수 없다.

## Objective Array
- String[]
- Object array

## ArrayList
### 특징
- 배열 공간이 꽉 찰 때마다 배열을 copy하는 방식으로 늘리므로 지연이 발생한다.
- 삽입/삭제 동작은 느리다.
### methods
- add(e) : add an element at the end of the ArrayList
- get(idx) : return an element at an idx
- set(idx, e) : change an element at an idx to e
- remove(idx) : remove an element at an idx
- clear() : remove all elements of the ArrayList
- size() : return a size of the ArrayList
```java
import java.util.ArrayList;
import java.util.Arrays;

public class JavaTest {
    public static void main(String[] args) {
        ArrayList<String> test = new ArrayList<>(Arrays.asList("1", "2", "3"));
        test.add("4");
        System.out.println(test); // [1, 2, 3, 4]
        System.out.println(test.get(0)); // 1
        test.set(0, "100"); 
        System.out.println(test); // [100, 2, 3, 4]
        test.remove(0);
        System.out.println(test); // [2, 3, 4]
        System.out.println(test.size()); // 3
        test.clear();
        System.out.println(test); // []
    }
}
```

## HashMap
- Python dictionary와 비슷
```java
import java.util.HashMap;

Hashmap<String, Integer> map = new HashMap<>(); // key와 value의 data type을 미리 선언.
map.put("name", 3); // hashmap에 새로운 원소를 넣는 method.
```