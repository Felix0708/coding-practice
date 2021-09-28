n = int(input())
for _ in range(n):
    test_list = input()
    total = 0
    curr = 0
    for i in range(len(test_list)):
        if test_list[i] == 'O':
            curr += 1
            total += curr
        else:
            curr = 0
    print(total)