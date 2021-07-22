# 고정점 찾기    이진 탐색
'''     이진 탐색 아님 그냥 for문으로 풂
from sys import stdin
n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))
res = -1

for i in range(n):
    if i == array[i]:
        res = i

print(res)
'''
# target을 mid와 연관 시켜야 됨

from sys import stdin
n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

def binary_search(array, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

print(binary_search(array, 0, n-1))
