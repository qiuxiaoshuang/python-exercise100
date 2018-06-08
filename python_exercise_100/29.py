# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
x = int(input("请输入一个数:\n"))
a = int(x / 10000)
b = int(x % 10000 / 1000)
c = int(x % 1000 / 100)
d = int(x % 100 / 10)
e = int(x % 10)
if a!=0:
    print("五位数")
    print(e,d,c,b,a)
elif b!=0:
    print("四位数")
    print(e,d,c,b)
elif c != 0:
    print("三位数")
    print(e, d, c)
elif d != 0:
    print("二位数")
    print(e, d)
else:
    print("一位数")
    print(e)