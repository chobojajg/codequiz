from math import gcd

def solution(a, b):
    n = int(b / gcd(a, b))
    rm = [2, 5]
    for i in rm:
        while(True):
            if n % i == 0:
                n /= i
            else:
                break
    if n == 1:
        return 1
    else:
        return 2
        