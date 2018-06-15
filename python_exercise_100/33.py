# 题目：按逗号分隔列表。
# 法一
s= ['a', 1, 'asd', 'q']
a= str(s)
print(type(a))
s1= a.split(', ')
print(type(s1))
print(s1)

# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 法二
L = [1, 2, 3, 4, 5]
s2 = ','.join(str(n) for n in L)
print(type(s2))
print(s2)