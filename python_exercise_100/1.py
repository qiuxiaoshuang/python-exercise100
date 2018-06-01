#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

common=[1,2,3,4]
w=0
for i in common:
    for j in common:
        for k in common:
            w=i+10*j+100*k
            if i!=k and i!=j and j!=k:
                print(w)
