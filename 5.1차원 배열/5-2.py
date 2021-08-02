# a = list(map(int,input().split()))
# cnt = 1
# max_num = a[0]
# for i in a[1:]:
#     if i > max_num:
#         max_num = i
#         cnt += 1
# print(max_num, cnt)

num_list = []
for numbers in range(9):
    num_list.append(int(input()))
max_num = num_list[0]
for i in num_list[1:]:
    if i > max_num:
        max_num = i
print(max_num, num_list.index(max_num) + 1, sep="\n")