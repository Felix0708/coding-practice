N = int(input())

arr = list(map(int, input().split()))
# print(arr)

re_arr = list(sorted(set(arr)))
# print(re_arr)

arr_dic = {value: index for index, value in enumerate(re_arr)}

# print(arr_dic)

for element in arr:
    print(arr_dic[element], end= " ")