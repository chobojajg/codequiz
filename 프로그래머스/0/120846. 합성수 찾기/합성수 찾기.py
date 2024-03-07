def getcount(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def solution(n):
    answer = 0
    count = 0
    for i in range(1, n + 1):
        count = getcount(i)
        if count > 2:
            answer += 1
    
    return answer