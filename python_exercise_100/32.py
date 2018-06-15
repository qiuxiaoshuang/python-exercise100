# 题目：按相反的顺序输出列表的值。
s=[1, 'a', 'vda', '5']
a=len(s)
while a>0:
    print(s[a-1])
    a= a-1

# 法二
for i in s[::-1]:
    print (i)