# 题目：求100之内的素数。(用一个数分别去除2到sqrt(这个数),如果能被整除,则表明此数不是素数,反之是素数)
import math
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n

A=range(1,100)
for a in A:
    print(is_prime(a))

