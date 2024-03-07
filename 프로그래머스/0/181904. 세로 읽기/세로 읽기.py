def solution(my_string, m, c):
    lis = []
    for i in range(len(my_string)+1):
        if i % m == 0 and i != 0:
            lis.append(my_string[i-m:i])
    lis2 = []
    for i in lis:
        lis2.append(i[c-1])
    return ''.join(lis2)