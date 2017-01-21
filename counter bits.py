import math
def countBits(n):
    counter = 0
    while(n >0):
            num = n%2
            n = math.floor(n/2)
            if(num==1):
                counter +=1
    return counter