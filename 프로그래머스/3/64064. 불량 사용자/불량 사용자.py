from itertools import permutations
def bancheck(user_list, ban_list):
    for i in range(len(ban_list)):
        if len(user_list[i]) != len(ban_list[i]):
            return False

        for j in range(len(user_list[i])):
            if ban_list[i][j] == "*":
                continue
            if ban_list[i][j] != user_list[i][j]:
                return False
    return True 
def solution(user_id, banned_id):
    answer = []
    p = list(permutations(user_id, len(banned_id)))
    for i in p:
        if bancheck(i, banned_id):
            i = set(i)
            if i not in answer:
                answer.append(i)
    return len(answer)