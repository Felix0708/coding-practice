N = int(input())
arr = []
for tc in range(N):
    word = input()
    arr.append(word)

set_arr = list(set(arr))

sorted_arr = []
for i in set_arr:
    sorted_arr.append((len(i), i))

result = sorted(sorted_arr)

for length, word in result:
    print(word)