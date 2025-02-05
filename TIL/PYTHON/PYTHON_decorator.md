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