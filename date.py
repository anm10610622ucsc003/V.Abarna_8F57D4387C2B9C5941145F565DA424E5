Import datetime
Print("This program Calculate age in seconds approximately ")
birth_day=int(input ("Enter the day(1-31):"))
birth_month=int(input("Enter the month(1-12):"))
birth_year=int(input("Enter the year(4 digit):"))
current _day=datetime.date.today().day
current _month=datetime.date.today().month
current _year=datetime.date.today().year
numsecs_day=24×60×60
numsecs_year=365×numsecs-day
avgnumsecs_year=(4×numsecs_year+numsecs_day)//4
avgnumsecs_month=avgnumsecs_year//12
numsecs_1900 to dob=(birth_year-1900)×avgnumsecs_year
+(birth_year)×avgnumsecs_month
+(birth_day×numsecs_day)
numsecs_1900 to current=(current_year-1900)×avgnumsecs_year
+(current_month-1)×avgnumsecs_month
+(current_day×numsecs_day)
age_secs=numsecs_1900 to current -numsecs_1900 to dob
