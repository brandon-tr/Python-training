row = 'x   1  2  3  4  5  6  7  8   9  10  11  12'
number = [1,2,3,4,5,6,7,8,9,10,11,12,]
print row
for column in range (1,13):
    print column
    number[column-1]*=number[column-1]
    print number