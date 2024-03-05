from itertools import permutations

balls = list(permutations(['1','2','3','4','5','6','7','8','9'], 3))

n = int(input())
for i in range(n):
    q, s, b = (map(int, input().split()))
    q = list(str(q))
    rc = 0

    for j in range(len(balls)):
        sc = 0
        bc = 0

        j -= rc

        for k in range(3):
            if q[k] == balls[j][k]:
                sc += 1
            elif q[k] in balls[j]:
                bc += 1
        if sc != s or bc != b:
            balls.remove(balls[j])
            rc += 1

print(len(balls))