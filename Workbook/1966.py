#14:40 ~ 17:30

import sys
from collections import deque

rep = int(sys.stdin.readline().rstrip())


for i in range(rep):
    n, m = map(int, sys.stdin.readline().split())
    origin = deque(map(int, sys.stdin.readline().split()))
    x = deque(sorted(origin, reverse=True))
    y = deque([0] * n)
    y[m] = "target"
    pr = 0
    while True:
        if n == 1:
            print(1)
            break
        else:
            if x[0] == origin[0] and y[0] == "target":
                pr += 1
                print(pr)
                break
            elif x[0] == origin[0] and y[0] == 0:
                x.popleft()
                origin.popleft()
                y.popleft()
                pr += 1
                continue
            elif x[0] != origin[0]:
                origin.append(origin.popleft())
                y.append(y.popleft())
                continue

#다른 사람의 풀이
# 출처 : https://www.acmicpc.net/source/52788420
import sys
input = sys.stdin.readline

Q = []
R = []

for _ in range(int(input())):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    QS = sorted(Q, reverse=True)
    T = Q[M]
    Q[M] = -1
    result = 1

    while True:
        if Q[0] == -1 and max(QS) == T:
            R.append(result)
            break
        elif Q[0] == QS[0]:
            QS.pop(0)
            Q.pop(0)
            result += 1
        else:
            tmp = Q.pop(0)
            Q.append(tmp)

for r in R: print(r)
