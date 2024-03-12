def remove_card(lst):
    new_lst = []
    for i, e in enumerate(lst):
        if i % 2 != 0:
            new_lst.append(e)
    return new_lst


n = int(input())
card = [i for i in range(1, n+1)]
temp_card = 0

while len(card) > 1:
    if len(card) % 2 == 0:
        card = remove_card(card)
    else:
        temp_card = card.pop()
        card = remove_card(card)
        card.insert(0, temp_card)

print(card[0])