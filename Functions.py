# def oddEven():
#     for i in range (1,2001):
#         if i % 2 == 0:
#             print "{} is even".format(i)
#         else:
#             print "{} is odd".format(i)
def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
# oddEven()
# a = [2,4,10,16]
# b = multiply(a,5)
# print b


def layered(arr):
    new_arr = []
    for i in arr:
        append_arr = []
        for j in range(0,i):
            append_arr.append(1)
            new_arr.append(append_arr)
    return new_arr

x = layered(multiply([2,4,5],3))
print x