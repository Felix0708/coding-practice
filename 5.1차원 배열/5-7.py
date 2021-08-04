n = int(input())
for _ in range(n):
    test_scores = list(map(int, input().split()))
    scores_avg = sum(test_scores[1:]) / test_scores[0]
    cnt = 0
    for i in test_scores[1:]:
        if i > scores_avg:
            cnt += 1
    a = cnt / test_scores[0] * 100
    print( "%0.3f%%" % a)