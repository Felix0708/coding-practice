N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    error = 0
    if num > 1 :
        for i in range(2, num):  
            # 2부터 n-1까지
            if num % i == 0:
                error += 1  
                # 2부터 n-1까지 나눈 나머지가 0이면 error가 증가
        if error == 0:
            cnt += 1  
            # error가 없으면 소수.
print(cnt)