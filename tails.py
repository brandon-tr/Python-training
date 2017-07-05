import random

for i in range(0, 5001):
    random_num = random.randint(0,1)
    if(random_num == 1):
        print 'Heads'
    else:
        print 'Tails'