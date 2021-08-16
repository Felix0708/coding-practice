def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solve(a))