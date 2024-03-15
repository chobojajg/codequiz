def solution(arrows):
    x, y = 0, 0
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    answer = 0
    data = {}
    for arrow in arrows:
        for i in range(2):
            x2 = x + dx[arrow]
            y2 = y + dy[arrow]
            if (x2, y2) in data and (x, y) not in data[(x2, y2)]:
                if (x, y) not in data:
                    data[(x, y)] = []
                if (x2, y2) not in data:
                    data[(x2, y2)] = []
                answer += 1
                data[(x, y)].append((x2, y2))
                data[(x2, y2)].append((x, y))
            elif (x2, y2) not in data:
                if (x, y) not in data:
                    data[(x, y)] = []
                if (x2, y2) not in data:
                    data[(x2, y2)] = []
                data[(x, y)].append((x2, y2))
                data[(x2, y2)].append((x, y))
            x, y = x2, y2
    return answer