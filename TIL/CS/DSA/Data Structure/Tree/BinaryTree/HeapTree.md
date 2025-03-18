# HeapTree
## 개요
힙 트리는 부모 노드의 값이 자식 노드의 값보다 큰/작은 이진 트리이다.

힙 트리는 우선 순위 큐로 활용된다.

힙 트리가 정렬된 큐에 비해 가지는 강점은 데이터의 삽입과 삭제가 빠르기 때문이다.
$$
Time Complexity = \log{N}
$$
## Heap tree 구현
### 1. heapq 사용
#### 기본적인 힙의 구현
아래 코드를 사용하면 python에서 손쉽게 heapq를 사용할 수 있다.

heapq는 특정 배열을 heap으로 사용할 수 있도록 하는 library이다.

기본적으로 min heap인데, max heap을 사용하기 위해서는 -x를 저장하면 된다.
```python
import heapq


arr = [20, 15, 19, 4, 13, 11]
heapq.heapify(arr)
heapq.heappop(arr)
heapq.heappush(arr, 100)
```
#### 여러 기준을 적용한 힙
아래 코드를 사용하면 여러 기준으로 heap을 만들 수 있다.

이때 tuple의 앞에서 부터 우선 순위가 주어진다.

즉, 아래의 코드는 단어를 길이를 기준으로 heap에 넣되, 길이가 같다면 단어의 사전 순을 기준으로 넣는다.
```python
words = ['apple', 'kiwi', 'banana', 'melon', 'strawberry']
heap = []
for word in words:
    heapq.heappush(heap, (len(word), word))
```
### 2. 직접 구현
```python
from collections import deque


class Heap():
    HEAPSIZE = 10000

    # initialize heap.
    def __init__(self, original_arr, heap_mode='MIN'):
        self.heap = [None] * self.HEAPSIZE
        self.top = 0
        if heap_mode == 'MAX':
            self.cmp = self.is_larger
        elif heap_mode == 'MIN':
            self.cmp = self.is_smaller
        else:
            raise ValueError
        for elem in original_arr:
            self.enqueue(elem)

    def enqueue(self, e):
        self.top += 1
        self.heap[self.top] = e
        cur_node = self.top
        parent_node = cur_node // 2
        while parent_node:
            if self.cmp(self.heap[cur_node], self.heap[parent_node]):
                self.swap(cur_node, parent_node)
            else:
                break
            cur_node = parent_node
            parent_node //= 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def dequeue(self):
        result = self.heap[1]
        self.heap[1] = self.heap[self.top]
        self.heap[self.top] = None
        self.top -= 1
        self.heapfiy()
        return result

    def heapfiy(self):
        cur_node = 1
        while self.heap[cur_node] is not None:
            left_node = 2 * cur_node
            right_node = 2 * cur_node + 1
            # case 1. right node does not exist and left node exist
            # compare left and swap
            if self.heap[right_node] is None and self.heap[left_node] is not None:
                if self.cmp(self.heap[left_node], self.heap[cur_node]):
                    self.swap(left_node, cur_node)
                    cur_node = left_node
                else:
                    break
            # case 2. left and right node does not exist
            elif self.heap[right_node] is None and self.heap[left_node] is None:
                break
            # case 3. left and right nodes exist
            elif self.heap[left_node] is not None and self.heap[right_node] is not None:
                # find max_node
                if self.cmp(self.heap[left_node], self.heap[right_node]):
                    max_node = left_node
                else:
                    max_node = right_node
                # compare max_node and cur_node. then swap
                if self.cmp(self.heap[max_node], self.heap[cur_node]):
                    self.swap(max_node, cur_node)
                    cur_node = max_node
                else:
                    break

    def print_heap(self):
        print(self.heap[:self.top+1])

    @staticmethod
    def is_larger(a, b):
        return a > b

    @staticmethod
    def is_smaller(a, b):
        return a < b
```

