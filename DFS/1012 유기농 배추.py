import sys
#10:40 ~ 11:10
sys.setrecursionlimit(10000000)

input = sys.stdin.readline
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def DFS(x,y):
  global M,N
  lis[y][x] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<M and 0<=ny<N and lis[ny][nx] == 1:
      DFS(nx, ny)



rep = int(input())
res = []
for _ in range(rep):
  M,N,K = map(int, input().split())

  if K == 1: #K가 1일 경우 반환
    A,B = map(int, input().split())
    print(1)
    continue

  lis = [[0] * M for _ in range(N)]
  dic = dict() #숫자를 일일히 돌지 않고 딕셔너리에 있는 것만 처리
  cnt = 0

  for _ in range(K):
    A,B = map(int, input().split())
    dic[A] = B
    lis[B][A] = 1

  for key in dic:

    if lis[int(dic[key])][int(key)] == 1:
      cnt += 1
      DFS(int(key), int(dic[key]))

  print(cnt)    


