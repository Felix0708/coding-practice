a = int(input())
b = int(input())
c = int(input())

d = a * b * c
d_list = list(map(int, str(d)))
cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt9 = 0
for i in d_list:
    if i == 0:
        cnt0 += 1
    elif i == 1:
        cnt1 += 1
    elif i == 2:
        cnt2 += 1
    elif i == 3:
        cnt3 += 1
    elif i == 4:
        cnt4 += 1
    elif i == 5:
        cnt5 += 1
    elif i == 6:
        cnt6 += 1
    elif i == 7:
        cnt7 += 1
    elif i == 8:
        cnt8 += 1
    else:
        cnt9 += 1
print(cnt0, cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8, cnt9, sep="\n")