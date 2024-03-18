def solution(arr):
    answer = [[]]
    ln = len(arr)
    for i in arr:
        if ln < len(i):
            ln = len(i)
    for i in range(ln):
        if len(arr) < ln:
            arr.append([])
        for j in range(ln):
            if len(arr[i]) < ln:
                arr[i].append(0)
            else:
                break 
    return arr