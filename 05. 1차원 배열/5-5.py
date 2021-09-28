# test_len = int(input())
# arr = []
# for numbers in range(test_len):
#     n = int(input())
#     arr.append(n)
# max_arr = max(arr)

# re_arr = []
# for i in arr:
#     re_arr.append((i / max_arr) * 100)
# test_avg = sum(re_arr) / test_len
# print(test_avg)
# -----------------
n = int(input())
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for score in test_list :
    new_list.append(score/max_score *100)
test_avg = sum(new_list)/n
print(test_avg)