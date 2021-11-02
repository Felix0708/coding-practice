num = int(input())

while num != 1:
    for i in range(2, num + 1):
        # 나눠지면 출력하고,
        # 다음을 위해 해당 수로 num을 나눠줍니다.
        if(num % i == 0):
            print(i)
            num = num // i
            break