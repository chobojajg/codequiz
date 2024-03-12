import heapq

n, c = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
for _ in range(c):
    min_card = heapq.heappop(cards)
    sec_min_card = heapq.heappop(cards)
    sum_min_card = min_card + sec_min_card
    heapq.heappush(cards, sum_min_card)
    heapq.heappush(cards, sum_min_card)
print(sum(cards))