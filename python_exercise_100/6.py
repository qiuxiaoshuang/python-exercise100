#题目：斐波那契数列。
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

# s=[]
# n=input("输入斐波那契数列的n值")
# if n==0:
#     s[0]=0
#     print(s[0])
# elif n==1:
#     s[1]=1
#     print(s[1])
# else:
#     while(int(n)>=2):
#         s[n]=s[n-1]=s[n-2]
#         print(s[n])

#法一
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


# 输出了第10个斐波那契数列
print(fib(10))






#法2
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# 输出了第10个斐波那契数列

print(fib(6))