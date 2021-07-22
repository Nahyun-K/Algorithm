# 떡볶이 떡 만들기
from sys import stdin
def binary_search(lst, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, start, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, end)
    
n, m = map(int, stdin.readline().split())       # 떡의 개수 N 떡의 길이 M
array = list(map(int, stdin.readline().split()))
max_value = max(array)
lst = []
for i in range(max_value):
    sum = 0
    for j in range(n):
        cnt = array[j] - i
        if cnt < 0:
            cnt = 0
        sum += cnt
    lst.append(sum)

lst.sort()
res = binary_search(lst, m, 0, len(lst) - 1)

for i in range(max_value):
    if i == max_value - (res + 1):
        print(i)
