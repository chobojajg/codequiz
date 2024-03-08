s = input()
check_list = []
check_num = 0
result = 0
for i in s:
    if i == '(':
        check_list.append(i)
        check_num += 1
    else:
        check_num -= 1
        if check_list[-1] == i:
            result += 1
        else:
            result += check_num
        check_list.append(i)
print(result)