import sys 

n = int(input()) 
arr = [] 
diction = {} 
for _ in range(n): 
    i = int(sys.stdin.readline()) 
    arr.append(i) 
    if i in diction: 
        # 최빈값 계산을 위해 딕셔너리에 담기 
        diction[i] += 1 
    else: 
        diction[i] = 1 

# 산술평균 
print(round(sum(arr)/n)) 

# 중앙값 
arr.sort() 
i = int(len(arr)//2) 
print(arr[i]) 

# 최빈값 
maxNum = 0 
arr2 = [] 
for key, val in diction.items(): 
    if val > maxNum: 
        arr2.clear() 
        arr2.append(key) 
        maxNum = val 
    elif val == maxNum: 
        arr2.append(key) 
        maxNum = val 
arr2.sort() 
# 최빈값이 여러 개 있을 경우, 
# 최빈값 중 두 번째로 작은 값 출력을 위해 정렬 

print(arr2[0]) if len(arr2) == 1 else print(arr2[1])

# 범위 
print(arr[len(arr)-1] - arr[0])

