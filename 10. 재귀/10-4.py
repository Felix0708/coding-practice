def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)

    else:
        hanoi(n - 1, start, end, mid)
        print(start, end)
        hanoi(n - 1, mid, start, end)
        
n = int(input())
total = 1
for i in range(n - 1):
    total = total * 2 + 1
print(total)
hanoi(n, 1, 2, 3)