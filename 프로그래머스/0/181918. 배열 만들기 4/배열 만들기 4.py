def solution(arr):
    stk = []
    while len(arr):
        a = arr.index(min(arr))
        if arr[a] in stk:
            stk.pop()
        stk.append(arr.pop(a))
        arr = arr[a:]

    return stk