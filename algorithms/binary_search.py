from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [-1, 4, 5, 8, 10, 12, 14, 15, 22]
target = 13
print(binary_search(arr, target))
