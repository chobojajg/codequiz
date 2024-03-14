def solution(arr):
    answer = []
    try:
        start = arr.index(2)
        end = len(arr) - arr[::-1].index(2)
        answer = arr[start:end]
    except:
        answer.append(-1)
    return answer