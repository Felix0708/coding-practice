T = int(input())
for tc in range(T):
    R, S = input().split()
    text = ''
    for i in S:
        text += int(R) * i
    print(text)