def solution(n, words):
    answer = []
    count = 0
    word = []
    
    for i in range(len(words)):
        if i % n == 0:
            count += 1
        if i > 0:
            if words[i] in word or words[i][0] != words[i - 1][-1]:
                answer = [(i % n) + 1, count]
                return answer
        word.append(words[i])
    answer = [0, 0]
    
    return answer