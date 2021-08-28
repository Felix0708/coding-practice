text = input().upper()

text_arr = []
for i in text:
    if i in text_arr:
        pass
    else:
        text_arr.append(i)
stack = []
for k, v in enumerate(text_arr):
    stack.append([k, v, 0])

for i in range(len(text)):
    for j in range(len(stack)):
        if text[i] == stack[j][1]:
            stack[j][2] += 1

max_arr = 0
for i in range(len(stack)):
    if max_arr < stack[i][2]:
        max_arr = stack[i][2]

cnt = 0
for i in range(len(stack)):
    if stack[i][2] == max_arr:
        cnt += 1

if cnt >= 2:    
    print('?')
else:
    for i in range(len(stack)):
        if stack[i][2] == max_arr:
            print(stack[i][1])
