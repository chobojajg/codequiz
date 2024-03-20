def solution(data, ext, val_ext, sort_by):
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    et = dic[ext]
    sk = dic[sort_by]
    answer = []
    for i in data:
        if i[et] < val_ext:
            answer.append(i)
    
    answer.sort(key=lambda x:x[sk])
    return answer