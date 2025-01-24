# PYTHON control flow
- 코드의 실행 흐름을 제어하는데 사용되는 구문.
- 조건에 따라 코드 블럭을 실행/반복하는 것.

## 조건문 if
- 주어진 condition을 평가, `Truthy` 인 경우 실행. `Falsy` 인 경우 스킵.
```python
if condition1:
    do_something
elif condition2:
    do_something
else:
    do_something
```
- 조건문은 순차적으로 진행됨.

## 반복문
### for
- iterable은 복수로, elem은 단수로 표현.
- 횟수가 명확한 경우에 사용
```python
for elem in iterable:
    do_something
```
### while
- 조건식이 참인 동안 코드를 반복해서 실행.
  - 적절한 종료 (수렴) 조건을 작성할 것.
- 횟수가 불명확하거나 조건에 따라 반복을 종료해야 하는 경우.
```python
while condition:
    do_something
```

### Control loops
1. break
   1. 현재의 loop를 종료
   ```python
   for i in range(10):
        if not i%5:
            break
   ```
2. continue
   1. 현재의 loop 단계를 skip
   ```python
   # 5는 출력되지 않는다.
   for i in range(10):
        if not i%5:
            continue
        print(i)
   ```
3. pass
   1. 아무것도 하지 않고 넘어감.
   2. 코드의 미완성 부분.
   3. 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행.
   ```python
   for i in range(10):
        pass
   ```

### List 생성
1. List comprehenstion
- 간결하고 효율적인 리스트 생성 방법.
- 조건을 넣거나, 중첩 for 문을 사용하는 등 다양한 패턴을 구현하기에도 용이.
- 단, 가독성을 해치지 않는 선에서 사용.
- Pythonic한 방식으로 간결한 코드 작성 가능.
- 대부분의 경우 속도가 가장 빠르다.
```python
[expression for var in iterable]
[expression for var in iterable if condition]
[expression if condition else statement for var in iterable]

list(expression for var in iterable)
list(expression for var in iterable if condition)
list(expression if condition else statement for var in iterable)
```

2. for loop
- 직관적으로 이해하기 쉽고, 복잡한 로직(continue, break)가 필요한 경우 용이.
- 여러 변수를 업데이트하기 좋다.
```python
a = []
for i in range(4):
    a.append(i)
```
3. map
- 함수형 프로그래밍 스타일을 선호하거나, 이미 정의된 함수를 적용해야 할 때 유용.
- 이미 존재하는 함수에 값을 여러번 적용해야 할 때 유리하다.
- 복잡한 로직은 map 내부에서 처리하기 난해하므로... 읽기 어려워질 수 있다.

#### 결론
- **성능 차이는 대부분의 경우 미미하므로 가독성과 유지 보수성이 더 중요하다.**