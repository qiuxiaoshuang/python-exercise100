# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

win=int(input('请输入当月利润:\n'))
if win<=10:
    reward=win*0.1
elif win>10 and win<20:
    reward=10*0.1+(win-10)*0.075
elif win>20 and win<40:
    reward=10*0.1+10*0.075+(win-20)*0.05
elif win>40 and win<60:
    reward=10*0.1+10*0.075+10*0.05+(win-40)*0.03
elif win>60 and win<100:
    reward=10*0.1+10*0.075+10*0.05+30*0.03+(win-60)*0.015
else:
    reward=10*0.1+10*0.075+10*0.05+20*0.03+40*0.015

print("发放奖金 "+str(reward)+"万元")

