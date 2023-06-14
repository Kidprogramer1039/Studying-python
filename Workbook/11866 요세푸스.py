# 리스트 슬라이싱을 잘만 활용하면, 굳이 리스트를 따로 출력하지 않아도 숫자만 따로 뽑아 쓰는게 가능하다.

import sys
from collections import deque

n, k = sys.stdin.readline().split()
result = deque()
arr = deque()

for i in range(1, int(n)+1):
    arr.append(i)

while len(arr) > 0:
    for i in range(int(k)-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

list_str = str(result)[7:-2]
print("<"+list_str+">")
