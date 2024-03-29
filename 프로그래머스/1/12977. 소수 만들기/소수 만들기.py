def checkprime(n):
    a = int(n ** (1/2)) + 1
    for i in range(2, a):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if checkprime(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer