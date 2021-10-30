t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')

# T = int(input())
# for tc in range(1, T + 1):
#     H, W, N = map(int, input().split())
#     # H는 층 수, W는 각 층의 방 수, N은 몇 번째 손님

#     hotel = H * W
#     hotel_maps = [['0'] * W for _ in range(H)]
#     visited = [['0'] * W for _ in range(H)]

#     i = H
#     for row in range(H):
#         for col in range(W):
#             if col < 10:
#                 hotel_maps[row][col] = str(i - row) + '0' + str(col + 1)
#             else:
#                 hotel_maps[row][col] = str(i - row) + str(col + 1)
    
#     cnt = 0
#     for y in range(W):
#         for x in range(H-1, -1, -1):
#             visited[x][y] = 1
#             cnt += 1
#             if cnt == N:
#                 break
#         if cnt == N:
#             print(hotel_maps[x][y])
#             break