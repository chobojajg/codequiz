def solution(str1, str2):
    return (1 if str2 in str1 else 2)

    # for i in range(len(str1)):
    #     stack = ""
    #     if str1[i] == str2[0]:
    #         if i + len(str2) > len(str1):
    #             return 2
    #         stack += str1[i:i+len(str2)]
    #         if stack == str2:
    #             return 1
    # return 2
            
