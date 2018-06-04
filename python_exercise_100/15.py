# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
sorces=input("请输入你的分数:\n")
if sorces >='90':
    grade='A'
elif sorces>='60' and sorces<'89':
    grade='B'
elif sorces < '60':
    grade='C'
print(str(sorces),grade)
