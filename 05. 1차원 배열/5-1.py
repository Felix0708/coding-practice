a = int(input())
b = list(map(int, input().split()))
max_num = b[0]
min_num = b[0]
for i in b[1:]:
    if max_num < i:
        max_num = i
    elif min_num > i:
        min_num = i
print(min_num, max_num)