# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def xf_print(s,l):
    if l==0:
        return
    print(s[l-1])
    xf_print(s,l-1)




s=input("输入字符串:\n")
l=len(s)
xf_print(s,l)