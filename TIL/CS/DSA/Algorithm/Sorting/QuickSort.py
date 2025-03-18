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
    arr[l], arr[i] = arr[i], arr[l]
    # recursive call
    # i는 pivot 보다 작은 가장 오른쪽 요소의 index
    quick_sort2(l, i-1)
    quick_sort2(i+1, r)
    return


arr = [2, 5, 1, 8, 20, 30, 0, 500, 20, 435, 206, 201, 206, 502]
quick_sort2(0, len(arr)-1)
print(arr)
