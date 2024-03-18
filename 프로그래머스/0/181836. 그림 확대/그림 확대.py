def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        word = []
        for j in range(len(picture[i])):
            for n in range(k):
                word.append(picture[i][j])
        for m in range(k):
            answer.append(''.join(word))
    return answer