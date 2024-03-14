def solution(arr):
    answer = -1
    before = []
    while True:
        if arr != before:
            before = arr[:]
            answer += 1
        else:
            break
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
    return answer