# import sys
# input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    x , y = map(int, input().split())
    arr.append([y, x])

re_arr = sorted(arr)

for y, x in re_arr:
    print(x, y)

# for i in range(N):
#     print(re_arr[i][1], re_arr[i][0])