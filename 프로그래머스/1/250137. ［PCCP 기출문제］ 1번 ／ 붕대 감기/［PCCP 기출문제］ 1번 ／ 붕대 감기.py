def solution(bandage, health, attacks):
    answer = 0
    cnt = 0
    hp = health
    for i in range(1, attacks[-1][0] + 1):
        if attacks[0][0] == i:
            data = attacks.pop(0)
            hp -= data[1]
            cnt = 0
            if hp <= 0:
                return -1
        else:
            hp += bandage[1]
            cnt += 1
            if cnt == bandage[0]:
                hp += bandage[2]
                cnt = 0
            if hp > health:
                hp = health
    if hp <= 0:
        return -1
    return hp