import sys
# 12:20~ 12:51
def dfs(x,y, max):
  # dfs의 범위를 벗어나지 않는지 체크
  if x>=0 and x<num and y>=0 and y<=large:
    over = False
  else:
    over = True
  # 벗어나지 않을 경우
  if (not over):

  



input = sys.stdin.readline

num, large = map(int, input().split())
lis = []
for _ in range(num):
  tmp = list(map(int, input().split()))
  lis.append(tmp)

visited = [[False]*large for _ in range(num)]

res = dfs(0,0,0)
