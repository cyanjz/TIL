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

<br/><br/>

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

<br/><br/>

# Instance
```python
name = "Alice"
print(type(name))
```
- 변수 name의 타입은 str.
- 즉, 변수 name은 str class의 instance.

<br/><br/>

# Methods
## Magic methods
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
- class, instance 양쪽에도 영향을 주지 않아야 한다. 즉 연관성을 보고 class에 넣어야 하는지 생각하지.
- class, instance 상관 없이 독립적으로 동작하는 method.
- `@staticmethod` decorator를 사용하여 정의.
- 호출 시 전달 받는 인자가 없음.
- instance, class 속성에 접근하지 않는 도우미 함수와 비슷한 역할.
  - 상태 확인
  - 유효성 검사
```python
class MathUtils:
    @staticemethod
    def add(a, b): # cls, self 인자 없음.
        return a + b

print(MathUtils.add(3, 5)) # 8
```

<br/><br/>

# Variables
1. Instance variables : `self.var` 형식으로 선언. instance 별로 값이 다름.
2. Class variables : class 내부에 정의.
   1. instance/static method 내부에서는 `class_name.var` 형식으로 접근
   2. class method 내부에서는 `cls.var` 형식으로 접근
3. 접근 순서 : Instance variable -> Class variable
```python
class A:
  class_var = 1
  def __init__(self, a, b):
    self.instance_var1 = a
    self.instance_var2 = b
```

<br/><br/>

# Objects, Instance in memory
- 각 instance는 독립적인 메모리 공간을 가지며, 클래스와 인스턴스 간에는 서로의 데이터, 상태에 직접적인 접근이 불가능하다.
- OOP의 중요한 특징 중 하나. 클래스와 인스턴스를 모듈화. 각각의 객체가 독립적으로 동작하도록 보장.
- 코드의 가독성, 유지보수성, 재사용성을 높인다.

<br/><br/>

# Class Inheritance
- 무작정 상속을 진행하지 말고 여러 class에 일단 싹다 넣어보고, 재활용 가능한지 여부를 나중에 판단, 상속.
- class를 다 작성하고 나서 상속을 진행하기!
```python
class A: pass
class B(A) : pass
```
## 개요
- 특정 class의 method, class variable을 다른 class (sub-class, child class)에서 사용할 수 있도록 하는 기능.
- 부모 class의 코드를 재사용하므로 기존 클래스의 수정 없이 확장을 이룰 수 있다.
- 계층 구조 : 상속을 통해 계층 구조를 만들면 좀 더 구조적인 형식의 코딩을 할 수 있다.
- 유지 보수성 : 부모 class의 method, class variable를 수정하여 child class의 method도 한번에 수정할 수 있다.

## Method overriding
- SubClass에서 Parent Class의 method를 재정의하는 것.
- 기존 클래스를 변경하지 않으면서 method를 확장하는 방법.
```python
class A:
  def test(self):
    print('a')

class B(A):
  def test(self):
    print('b')

b = B()
b.test() # b
```

## Method referencing and MRO
- Python에서 method를 찾아가는 방식은 MRO(Method Resolution Order)를 따른다.
- SubClass.mro()를 사용하면 list 형식으로 확인할 수 있다.
- 단일 상속의 경우에는 parent가 하나이기에 충돌이 발생할 염려가 없으나, 다중 상속의 경우에는 충돌이 발생할 수 있으므로, python의 내장 알고리즘을 통한 MRO가 존재한다.
- class가 여러번 액세스 되지 않도록 우선 순위에 영향을 주지 않으면서 sub class를 만드는 단조적인 구조 형성.
```python
class A:
  def test():
    print('a')

class B(A):
  def test():
    print('b')

class C(A):
  def test():
    print('c')

class D(B, C):
  def test():
    print('d')

print(D.mro()) #[D B C A object]
```
- DFS, left 2 right, C3 linearlization등등이 복합적으로 사용된다.
- 아래의 예제를 참조.
```python
class A: pass

class B(A): pass

class C(B): pass

class D(A): pass

class E(C, D): pass

print(E.mro()) #[E, C, B, D, A, object]
```

## super()
- 다중 상속에서 MRO를 따르기 때문에 부모 class의 method를 호출해야 할 때 사용하는 함수.
- class를 직접 호출할 수도 있으나, super()를 사용하면 더 명확하게 코드를 작성할 수 있다.
- 또한, super()를 연속해서 사용하면 mro 걱정 없이 최상단의 class method를 참조할 수 있다.
  - 단, 중간의 class에서 super() 외에 뭔가를 해서는 안됨.
- 일관된 super 사용.
```python
class A:
  def __init__(self, a, b):
    self.a = a
    self.b = b


class B(A):
  def __init__(self, c):
    A.__init__(self, 100, 200)
    # super().__init__(100, 200)
    self.c = c

b = B(4)
print(b.a)
```

# Error and Exception
```python
try:
	code_which_might_raise_error
except:
	code_to_run_when_error_raised
else:
	code_to_run_when_error_isnot_raised
finally:
	code_to_run_evertime
```
## 개요
- 예외를 처리하는 방식. try의 code를 실행하고 error가 발생하면 except 구문으로 넘어간다.
- built in errors
```python
ZeroDivisionError
NameError
TypeError # 타입 불일치, 인자 누락/초과/타입 불일치
ValueError # 연산이나 함수에 문제가 없으나 부적절한 값을 인자로 받았음.
IndexError
KeyError
ModuleNotFoundError
ImportError
KeyboardInterrupt
IndentationError
```
## 상속에 유의
- exception 발생 시 상속 구조에 유의
```python
try:
	num = int(input())
	print(100/num)
except BaseException: # 최상위 class
	print('제대로 입력하세요.')
except ZeroDivisionError: # 하위 class. 따라서 아래의 블록은 실행이 불가능.
	print('0으로 나눌 수 없습니다.')
```
## as keyword
```python
my_list = []
try:
  number = my_list[1]
except IndexError as error:
  print(f'{error}가 발생했습니다!') # list index out of range가 발생했습니다!
```

# EAFP & LBYL
## EAFP : Easier to Ask for Forgiveness than Permission
- 일단 실행하고 예외를 처리.
- 코드에서 예외가 발생하는 부분을 미리 예측해서 대비하는게 아니라, 예외가 발생한 후에 예외를 처리
- 예외 사항을 예측하기 어려운 경우에 발생.


## LBYL : Look Before You Leap
- 실행하기 전 조건을 검사, 예외 상황을 회피.
- 좀 더 예측 가능한 동작을 하지만, 더 길고 복잡해질 수 있다.
- 예외 상황을 미리 방지하고 싶을 때 유용.