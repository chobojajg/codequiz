def solution(arr, queries):
    answer = []
    for i in queries:
        c_a = arr[i[0]:i[1] + 1]
        ln = len(c_a)
        for j in range(ln):
            if i[2] < min(c_a):
                answer.append(min(c_a))
                break
            else:
                c_a.remove(min(c_a))
                if j + 1 == ln:
                    answer.append(-1)
    return answer