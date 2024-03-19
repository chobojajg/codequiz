def solution(s, skip, index):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(s)):
        num = 0
        for j in range(index):
            num += 1
            if alpha.index(s[i]) + num > 25:
                num -= 26
            while alpha[alpha.index(s[i]) + num] in skip:
                num += 1
                if alpha.index(s[i]) + num > 25:
                    num -= 26
        answer += alpha[alpha.index(s[i]) + num]
            
    return answer