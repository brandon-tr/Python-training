l = ['magical unicorns',10,'hello',-9,'world']
sum = 0
int1 = False
str1 = False
Mixed = False
stringCon = ''
for i in l:
    if type(i) is int or  type(i) is float:
        sum = sum + i
        int1 = True
    elif type(i) is str:
        stringCon = stringCon + i + ' '
        str1 = True
    if int1 == True and str1 == True:
        Mixed = True
print (sum, stringCon, Mixed)
