# 부품 찾기
from sys import stdin
n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))

count = [0] * m             # [0, 0, 0]  -> 5, 7, 9

for i in range(n):
    for j in range(m):
        if lst[j] == array[i]:
            count[j] += 1


for i in range(m):
    if count[i] == 0:
        print("no", end=' ')
    else:
        print("yes", end=' ')
