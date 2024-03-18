def solution(arr, n):
    la = len(arr)
    if la % 2 == 0:
        for i in range(la):
            if i % 2 == 1:
                arr[i] += n
    else:
        for i in range(la):
            if i % 2 == 0:
                arr[i] += n
                
    return arr