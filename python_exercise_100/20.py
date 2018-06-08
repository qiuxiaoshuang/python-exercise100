# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

def high_distance(h):#反弹高度
    if h==0:
        return 0
    else:
        return float(h)/2


s=[]
s.append(100)
# b=input("落地次数为:\n")
b=10
for i in range(1,int(b)+1):
    s.append(high_distance(s[i-1]))
    print(s[int(i)])
distance=0
for i in range(1,int(len(s)-1)):
    distance=distance+float(s[i])*2
distance=distance+s[0]
print(distance)
print(s[int(b)])