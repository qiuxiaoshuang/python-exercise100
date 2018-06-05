# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
Tn=0
sum=0
a=int(input("输入一个0-9之间的数字:\n"))
b=int(input("请输入你想要几个数相加:\n"))
for b in range(b):
    Tn=Tn+a
    a=a*10
    print(Tn)
