try:
    # 获取用户输入的年份
    year = int(input("请输入年份："))
    # 判断是否为闰年
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("此年份是闰年")
    else:
        print("此年份不是闰年")
except ValueError:
    print("输入无效，请输入一个有效的数字年份。")
