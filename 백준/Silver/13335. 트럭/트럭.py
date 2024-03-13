import sys
n, bridge_length, weight = map(int, sys.stdin.readline().split())
truck_weights = list(map(int, sys.stdin.readline().split()))
answer = 0
weightsum = 0
onb = []
count = []
while truck_weights or onb:
    for i in range(len(count)):
        count[i] += 1
        if i == len(count) - 1:
            if count[0] > bridge_length:
                weightsum -= onb[0]
                onb.pop(0)
                count.pop(0)
    if truck_weights:
        if weightsum + truck_weights[0] <= weight:
            weightsum += truck_weights[0]
            onb.append(truck_weights.pop(0))
            count.append(1)
    answer += 1
print(answer)