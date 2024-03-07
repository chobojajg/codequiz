T = int(input())
for test_case in range(1, T + 1):
    a = input()
    a_list = list(a[::-1])
    for i in range(len(a_list)):
        if a_list[i] == 'b':
            a_list[i] = 'd'
        elif a_list[i] == 'd':
            a_list[i] = 'b'
        elif a_list[i] == 'q':
            a_list[i] = 'p'
        elif a_list[i] == 'p':
            a_list[i] = 'q'
    result = ''.join(a_list)
    print(f"#{test_case} {result}")
