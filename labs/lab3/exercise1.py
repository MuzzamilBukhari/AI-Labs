# i

sq = lambda num : num ** 2

cb = lambda num : num ** 3

l1 = [2,3,4]
sqList = []
cbList = []

for num in l1:
    sqList.append(sq(num))
    cbList.append(cb(num))

print(sqList)
print(cbList)

# ii
check_first_char = lambda str, char : str[0] == char

print(check_first_char('muzzamil', 'a'))
print(check_first_char('muzzamil', 'm'))


# iii
from datetime import datetime

now = datetime.now()

get_year = lambda dt : dt.year
get_month = lambda dt : dt.month
get_date = lambda dt : dt.day
get_time = lambda dt : dt.strftime("%H:%M:%S")

year = get_year(now)
month = get_month(now)
date = get_date(now)
time = get_time(now)

print(year, month, date, time)
