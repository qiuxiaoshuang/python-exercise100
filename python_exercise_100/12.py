# 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
# 对正整数n，如果用2到  之间的所有整数去除，均无法整除，则n为质数。 　　　
import math
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n

A=range(101,200)
for a in A:
    print(is_prime(a))
