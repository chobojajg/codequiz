import itertools

def checkcount(k, index, dic):
    count = 0
    for i in range(len(dic)):
        if dic[index[i]][0] <= k:
            k -= dic[index[i]][1]
            count += 1
    return count
    
def solution(k, dungeons):
    answer = 0
    dic = {}
    index = []
    dungeons.sort()#key=lambda x:x[1])
    for i in range(len(dungeons)):
        dic[i] = dungeons[i]
        index.append(i)
    result = list(itertools.permutations(index, len(index)))
    for i in result:
        num = 0
        num = checkcount(k, i, dic)
        if num > answer:
            answer = num
    return answer