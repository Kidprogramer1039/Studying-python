import sys
sys.setrecursionlimit(10000000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
  global tmp,maxLen,n,m
  lis[x][y] = -1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0<=nx<n) and (0<=ny<m) and lis[nx][ny] == 1:
      tmp += 1
      DFS(nx,ny)

  


n,m = map(int, input().split())
lis = []
for _ in range(n):
  lis.append(list(map(int, input().split())))
cnt = 0
maxLen = 0
tmp = 1
for i in range(n):
  for j in range(m):
    if lis[i][j] == 1:
      cnt += 1
      DFS(i,j)
      maxLen = max(tmp, maxLen)
      tmp = 1

print(cnt)
print(maxLen)
