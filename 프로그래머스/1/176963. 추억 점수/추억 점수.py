def solution(name, yearning, photo):
    answer = []
    point = {}
    for i in range(len(name)):
        point[name[i]] = yearning[i]
    for i in photo:
        score = 0
        for j in i:
            if j in point:
                score += point[j]
        answer.append(score)
    return answer