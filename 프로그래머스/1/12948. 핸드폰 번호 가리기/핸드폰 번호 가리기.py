def solution(phone_number):
    answer = ''
    plist = []
    plist = list(phone_number)
    
    for i in range(0, len(phone_number[0:-4])):
        plist[i] = "*"
        
    answer = "".join(plist)
    
    return answer