# 题目：利用递归方法求5!。
def jiecheng(n):
    if n>=0 and n<2:
        return 1
    else:
        return n*jiecheng(n-1)


print(jiecheng(5))