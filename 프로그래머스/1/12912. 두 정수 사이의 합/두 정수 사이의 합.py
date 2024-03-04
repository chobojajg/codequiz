def solution(a, b):
    answer = 0
    lis = [a, b]
    b = max(lis)
    s = min(lis)
    
    #for i in range(s, b + 1):
    #    answer = answer + i
    
    answer = (b + s) * (b - s + 1) / 2
    
    return answer