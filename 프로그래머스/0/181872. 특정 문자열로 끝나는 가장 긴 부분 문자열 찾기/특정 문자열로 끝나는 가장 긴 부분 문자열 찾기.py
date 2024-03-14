def solution(myString, pat):
    rs = myString[::-1]
    rp = pat[::-1]
    answer = rs[rs.index(rp):][::-1]
    return answer