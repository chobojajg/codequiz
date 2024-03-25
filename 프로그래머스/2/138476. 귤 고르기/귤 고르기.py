def solution(k, tangerine):
    answer = 0
    arr = {}
    for i in range(1, max(tangerine) + 1):
        arr[i] = 0
    for i in tangerine:
        arr[i] += 1
    arr = dict(sorted(arr.items(), key=lambda x: x[1], reverse=True))
    box = 0
    cnt = 0
    for i in arr:
        box += arr[i]
        cnt += 1
        if box >= k:
            return cnt