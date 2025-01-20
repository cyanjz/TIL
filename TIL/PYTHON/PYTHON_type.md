# TYPE
**이 문서에서는 PYTHON에 존재하는 여러 type들을 기술합니다.**
## 개요
### 정의
- 변수나 값이 가질 수 있는 데이터의 종류. 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는 지를 정의.
### 존재 이유
- 데이터 타입에 맞는 연산이 존재.
- 데이터 타입 별로 정의되는 method가 다름.
- 잘못된 데이터 타입으로 인해 발생하는 오류를 방지.
## Numeric Type
### Integer(Decimal)
- 1, 2, 3, 4... 과 같은 정수를 10진법으로 나타내는 자료형
### Non-decimal
```python
# 2진수
0b11 == 3
# 8진수
0o72 == 9
# 16진수
0xa1 == 12
```
### Float
- 1.2, 1.5... 와 같은 실수를 나타내는 자료형
```python
num1 = 314e-2
num2 = 3.14
```
#### Floating point rounding error
```python
# Floating point roundig error occurs
num1 = 3.2
num2 = 1.2
num1 -= 3
num2 -= 1
num1 == num2 # false
```
```PYTHON
# Decimal
from decimal import Decimal
num1 = Decimal("3.2") - Decimal("3.0")
num2 = Decimal("1.2") - Decimal("1.0")
num1 == num2 # true
```

## Sequence Type
- 여러 개의 값들을 순서대로 나열하여 저장하는 자료형
- list, tuple, range, ...
- 특징
  - Sequential : 값이 순서대로 저장.
  - Indexing : index로 값에 접근 가능. temp[2] Python에서는 음수로 접근 가능.
  - Slicing : 범위에 해당하는 값에 접근 가능. temp[2, 4]
  - Length : 길이가 있음.
  - Iteration : _\_iter__ method가 존재. 순회할 수 있음.
### Text Sequence Type, String
- Sequential, Immutable data type(내부의 값을 변경할 수 없음.).
- PEP-8 convention : ""와 '' 아무거나 써도 되는데 코드 내에서 통일 할 것.
- Escape Sequence
  - \n : newline
  - \t : tab
  - \\\ : \
  - \' : ' (PEP-8 convention에서 지양을 명시)
  - \" : " (PEP-8 convention에서 지양을 명시)
- String Interpolation
  - 문자열 내에 변수나 표현식을 삽입하는 방법. f-string.
  - ```python
    f"{num1} {num2} asdfasdf"
    ```
- Immutable 관련 사항
```python
# 아래의 코드에서 "hello" 객체가 바뀌는게 아니라 "hzllo" 객체를 형성하고 test1에서 재할당함.
# String의 immutable에 대한 반례가 아님에 유의.
test1 = "hello"
test1 = "hzllo"
```
### Tuple
### List
### Dict
