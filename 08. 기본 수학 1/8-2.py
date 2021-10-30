n = int(input())
cnt = 1
cnt_six = 6
idx = 1

while n > cnt:
    idx += 1
    cnt += cnt_six
    cnt_six += 6
print(idx)