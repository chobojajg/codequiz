def solution(rank, attendance):
    answer = 0
    newlist = []
    for i in range(len(attendance)):
        if attendance[i]:
            newlist.append([rank[i], i])
    newlist.sort()
    answer = 10000 * newlist[0][1] + 100 * newlist[1][1] + newlist[2][1]
    return answer