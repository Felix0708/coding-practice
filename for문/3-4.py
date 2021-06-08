import sys  #내장된 것을 이용해 더 빠르게 출력

t = int(input());
for i in range(t):
  a,b = map(int, sys.stdin.readline().split())  #input 대신에 사용
  print(a + b)