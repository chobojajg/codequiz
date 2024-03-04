def solution(price, money, count):
    answer = -1
    mcount = 0

    for i in range(1, count + 1):
        mcount = mcount + (price * i)
    
    answer = mcount - money
    
    if answer < 0:
        answer = 0
    
    return answer