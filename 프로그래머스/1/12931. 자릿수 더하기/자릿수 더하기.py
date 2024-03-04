def solution(n):
    strarr = list(str(n))
    numarr = []
    for i in range(len(strarr)):
        numarr.append(int(strarr[i]))
    return sum(numarr)