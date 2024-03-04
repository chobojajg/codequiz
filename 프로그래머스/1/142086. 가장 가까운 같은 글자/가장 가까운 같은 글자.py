def solution(s):
    answer = []
    for i,string in enumerate(s):
        if string.isalpha():
            if string in s[:i]:
                answer.append(i-s.index(string))
                st = list(s)
                st[s.index(string)] = '0'
                s = ''.join(st)
            else:
                answer.append(-1)
    return answer