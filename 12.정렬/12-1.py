N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

for i in range(len(a)-1, 0, -1):
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

for i in a:
    print(i)