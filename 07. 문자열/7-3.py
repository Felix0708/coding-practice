alpha = [
    'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h',  
    'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p',
    'q', 'r', 's', 't',
    'u', 'v', 'w', 'x',
    'y', 'z'    
    ]

n = input()
ans = []

for i in range(len(alpha)):
    if alpha[i] in n:
        for j in range(0, len(n)):
            if alpha[i] == n[j]:
                if alpha[i] in ans:
                    pass
                else:
                    ans.append(alpha[i])
                    print(j, end=' ')
    else:
        print(-1, end=' ')
