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

## Collection
- 여러 개의 값들을 저장하는 Datatype
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
### List
#### 개요
- Sequential, Mutable data type.
- 0개 이상의 객체를 포함. 데이터의 목록을 저장.
```python
test0 = [] # empty list
test1 = [1, 2, 3]
test2 = ['a', 1, '3']
```
#### Deep/Shallow copy
- List 유의사항 - List에는 객체를 가리키는 주소가 있다.
- 특정 list를 복사하기 위해서는 List 내부의 객체에 변수를 할당해야한다.
```python
a = [[1, 2], [3, 4]]
b = a # not a copy
c = a[:] # shallow copy
d = [row[:] for row in a] # deep copy
```

### Tuple
- Sequential, Immutable data type.
- 단일 요소 튜플을 만들 때는 반드시 후행 쉼표를 사용.
- 내부 동작과 안전한 데이터 전달에 사용.
```python
test0 = (1) # int
test1 = (1,) # tuple
# 내부적으로 tuple이 사용되는 경우
x, y  = 10, 20
x, y = y, x
test2 = (1, 2, 3)
a, b, c = test2 # unpacking
```
### Range
- Sequential, Immutable data type.
- 연속된 정수 sequence를 생성.
- 함수인 동시에 data type
```python
# [start, end)
# step : default = 1
range(start, end, step)
```
## Non-Sequential type
- Indexing 불가!
### Dict
- Non-Sequential, Mutable data type
- Key-Value 쌍으로 이루어진 data type
- Key : Immutable, Value : any datatype
- 100개 이하에서는 list와 차이가 근소하나 크기가 커질수록 list가 유리함.
### Set
- Non-Sequential, Unique data type
```python
set1 | set2 # Union
set1 & set2 # Intersection
set1 - set2 # Substraction
```
- 빈 set를 만들 때는 set()을 사용.

## Other data types
### None
- 값이 없음.
### Boolean
- True, False
- 조건문에서 다룰 예정.

## Type conversion
- 하나의 데이터 타입을 다른 타입으로 바꾸는 것.
### 명시적 형변환
- 프로그래머가 수행하는 형변환. 암시적이 아닌 모든 형변환.
```python
int("1")
int(3.5)
float("3.5")
```
### 암시적 형변환
- Boolean, Numerical type에서 발생하는 형변환
```python
3 + 5.0 # 8.0
True + 3 # 4
True + False # 1
```

## Operator
### 산술 연산자
+, -, * ,**, ...
### 복합 연산자
+=, -=, *=, **=, ...
### 비교 연산자
<, >, <=, >=, ...
- == : 값이 같은 지를 비교. 동등성(Equality)
- is : 객체가 같은지를 비교. 식별성(Identity)
  - 주로 None과 같은 Singleton 객체를 비교할 때 사용.
#### Singleton
- 프로그램 전체에 1개만 존재하도록 만들어진 객체.
- None, True, False.
- Python에서 작은 숫자들의 경우 memory 주소를 하나로 고정.
  - Python 범위 및 메모리 상황마다 다를 수 있음.
### 논리 연산자
- and, or, not
- 단축 평가
```python
3 and 4 # 4
0 and 4 # 0
2 or 1 # 2
0 or 1 # 1
```
### Membership operator
- in, not in
### Sequence operator
```python
a, b = [1, 2, 3], [4, 5, 6]
a + b = c # c = [1, 2, 3, 4, 5, 6]
a * 2 = d # d = [1, 2, 3, 1, 2, 3]
```
## 참조
### Trailing comma
- Collection의 마지막에 붙는 comma.
```python
a = (1, )
b = {1, }
```