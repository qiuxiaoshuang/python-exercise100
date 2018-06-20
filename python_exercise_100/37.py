# 题目：对10个数进行排序。(未完成)
a=[]
str=input("please input 10 number")
print(str)
# print(type(str))
a.append(str.split(',',9))
print(a)
# print(type(a))
for i in range(9):
    min=0
    if a[i]<a[i+1]:
        min=a[i]