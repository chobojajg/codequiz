def third(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        if not mod:
            rev_base += "3"
            n -= 1
        else:
            rev_base += str(mod)

    return rev_base[::-1] 

def solution(n):
    answer = str(third(n))
    answer = answer.replace("3", "4")
    return answer