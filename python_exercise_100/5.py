#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#法一
# print("请输入三个整数")
# x=input("输入整数x:\n")
# y=input("输入整数y:\n")
# z=input("输入整数z:\n")
# if x<y:
#     if x>z:
#         print(z,x,y)
#     else:
#         if y<z:
#             print(x,y,z)
#         else:
#             print(x,z,y)
# else:
#     if y>z:
#         print(z,y,x)
#     else:
#         if x<z:
#             print(y,x,z)
#         else:
#             print(y,z,x)


#法二
# l=[]
# l.append(x)
# l.append(y)
# l.append(z)
# l.sort()
# print(l)



#法三
l=[]
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print (l)