def checkwordone(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    check = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            check += 1
    return check


def solution(begin, target, words):
    answer = 0
    lst = []
    if target not in words:
        return 0
    visit = [False] * (len(words))

    def dfs(v, begin, cnt):
        visit[v] = True
        cnt += 1
        if begin == target:
            lst.append(cnt)
            return
        for i in range(len(words)):
            if not visit[i] and checkwordone(begin, words[i]) == 1:
                begin = words[i]
                dfs(i, begin, cnt)

    for i in range(len(words)):
        if not visit[i] and checkwordone(begin, words[i]) == 1:
            begin = words[i]
            dfs(i, begin, answer)

    return min(lst)