import datetime
from dateutil.relativedelta import relativedelta
def make_date(string):
    y, m, d = map(int, string.split('.'))
    now = datetime.date(y, m, d)
    return now
    
def solution(today, terms, privacies):
    answer = []
    dt = {}
    now = make_date(today)
    for i in terms:
        a, b = i.split()
        dt[a] = int(b)
    for i in range(len(privacies)):
        date, tp = privacies[i].split()
        date = make_date(date)
        if date + relativedelta(months = dt[tp]) <= now:
            answer.append(i+1)
        
    return answer