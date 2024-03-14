def solution(before, after):
    answer = 0
    bli = list(before)
    ali = list(after)
    
    bli.sort()
    ali.sort()
    
    if bli == ali:
        return 1
    
    return answer