string = input()
string = list(string)
for i in range(len(string)):
    if string[i].islower():
        string[i] = string[i].upper()
    else:
        string[i] = string[i].lower()
string = ''.join(string)
print(string)