def d(n):
    cnt = 0
    n_list = []
    for i in range(1, n+1):
        n_list = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            cnt += 1
    return cnt

num = int(input())
print(d(num))