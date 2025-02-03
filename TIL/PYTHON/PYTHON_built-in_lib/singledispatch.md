# singledispatch
## Function
```python
from functools import singledispatch

@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported type")

@add.register
def _(a: int, b: int) -> int:
    return a + b

@add.register
def _(a: str, b: str) -> str:
    return a + " " + b

@add.register
def _(a: list, b: list) -> list:
    return a + b

# 테스트
print(add(1, 2))         # 3 (int + int)
print(add("Hello", "World"))  # "Hello World" (str + str)
print(add([1, 2], [3, 4]))    # [1, 2, 3, 4] (list + list)
```
## Class method
```python
from functools import singledispatchmethod

class Calculator:
    @singledispatchmethod
    def multiply(self, a, b):
        raise NotImplementedError("Unsupported type")

    @multiply.register
    def _(self, a: int, b: int) -> int:
        return a * b

    @multiply.register
    def _(self, a: str, b: int) -> str:
        return a * b  # 문자열 반복

calc = Calculator()
print(calc.multiply(3, 4))   # 12
print(calc.multiply("Hi", 3)) # "HiHiHi"
```