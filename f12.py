#IMPORT LIABRARY
#import math
#print(math.sqrt(16))
#print(math.factorial(4))
#print(math.pow(20,4))

#imort random
import random
#print(random.random())
#a=random.random()
#if(a<.5):
    #print('heads')
#else:
    #print('tails')
    dice1=(random.randrange(1,7))
    dice2=(random.randrange(1,7))
    total=dice1+dice2
    print("your pair of dice is:",total)