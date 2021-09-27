A, B = map(str, input().split())

A_str = ''
for i in range(2, -1, -1):
    A_str += A[i]

B_str = ''
for j in range(2, -1, -1):
    B_str += B[j]

if int(A_str) > int(B_str):
    print(A_str)
else:
    print(B_str)