import re
def solution(myString):
    answer = re.sub("[a-l]", "l", myString)
    return answer