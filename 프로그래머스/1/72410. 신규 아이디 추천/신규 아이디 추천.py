import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^a-z0-9_.-]","",new_id)
    new_id = re.sub("(([.])\\2{1,})",".",new_id)
    new_id = new_id.strip(".")
    if not (new_id.replace(" ","")):
        new_id = "a"
    if(len(new_id)>=16):
        new_id = new_id[:15]
        new_id = new_id.strip(".")
    if(len(new_id)<=2):
        while(len(new_id)<=2):
            new_id = new_id + new_id[-1]
    answer = new_id
    return answer