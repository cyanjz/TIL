# Python 단축 표현 활용
- Pythonic code? : 파이썬스러운 코드 (선언부, 호출부)
- 논리 연산 결과가 확실할 때 나머지 **평가**를 건너뛰는 단축 표현을 사용하자.
```python
# and
# 첫번째 조건이 Falsy면 첫번째 조건을 return
# 첫번째 조건이 Truthy면 두번째 조건을 return
result = False and print(123) # False
result = True and print(123) # None

# or
# 첫번째 조건이 Falsy 두번째 조건을 return
# 첫번째 조건이 Truthy면 첫번째 조건을 return
result = False or print(123) # None
result = True or print(123) # True
```

## 어떻게 활용하는가
### Truthy
- 코드 내에서 `True`로 평가되는 값.
- `Falsy`로 명시되지 않는 대부분의 값.
1. Not empty sequence & collections
2. non zero numbers (int, float, complex)
3. `True`

### Flasy
- 코드 내에서 `False`로 평가되는 값.
1. Empty sequence & collections
    - `[], tuple(), {}, set(), "", ragne(0)`
2. Zero numbers (int, float, complex)
3. `None`, `False`

### 예제
```python
# case 1 - Empty 여부 확인
my_list = [1, 2, 3]
result = my_list and my_list[0] # 1

empty_list = []
result = empty_list and my_list[0] # []

# case 2 - Default 값 지정
name = "" or "Guest"
print(name) # Guest

# case 3 - bool()을 확인한 평가
print(bool([])) # False
```