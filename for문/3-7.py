t = int(input());
for i in range(1, t+1):
  a,b = map(int, input().split())
  print("Case #"+str(i)+":" , a + b)
  #i는 정수형이지만 문자형과 같이 붙여서 쓰기 위해 같은 자료형인 str(i) 로 바꿈
  