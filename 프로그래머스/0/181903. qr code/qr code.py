def solution(q, r, code):
    answer = ''
    lst = []
    for i in range(len(code)):
        if i % q == r:
            lst.append(code[i])
    answer = ''.join(lst)
    return answer