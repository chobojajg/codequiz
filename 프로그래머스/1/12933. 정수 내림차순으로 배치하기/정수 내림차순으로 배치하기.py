def solution(n):
    answer = 0
    
    listn = list(str(n))
    listnumn = []
    listn2 = []
    
    for i in range(len(listn)):
        listnumn.append(int(listn[i]))
    
    listnumn.sort(reverse = True)
    
    for i in range(len(listnumn)):
        listn2.append(str(listnumn[i]))
        
    answer = int("".join(listn2))
    
    return answer