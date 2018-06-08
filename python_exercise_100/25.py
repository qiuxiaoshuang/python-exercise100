# 求1+2!+3!+...+20!的和。
def myfact(n):
    if n>=0 and n<2:
        return 1
    else:
        return n*myfact(n-1)


sum=0
for i in range(1,21):
    sum=sum+myfact(i)
print(sum)