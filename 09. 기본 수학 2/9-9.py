while True:
    a, b, c = map(int, input().split())
    
    if a == b == c == 0:
        break
    
    temp = [a, b, c]
    temp.sort()
    
    if temp[0]**2 + temp[1]**2 == temp[2]**2:
        print('right')
    else:
        print('wrong')