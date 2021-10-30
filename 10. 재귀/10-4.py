A, B, V = map(int, input().split())
# A는 낮에 올라갈 수 있는 길이
# B는 밤에 미끄러지는 길이
# V는 나무의 높이

days = 0
# 하루에 A- B
# 목표지점 도달 시, 미끄러지지 않음. V - B
# V - B에서 A - B를 나눌 때, 나머지가 0이 아니라면
# 하루가 더 필요하므로 몫에 1을 더해주고
# 나머지가 0이라면 몫을 출력해준다.
if (V - B) % (A - B) != 0:
    days = ((V - B) // (A - B)) + 1
else:
    days = ((V - B) // (A - B))

print(days)