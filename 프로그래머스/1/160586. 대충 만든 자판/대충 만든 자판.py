def solution(keymap, targets):
    answer = []
    key = {}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in key:
                key[keymap[i][j]] = []
            key[keymap[i][j]].append(j + 1)
    for i in targets:
        num = 0
        for j in i:
            if j not in key:
                num = -1
                break
            num += min(key[j])
        answer.append(num)
            
    return answer