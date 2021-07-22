# 부품 찾기
from sys import stdin
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))
array.sort()
m = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))

for target in lst:
    if binary_search(array, target, 0, n-1) == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')
