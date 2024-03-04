dic = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def solution(s):
    answer = 0
    num = []
    word = ""
    result = ""
    
    for i in s:
        if i.isdigit():
            num.append(i)
        else:
            word += i
            if len(word) > 2:
                if word in dic:
                    num.append(dic.get(word))
                    word = ""
    
    result = "".join(map(str, num))
    answer = int(result)
    
    return answer