def solution(cards1, cards2, goal):
    check = 0
    for i in goal:
        if len(cards1) > 0:
            if i == cards1[0]:
                cards1.pop(0)
                check += 1
                continue
        if len(cards2) > 0:
            if i == cards2[0]:
                cards2.pop(0)
                check += 1
                continue
        break
    if len(goal) == check:
        return "Yes"
    return "No"
            