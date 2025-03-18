# Segment Tree
## 개요
Segment Tree는 배열에서 특정 범위에 해당하는 최댓값/최솟값, 임의의 우선 순위상 앞선 요소를 찾는데 사용.

Segment Tree의 강점은 마찬가지로 데이터의 업데이트 그리고 query의 시간 복잡도가 배열보다 좋기 때문이다.

$$
\text{Tree 형성의 시간 복잡도 : }O(N)
\\
\text{Query의 시간 복잡도 : }O(\log{N})
\\
\text{Update의 시간 복잡도 : }O(\log{N})
$$

## 구현
1. 재귀
재귀적으로 구현하면 아래와 같은 코드를 작성할 수 있다.

함수 설명
- builder 함수는 segment tree를 만들 때 사용된다.
- update 함수는 segment tree의 특정 부분을 update한다.
- query 함수는 segment tree를 사용하여 start ~ end에 해당하는 범위에서 최대/최소 값을 찾는다.
```python
def builder(node, left, right):
    global seg_tree
    if left == right:
        seg_tree[node] = arr[left]
    else:
        mid = (left+right)//2
        builder(2 * node, left, mid)  # left child update
        builder(2 * node+1, mid+1, right)  # right child update
        seg_tree[node] = seg_tree[2*node] + seg_tree[2*node+1]


def update(node, left, right, val, idx):
    global seg_tree
    if left == right:
        seg_tree[node] += val
    else:
        mid = (left+right)//2
        if left <= idx <= mid:
            update(2 * node, left, mid, val, idx)
        else:
            update(2 * node+1, mid+1, right, val, idx)
        seg_tree[node] = seg_tree[2*node] + seg_tree[2*node+1]


def query(node, s, e, left=0, right=6):
    # s, e -> query
    # l, r -> scope
    # query가 scope를 벗어나는 경우.
    if e < left or right < s:
        return 0
    # scope가 querry 내에 있는 경우.
    if s <= left and right <= e:
        return seg_tree[node]
    mid = (left+right)//2
    return query(2*node, s, e, left, mid) + query(2*node+1, s, e, mid+1, right)


arr = [1, 2, 3, 4, 5]
N = len(arr)
seg_tree = [0] * (2 * N)
builder(1, 0, N-1)
update(1, 0, N-1, 100, 1)
print(seg_tree)
update(1, 0, N-1, 100, 4)
print(seg_tree)
```