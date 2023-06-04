import sys
from collections import deque

rep = int(sys.stdin.readline())
for _ in range(rep):
    com = sys.stdin.readline().rstrip() #명령 입력받기
    x = int(sys.stdin.readline()) #배열 크기 입력(파이썬에서는 의미 없음)
    arr = sys.stdin.readline().strip('[]\n').split(',') #배열을 str로 입력받은 후, 앞뒤 괄호 제거 및 줄바꿈 문자 제거
    arr = deque(arr) #쉼표를 기준삼아서 덱으로 재분류

    
"""   
위 코드를 보면 알 수 있듯, int문 같은 숫자는 sys 라이브러리를 쓸 때 따로 형변환을 해주면 개행문자를 없앨 수 있어서 편리하지만, str문, 혹은 리스트를 써야 하는 경우에는
형변환을 하지 말고 strip 함수를 사용하면 더 편하게 작업할 수 있다.
"""
