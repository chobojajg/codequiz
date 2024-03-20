def solution(park, routes):
    answer = []
    c = len(park)
    r = len(park[0])
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start = [i, j] # 0은c 1은 r
    for i in routes:
        v, n = i.split()
        n = int(n)
        if v == 'E' and 0 <= start[1] + n < r:
            check = True
            for j in range(1, n + 1):
                if park[start[0]][start[1] + j] == 'X':
                    check = False
            if check:
                start[1] += n
        elif v == 'W' and r > start[1] - n >= 0:
            check = True
            for j in range(1, n + 1):
                if park[start[0]][start[1] - j] == 'X':
                    check = False
            if check:
                start[1] -= n
        elif v == 'S' and 0 <= start[0] + n < c:
            check = True
            for j in range(1, n + 1):
                if park[start[0] + j][start[1]] == 'X':
                    check = False
            if check:
                start[0] += n
        elif v == 'N' and c > start[0] - n >= 0:
            check = True
            for j in range(1, n + 1):
                if park[start[0] - j][start[1]] == 'X':
                    check = False
            if check:
                start[0] -= n
    return start