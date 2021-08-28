text = input()
result =0
i=0
while len(text)-2>=i: 
    # 문자열 리스트 길이를 넘는 것을 방지하기 위해 -1을 해야겠지만
    # 이 경우를 보면 i+1의 값을 비교해볼때가 있기 때문에 
    # 1회 더 줄여서 -2를 해줍니다.
    # 마지막 문자는 검사를 안하느냐 걱정될 수 있습니다. 
    if text[i]=='c' and (text[i+1]=='-' or text[i+1]=='='):
        result +=1
        i +=1 
    # 크로아티아 문자열이 된 길이만큼 반복문의 핵심인 i값을 증가시켜 
    # 일반 알파벳으로 인식되는 것을 회피합니다.
    # 문자열 길이를 넘는 것을 방지하기 위해 'dz='의 경우는 
    # i의 여유를 1개 더 가진 상태일때 확인합니다.
    elif text[i]=='d' and (text[i+1]=='-' or (text[i+1]=='z' and len(text)-3>=i and text[i+2]=='=')):
        if text[i+1]=='z':
            result += 1
            i += 2
        else:
            result += 1
            i += 1
    elif text[i]=='l' and text[i+1]=='j':
        result += 1
        i += 1
    elif text[i]=='n' and text[i+1]=='j':
        result += 1
        i += 1
    elif text[i]=='s' and text[i+1]=='=':
        result += 1
        i += 1
    elif text[i]=='z' and text[i+1]=='=':
        result += 1
        i += 1
    else:
        result += 1
    i +=1 
    # for문이 아니기 때문에 기본적인 i값을 항상 증가시켜줍니다.

# 만약 i값이 문자열길이-1과 값이 같다면, 
# 마지막 값이 크로아티아 문자가 아닌 경우이기 때문에 세어지지 않았습니다.
if len(text)-1 == i:
    result +=1 # 결과값을 1 증가시켜줍니다.

print(result)