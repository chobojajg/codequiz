search = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
def solution(msg):
    answer = []
    while len(msg) > 0:
        word = ""
        count = 0
        word += msg[count]
        while word in search:
            if len(word) < len(msg):
                count += 1
                word += msg[count]
            else:
                break
        if word not in search:
            search[word] = len(search) + 1
            word = word[:-1]
        answer.append(search[word])
        msg = msg[len(word):]
            
    return answer