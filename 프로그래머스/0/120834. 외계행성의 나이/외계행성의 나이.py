dic = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j"}
def solution(age):
    answer = ''
    lis = []
    agestr = str(age)
    for i in agestr:
        lis.append(dic.get(int(i)))
    
    answer = "".join(lis)
    
    return answer