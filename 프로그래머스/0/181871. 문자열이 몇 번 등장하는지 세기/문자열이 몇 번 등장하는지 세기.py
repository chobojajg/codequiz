def solution(myString, pat):
    answer = 0
    while pat in myString:
        answer += 1
        index = myString.index(pat) + 1
        myString = myString[index:]
    return answer