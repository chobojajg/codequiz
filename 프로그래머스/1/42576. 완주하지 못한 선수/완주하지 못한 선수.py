def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append("_")
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer
    # for i in participant:
    #     if i in completion:
    #         completion.remove(i)
    #     else:
    #         answer = i
    #         break
    # return answer