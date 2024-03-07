def solution(s):
    
    s = s.lower()
    sarr = list(s)
    
    pcount = sarr.count("p")
    ycount = sarr.count("y")
    
    if pcount == ycount:
        answer = True
    else:
        answer = False
    
    return answer