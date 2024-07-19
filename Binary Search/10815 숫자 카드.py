# 11:28 ~ 11:39
def binary_search(x, start, end, lis):
  while start <= end:
    mid = (start + end) //2
    if lis[mid] == x:
      return 1
    else:
      if lis[mid] > x:
        end = mid-1
      elif lis[mid] < x:
        start = mid+1
  return 0






n = int(input())
haveList = list(map(int, input().split()))
m = int(input())
findList = list(map(int, input().split()))

haveList.sort()

for i in findList:
  res = binary_search(i,0, n-1, haveList)
  print(res)
