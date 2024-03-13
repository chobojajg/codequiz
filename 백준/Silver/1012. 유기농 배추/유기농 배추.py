import sys
case_num = int(sys.stdin.readline())
for _ in range(case_num):
    m, n, bea = map(int, sys.stdin.readline().split())
    bea_list = []
    for i in range(bea):
        x, y = map(int, sys.stdin.readline().split())
        bea_list.append([x, y])
    check_list = {}
    result = 0
    bea_queue = []
    while len(bea_list) > 0:
        if len(bea_queue) == 0:
            result += 1
            check_list[result] = []
            bea_queue.append(bea_list.pop(0))

        beachu = bea_queue.pop(0)
        check_list[result].append(beachu)
        if [beachu[0] + 1, beachu[1]] in bea_list:
            bea_queue.append([beachu[0] + 1, beachu[1]])
            bea_list.remove([beachu[0] + 1, beachu[1]])
        if [beachu[0], beachu[1] + 1] in bea_list:
            bea_queue.append([beachu[0], beachu[1] + 1])
            bea_list.remove([beachu[0], beachu[1] + 1])
        if [beachu[0] - 1, beachu[1]] in bea_list:
            bea_queue.append([beachu[0] - 1, beachu[1]])
            bea_list.remove([beachu[0] - 1, beachu[1]])
        if [beachu[0], beachu[1] - 1] in bea_list:
            bea_queue.append([beachu[0], beachu[1] - 1])
            bea_list.remove([beachu[0], beachu[1] - 1])

    print(result)