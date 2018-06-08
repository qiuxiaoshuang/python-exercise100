# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import re
def is_num(num):#判断是否为数字
    value = re.compile(r'^[-+]?[0-9]+$')
    result=value.match(num)
    if result:
        print("为数字")
        return True
    else:
        print("不为数字")
        return False


def is_letter(letter):#判断是否为字母
    value = re.compile(r'^[-+]?[a-z]|[-+]?[A-Z]$')
    result=value.match(letter)
    if result:
        print("为字母")
        return True
    else:
        print("不为字母")
        return False

def is_blank(blank):#判断是否为空格
    value = re.compile(r'^[-+]?\\s$')
    result=value.match(blank)
    if result:
        print("为空格")
        return True
    else:
        print("不为空格")
        return False


strs=input("输入一行字符:\n")
for str in strs:
    is_num(str)
    is_letter(str)
    is_blank(str)
    print("--------------------------------------------")