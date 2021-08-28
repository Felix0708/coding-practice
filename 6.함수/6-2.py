def d(n):
    next_num = n
    for value in list(str(n)):
        next_num += int(value)
    return next_num

number = []
for value in range(1, 10001):
    number.append(d(value))

numbers = set(number)

for value in range(1, 10001):
    if value in numbers:
        continue
    else:
        print(value)

# n = list(range(1, 10001))
# num_list = []
# for i in n:
#     for j in str(i):
#         i += int(j)
#     if i <= 10000:
#         num_list.append(i)

# numbers = []
# for i in n:
#     if i not in set(num_list):
#         numbers.append(i)
# for i in numbers:
#     print(i)
