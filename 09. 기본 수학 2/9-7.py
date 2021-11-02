x, y, w, h = map(int, input().split())
# 한수(x, y) 
# 오른쪽 위(w, h)

print(min(x, y, w-x, h-y))
