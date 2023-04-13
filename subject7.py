from datetime import date, timedelta

# 模拟输入起始及截止日期
begin = date(1964, 10, 11)
end = date(2020, 7, 24)

# range 函数进行遍历
for i in range((end - begin).days + 1):
    # date 对象和 timedelta 进行时间间隔计算，并返回 date 对西那个
    day = begin + timedelta(days=i)
    if day.day %2 == 0:
        continue
    # 也可以根据需要，转换成 str 字符串对象
    day_str = day.strftime('%Y%m%d')
    # other things
    day_int = int(day_str)
    num = int(bin(day_int)[2:][::-1],2)
    if num == day_int:
        print(day)
