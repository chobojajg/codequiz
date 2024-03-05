def solution(cipher, code):
    answer = ''
    num = 1
    while num * code <= len(cipher):
        answer += cipher[num * code - 1]
        num += 1
    
    return answer