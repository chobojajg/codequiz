prime = {0:2}
def checkprime(n):
    a = int(n ** (1/2)) + 1
    for i in range(2, a):
        if n % i == 0:
            return False
    return True

def solution(n):
    for i in range(3, n + 1):
        isprime = checkprime(i)
        if isprime:
            prime[len(prime)] = i
    return len(prime)
    # count = n-1
    # for i in range(2,n+1):
    #     for x in range(2,i):
    #         if i % x == 0:
    #             count -= 1
    #             break
    # return count
    
    # answer = 0
    # for i in range(3, n + 1):
    #     isprime = True
    #     if i % 2 == 0:
    #         isprime = False
    #     else:
    #         for j in range(len(prime)):
    #             if i % prime[j] == 0:
    #                 isprime = False
    #                 break
    #     if isprime:
    #         prime[len(prime)] = i
    # answer = len(prime)
    # return answer