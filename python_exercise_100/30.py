# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
s = int(input("请输入一个数字：\n"))
x = str(s)
m = len(x)
flag = True
if m%2 == 1:
    for i in range(int(m/2)-1):
        if x[i] != x[-i-1]:
            flag=False
            break
    if flag:
        print("是回文")
    else:
        print("不是回文")





