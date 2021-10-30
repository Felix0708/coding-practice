T = int(input())
for tc in range(1, T + 1):
    x, y = map(int, input().split())
    # x는 현재 위치, y는 목표 위치
    distance = y - x # 거리
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  
        # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)