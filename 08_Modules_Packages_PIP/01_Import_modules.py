# how to import
# completed-> import math
# specific functions-> from math import pi
import math
print(math.sin(math.pi/2))

# exercise dice
import random
number =  random.randint(1,6)
print(number)
if(number==6):
    print("you are lucky")
else:
    print("try again")