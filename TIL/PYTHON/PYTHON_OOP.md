# Procedural Programming - 절차 지향 프로그래밍.
## 특징
- 입력을 받고, 처리/결과를 내는 과정이 위에서 아래로 순차적으로 진행.
- 순차적인 명령어 실행.
- 데이터와 함수의 분리.
- 함수 호출의 흐름이 중요.
## 한계점
- 복잡성 증가 : 데이터/함수/전역 변수의 관리 어려움.
- 유지보수 문제 : 코드 수정 시 영향 범위 파악이 어렵다.

# Object Oriented Programming - 객체 지향 프로그래밍.
데이터와 함수를 하나의 단위로 묶어서 관리. 객체들을 조합, 재활용하는 방식으로 프로그램 구성. 순서보다는 각자의 역할이 중요.
## 특징
- 프로그램을 데이터, 함수를 묶어서 하나의 객체로 조직적으로 관리.
- 데이터와 method의 결합.
- 객체 간 상호작용과 메시지 전달이 중요.
- 데이터가 능동적인 존재가 됨. 코드의 구조화, 재사용성을 높이는 동시에 실제 세계의 모델링 방식과 더 유사한 프로그래밍을 가능하게 한다.
- 세부 요소
  - Attribute : 객체의 상태/데이터.
  - Method : 객체의 행동/기능.
  - 고유성 : 각 객체는 고유한 특성을 지님.
# Class
- 사용자 정의 객체를 만드는 수단, 속성과 method 정의.
- Instance(객체)를 만들기 위한 틀.
- 데이터와 기능을 한데 묶는 방법.
- 파이썬에서 type을 표현하는 방법.
- PascalCase
- class 자체도 하나의 객체.
```python
class MyClass:
    pass
```
## Class 구조
- Method, Variables

# Instance
```python
name = "Alice"
print(type(name))
```
- 변수 name의 타입은 str.
- 즉, 변수 name은 str class의 instance.

# Methods
## Magic method
1. `__init__(self, args)` : 새로운 instance를 형성할 때 필요한 초기 값을 설정.
2. `__str__(self)` : print에 의해 호출되어 객체 출력을 문자열 표현으로 변경.
```python
class MyClass:
    def __str__(self):
        return "str"
test = MyClass()
```
3. `__name__(self)` : object의 이름을 return.
## Method types
### Instance methods(인스턴스가 사용.)
1. instance의 상태를 변경하거나, 해당 instance의 특정 동작을 수행.
2. class 내부에 정의되는 method의 기본.
3. 반드시 첫 인자로 instance 자신 (self)을 받음.
4. instance의 속성에 접근/변경 가능.
```python
'hello'.upper()
# 단축형 호출. instance 스스로 method를 호출하여 코드를 동작하는 OOP 표현.
# 첫번째 인자로 self를 받음.
str.upper('hello')
# 첫 인자로 문자열 instacne를 받음.
# 내부적으로는 str.upper('hello')가 동작.
```
### Class methods (클래스가 사용.)
- Instance의 상태에 의존하지 않는 기능을 정의. class 변수 조작, class 단계의 동작을 수행.
- `@classmethod` decorator를 사용하여 정의.
- 첫 인자는 해당 method를 호출하는 class(cls)를 전달.
```python
class a:
  interest_rate = 0.3
  def __init__(self, balance=1000):
    self.balance = balance
  @classmethod
  def change_rate(cls, rate):
    cls.interest_rate = rate
  @staticmethod
  def is_positive(num):
    return num > 0
    
b = a()
print(b.interest_rate) # 0.3
a.change_rate(0.4)
print(b.interest_rate) # 0.4
```
### Static methods (클래스가 사용.)
- class, instance 상관 없이 독립적으로 동작하는 method.
- `@staticmethod` decorator를 사용하여 정의.
- 호출 시 전달 받는 인자가 없음.
- instance, class 속성에 접근하지 않는 도우미 함수와 비슷한 역할.
```python
class MathUtils:
    @staticemethod
    def add(a, b): # cls, self 인자 없음.
        return a + b

print(MathUtils.add(3, 5)) # 8
```

# Variables
1. Instance variables : `self.var` 형식으로 선언. instance 별로 값이 다름.
2. Class variables : class 내부에 정의.
   1. instance/static method 내부에서는 `class_name.var` 형식으로 접근
   2. class method 내부에서는 `cls.var` 형식으로 접근
3. 접근 순서 : Instance variable -> Class variable

# Objects, Instance in memory
- 각 instance는 독립적인 메모리 공간을 가지며, 클래스와 인스턴스 간에는 서로의 데이터, 상태에 직접적인 접근이 불가능하다.
- OOP의 중요한 특징 중 하나. 클래스와 인스턴스를 모듈화. 각각의 객체가 독립적으로 동작하도록 보장.
- 코드의 가독성, 유지보수성, 재사용성을 높인다.

# Decorator
- 다른 함수의 코드를 유지한 채로 수정, 확장하기 위해 사용되는 함수.
- 연속해서 쓰려면 decorator function을 하나 더 만들고 위에 추가하면 됨.
```python
def decorator_function(func):
    def wrapper(*args, **kargs):
        print('함수 호출')
        result = func(*args, **kargs)
        print('함수 종료')
        return result
    return wrapper

@decorator_function
def add(a, b):
    return a + b

print(add(3, 5))
# 함수 호출
# 함수 종료
# 8
```

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet():
    return "hello"

print(greet()) # HELLO!!!
```

- class에도 적용 가능.
```python
class ClassDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print('decorator called')
        print(f'Excuting {self.func.__name__}')
        return self.func(*args, **kwargs)

@ClassDecorator
def say_hello():
    print("hello")

say_hello()
# decorator called
# Excuting say_hello
# hello
```

- 참조. decorator를 활용하지 않은 구조는 다음과 같이 나타낼 수 있다.
```python
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        return original_function()
    return wrapper_function

def say_hello():
    print("Hello!")

say_hello = decorator_function(say_hello)  # Manually applying the decorator
say_hello()

```