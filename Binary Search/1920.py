# 11:59 ~ 12:20

def double_search(start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if lis[mid] == target:
      return 1
    else:
      if lis[mid] > target:
        end = mid-1
      elif lis[mid] < target:
        start = mid+1
  return 0



a = int(input())
lis = list(map(int, input().split()))
tarNum = int(input())
tarLis = list(map(int, input().split()))
lis.sort()
for i in tarLis:
  res = double_search(0, len(lis)-1, i)
  print(res)
