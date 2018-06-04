# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
import  math


def is_flower_num(num):
    x = int(num / 100)
    y = int((num - x * 100) / 10)
    z = int(num - x * 100 - y * 10)
    if num == math.pow(x, 3) + math.pow(y, 3) + math.pow(z, 3):
        print(str(u) + "是水仙花数")




for u in range(100,500):
    print(is_flower_num(u))