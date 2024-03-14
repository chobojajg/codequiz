menu = {
    "iceamericano":'아메리카노',
    "americanoice":'아메리카노',
    "hotamericano":'아메리카노',
    "americanohot":'아메리카노',
    "americano":'아메리카노',
    "anything":'아메리카노',
    "icecafelatte":'카페 라테',
    "cafelatteice":'카페 라테',
    "hotcafelatte":'카페 라테',
    "cafelattehot":'카페 라테',
    "cafelatte":'카페 라테',
}
price = {
    '아메리카노':4500,
    '카페 라테':5000
}
def solution(order):
    answer = 0
    for i in order:
        answer += price[menu[i]]
    return answer