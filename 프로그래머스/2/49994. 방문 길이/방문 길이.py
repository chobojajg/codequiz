def solution(dirs):
    answer = 0
    lis = list(dirs)
    movelis = []
    point = [0,0]
    for i in lis:
        if i == "U":
            if point[1] + 1 <= 5:
                li = [point[0], (point[1] + point[1] + 1) / 2]
                if li not in movelis:
                    movelis.append(li)
                point[1] += 1
        elif i == "D":
            if point[1] - 1 >= -5:
                li = [point[0], (point[1] + point[1] - 1) / 2]
                if li not in movelis:
                    movelis.append(li)
                point[1] -= 1
        elif i == "R":
            if point[0] + 1 <= 5:
                li = [(point[0] + point[0] + 1) / 2, point[1]]
                if li not in movelis:
                    movelis.append(li)
                point[0] += 1
        elif i == "L":
            if point[0] - 1 >= -5:
                li = [(point[0] + point[0] - 1) / 2, point[1]]
                if li not in movelis:
                    movelis.append(li)
                point[0] -= 1
    answer = len(movelis)
    return answer