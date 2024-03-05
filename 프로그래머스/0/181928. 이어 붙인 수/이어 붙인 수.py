def solution(num_list):
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))
    odd_num = ''.join(odd)
    even_num = ''.join(even)
    return int(odd_num) + int(even_num)