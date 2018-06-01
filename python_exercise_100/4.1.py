# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 阳历平年365(1-12月分别为31天，28天，31天，30天，31天，30天，31天，31天，30天，31天，30天，31天)。
# 闰年共有366天(1-12月分别为31天，29天，31天，30天，31天，30天，31天，31天，30天，31天，30天，31天)。

year_dict = {
    "P": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    "R": [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
}


# 判断一年是平年还是闰年

def check_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return "R"
    elif year % 4 == 0:
        return "R"
    return "P"

year=input("输入年:\n")
month=input("输入月:\n")
day=input("输入日:\n")

yl = year_dict[check_year(int(year))]

total_day = 0
month_idx = 0
while month_idx < int(month) - 1:
   total_day += yl[month_idx]
   month_idx += 1

total_day += int(day)
print(total_day)