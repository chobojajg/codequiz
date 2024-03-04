def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p = []
    p.append(a)
    p.append(b)
    p.append(c)
    
    countarr = []
    for i in p:
        count = 0
        for j in range(len(answers)):
            n = j
            if n >= len(i):
                n %= len(i)
            if i[n] == answers[j]:
                count += 1
        countarr.append(count)
    result = list(filter(lambda x: countarr[x] == max(countarr), range(len(countarr))))
    for i in range(len(result)):
        result[i] += 1
    return result