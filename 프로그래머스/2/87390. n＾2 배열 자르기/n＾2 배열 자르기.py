dic = {}

def solution(n, left, right):
    answer = []
    low = left // n
    lowless = left % n
    high = right // n
    highless = right - (n * low)
    for i in range(low, high + 1):
        lis = []
        for k in range(i):
            lis.append(i+1)
        for j in range(i + 1, n + 1):
            lis.append(j)
        answer = answer + lis
    answer = answer[lowless:highless + 1]
    return answer