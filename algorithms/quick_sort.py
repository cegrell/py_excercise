from typing import List

def swap(arr: List[int], i: int, j: int) -> None:
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr: List[int], l: int, r: int) -> None:
    i, p = l-1, arr[r]
    for j in range(l, p):
        if arr[j] < p:
            i += 1
            swap(arr, i, j)
    i += 1
    swap(arr, i, r)
    return i

def qs(arr: List[int], l, r) -> None:
    if l >= r:
        return
    p = partition(arr, l, r)
    qs(arr, l, p - 1)
    qs(arr, p + 1, r)

arr = [5, 1, -2, 6, 8, 10, 2, 4]
qs(arr, 0, len(arr)-1)
print(arr)