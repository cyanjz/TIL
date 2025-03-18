# Quick Sort
## 개요
정렬 알고리즘의 일종.

$$
\text{Time Complexity} = O(N\log{N})
$$

## 알고리즘
퀵 정렬의 핵심 알고리즘은 특정 값보다 작은 값들을 해당 값의 왼쪽에, 큰 값들을 해당 값의 오른쪽에 존재하도록 하는 partition이다.

partition을 수행하는 방식에는 크게 두 가지 방법이 있다.
### 코드 1
왼쪽에서 출발하는 i와 오른쪽에서 출발하는 j를 사용한다.

왼쪽에서 오는 i의 경우에는 pivot보다 큰 값이 나오면 멈추고

오른쪽에서 오는 j의 경우에는 pivot보다 작은 값이 나오면 멈춘다.

#### 경계값 탐사
이때 i == j가 되었을 때...

arr[i]가 pivot보다 크다면 j가 1 감소하고

arr[i]가 pivot보다 작거나 같으면 i가 1 증가한다.

따라서 j가 pivot보다 작으면서 가장 오른쪽에 있는 요소의 index이다.

partition이 끝나면 pivot보다 작으면서 가장 오른쪽에 있는 요소의 index와 left를 swap한다.

```python
def quick_sort1(l, r):
    global arr
    # end condition
    if l >= r:
        return
    # initialize variables
    pivot = arr[l]
    i = l
    j = r
    # partition
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    # recursive call
    quick_sort1(l, j-1)
    quick_sort1(j+1, r)
    return
```


### 코드 2
배열의 특정 구간을 순회하면서 pivot보다 작거나 같은 수를 찾으면 왼쪽과 바꾼다.

이때 바꿔야 할 왼쪽의 index는 stack의 top과 유사하게 관리한다.

즉, pivot보다 작은 값이 발견되어 swap을 수행하면 i는 1 증가하여 pivot보다 작으면서 가장 오른쪽에 있는 요소의 index와 같아진다.
```python
def quick_sort2(l, r):
    global arr
    # end condition
    if l >= r:
        return
    # initialize variables
    pivot = arr[l]
    i = l - 1
    # partition
    for j in range(l, r+1):                         # 하나씩 순회 하면서
        if arr[j] <= pivot:                         # pivot 보다 작거나 같은 값을 찾으면
            i += 1
            arr[i], arr[j] = arr[j], arr[i]         # 왼쪽의 끝과 바꿔주기
    arr[l], arr[i] = arr[i], arr[l]                 # i는 pivot 보다 작은 가장 오른쪽 요소의 index
    # recursive call
    quick_sort2(l, i-1)
    quick_sort2(i+1, r)
    return
```