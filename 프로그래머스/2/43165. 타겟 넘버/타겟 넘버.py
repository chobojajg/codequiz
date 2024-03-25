answer = 0


def dfs(numbers, target, now, num):
    global answer
    if now == len(numbers):
        if num == target:
            answer += 1
        return
    dfs(numbers, target, now + 1, num + numbers[now])
    dfs(numbers, target, now + 1, num - numbers[now])
    

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer