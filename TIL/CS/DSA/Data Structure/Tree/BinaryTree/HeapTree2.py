import heapq


arr = [20, 15, 19, 4, 13, 11]
heapq.heapify(arr)
heapq.heappop(arr)
heapq.heappush(arr, 100)


words = ['apple', 'kiwi', 'banana', 'melon', 'strawberry']
heap = []
for word in words:
    heapq.heappush(heap, (len(word), word))
