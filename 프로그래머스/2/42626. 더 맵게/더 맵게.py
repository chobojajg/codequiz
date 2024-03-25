import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)
    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h) + (heapq.heappop(h) * 2))
        except:
            return -1
        answer += 1
    return answer
    
# def solution(scoville, K):
#     answer = 0
#     while min(scoville) < K:
#         if len(scoville) < 2:
#             return -1
#         scoville.sort()
#         scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
#         answer += 1
#     return answer