n = int(input())
for _ in range(n):
    file_num, file_pos = map(int, input().split())
    _list = list(map(int, input().split()))
    print_num = 1
    file_list = []

    for i in range(file_num):
        if i == file_pos:
            file_list.append([_list[i], True])
        else:
            file_list.append([_list[i], False])
    max_file = max(file_list)
    while True:
        if file_list[0][0] == max_file[0]:
            if file_list[0][1]:
                print(print_num)
                break
            file_list.pop(0)
            print_num += 1
            max_file = max(file_list)
        else:
            file_list.append(file_list.pop(0))