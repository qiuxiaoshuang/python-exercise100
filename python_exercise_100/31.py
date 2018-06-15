# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
first_letter= input("please input the first letter of the week :\n")
if first_letter== 'M':
    print("the week is Monday")
elif first_letter=='W':
    print("the week is Wednesday")
elif first_letter=='F':
    print("the week is Friday")
else:
    second_letter= input("please input the second letter of the week :\n")
    if first_letter== 'T' and  second_letter== 'u':
        print("the week is Tuesday")
    elif first_letter== 'T' and  second_letter== 'h':
        print("the week is Thursday")
    elif first_letter == 'S' and second_letter == 'a':
        print("the week is Saturday")
    elif first_letter == 'S' and second_letter == 'u':
        print("the week is Sunday")
    else:
        print("输入有误")