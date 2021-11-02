M = int(input())
N = int(input())
# M > N

arr = []
for i in range(M, N + 1):
    error = 0
    if i > 1 :
        for j in range(2, i):  
            # 2부터 n-1까지
            if i % j == 0:
                error += 1  
                # 2부터 n-1까지 나눈 나머지가 0이면 error가 증가
        if error == 0:
            arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))