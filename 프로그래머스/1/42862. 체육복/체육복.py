def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    remove_set = []
    
    for i in lost:
        if i in reserve:
            remove_set.append(i)
    lost = [i for i in lost if i not in remove_set]
    reserve = [i for i in reserve if i not in remove_set]
    
    los = lost[:]
            
    for i in lost:
        if i - 1 >= 1:
            if i - 1 in reserve:
                los.pop(los.index(i))
                reserve.pop(reserve.index(i - 1))
                continue
        if i + 1 <= n:
            if i + 1 in reserve:
                los.pop(los.index(i))
                reserve.pop(reserve.index(i + 1))
                continue
    answer = n - len(los)
        
    return answer