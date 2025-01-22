# Python Function
여기서는 Python의 Function을 다룹니다.
## 개요
- Function 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음.
    - 코드의 중복 방지
    - 재사용성이 높아지고, 코드의 가독성과 유지보수성 향상.
- 함수의 구조
```python
def get_sum(num1, num2):
    # Docstrint
    '''
    Docstring
    '''
    # Body
    sum_result = num1 + num2
    # Return
    return sum_result
```
    - Return이 명시되지 않아도 None을 return.
    - num1, num2 : parameter.
- Typing : python에서 type을 명시하는 방법.
```python
def test(pram1 : int) -> int:
    return parm1**2
```
## 매개변수와 인자
- 매개변수, parameters : 함수를 정의할 때 함수가 받을 값을 나타내는 변수.
- 인자, arguments : 함수를 호출할 때 실제로 전달되는 값.
### 인자의 종류
1. Postional Arguments
    - 함수 호출 시 인자의 위치에 따라 전달되는 인자.
    - 위치 인자는 함수 호출 시 반드시 값을 전달해야함.
2. Default Arguments
    - 매개변수에 default 값을 할당하는 것.
    - 호출 시 인자를 할당하지 않으면 기본값이 매개변수에 할당 됨.
3. Keyword Arguments
    - 함수 호출 시 이름과 함께 값을 전달하는 인자.
    - 인자의 호출 순서는 중요하지 않음.
    - 호출 시 Keyword arguments는 Positional arguments 뒤에 와야함.
4. Arbitrary Argument Lists
    - 정해지지 않은 개수의 인자를 처리.
    - `*args`
    - 내부적으로 `tuple`을 호출.
5. Arbitrary Keyword Argument Lists
    - 정해지지 않은 개수의 Keyword argument를 처리.
    - `**kargs`
    - 내부적으로 `dict`를 호출.
- Style guide : 
Positional - Default - Arbitrary - Arbitrary Keyword 순으로 작성.
## 재귀 함수
- 함수 내부에서 자기 자신을 호출하는 함수.
```python
# 기본 구조
def recurse(*params1):
    if break_condition:
        return something
    else:
        return recurse(*params2)

# Factorial
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
```
- 함수를 호출하면 Call stack에 함수가 들어간다.
- Call stack에 계속 쌓다가 위에서부터 return을 시작한다.
- 변수 사용이 줄어들고 가독성이 올라간다.
- 반드시 base case(종료되는 상황)가 1개 이상 있을 것.

## 내장 함수
- Python이 기본적으로 제공하는 함수.
- 별도의 Import 필요 없음.
```python
print, map, zip, len, max, min, sum, sorted, ...
```
[Python built-ins](https://docs.python.org/3/library/functions.html)

## 함수와 Scope
- 좁은 scope에 없으면 넓은 scope에서 찾아본다.
### Scope & Variables
1. Global and local
- Global Scope/variables : 코드 어디에서든 참조 가능.
- Local Scope/variables : 함수 내에서만 참조 가능.
2. Life cycle of Variables
- Built-in scope : 파이썬 실행 이후 계속 유지
- Global scope : 모듈의 호출, 인터프리터 끝날 때 까지 유지
- Local scope : 함수의 호출 ~ 종료까지 유지
### Name Resolution
- LEGB Rule : Local -> Enclosed -> Global -> Built-in
- 변수를 찾아가는 규칙.
- 역순은 불가능. 애초에 함수의 호출이 끝나면 local scope는 없어지므로.
```python
# global
a = 1
def test1():
    # enclosed
    b = 2
    def test2():
        # local
        c = 3
        # enclosed scope의 b를 재할당 하는게 아니라 local variable b에 2를 할당하는 것.
        b = 4
```
#### 번외
- List는 참조하여 변경이 가능.
- 사실 이는 Local에서 참조한 a list 자체에 method가 있기 때문임.
- dir(a)의 method 모두 사용 가능.
- int, str 같은 변수들도 method는 사용할 수 있다.
- 다른 것들도 Wrapper class 만들면 뭔가 가능하나?
```python
a = [1, 2, 3]
def test():
    a[0] = 100
test()
print(a) # [100, 2, 3]
```
## Style Guide
- snake_case
- 동사로 시작, 약어 지양.
```python
# 동사 + 명사
save_user()
# 동사 + 형용사 + 명사
calculate_total_price()
# get, set
get_user_name(), set_user_name()
```

## Packing/Unpacking
- Packing
```python
#  Tuple로 Packing을 수행
packed = 1, 2, 3, 4, 5
print(packed) # (1, 2, 3, 4, 5)

# `*변수명`을 사용하면 모든 값을 list로 묶어서 전달.
a, *b, c = [1, 2, 3, 4, 5]

# Tuple로 인자를 전달
def my_func(*args):
    print(args)
    print(type(args))

my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# Tuple
```
- Unpacking
```python
# case 1
test = 1, 2, 3, 4, 5
a, b, c, d, e = test

# case 2
def my_funcion(x, y, z):
    print(x, y, z)

names = [1, 2, 3]
my_function(*names)

# case 3
my_dict = {'x' : 1, 'y' : 2, 'z' : 3}
my_function(**my_dict)
```

## Labmda Function - 익명 함수
```python
# lambda params : expression
addition = lambda x, y : x + y
# 인자로 쓰일 때, 일회성일 때 많이 쓰인다.
numbers = [1, 2,, 3, 4, 5]
squares = list(map(lambda x : x**2, numbers))
```