t = int(input());
for i in range(t):
  a,b = input().split() 
  # map(int, input().split())이러면 밑에 없어도 된다
  a = int(a)
  b = int(b)
  print(a + b)