def solution(x):
    xstrarr = list(str(x))
    xintarr = []
    for i in range(len(xstrarr)):
        xintarr.append(int(xstrarr[i]))
    
    if x % sum(xintarr) == 0:
        answer = True
    else:
        answer = False
    
    return answer