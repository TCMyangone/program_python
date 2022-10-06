import datetime

now_year = datetime.datetime.now().year
now_month = datetime.datetime.now().month
now_day = datetime.datetime.now().day

id = input('请输入身份证号: ')
user_year = int(id[6:10])
user_month = int(id[10:12])
user_day = int(id[12:14])


if now_month >= user_month and now_day >= user_day:
    print('年龄:', now_year - user_year)
else:
    print('年龄:', now_year - user_year - 1)
