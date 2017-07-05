# def draw_stars(num):
#     star = '*'
#     for i in range(len(num)):
#         print star * num[i]

def draw_stars(num):
    for i in num:
        if isinstance(i,int):
            print '*' * i
        elif isinstance(i,str):
            print i.lower()[0] * len(i)


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)