from calendar import month_name
from typing import Dict


days = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
        'May': 31, 'June': 30, 'July': 31, 'August': 31,
        'September': 30, 'October': 31, 'November': 30, 'December': 31}

# Part A

print("===========- Part A -===========")

Month = input("Enter the name of the month: ")
print(days[Month])

# Part B
print("===========- Part B -===========")
print(sorted(days))

# Part C
print("===========- Part C -===========")

for i in days:
    if days[i] == 31:
        print(i)

# Part D
print("===========- Part D -===========")
c = [("February", 28)]
for i in days.keys():
    if days[i] == 30:
        c.append((i, 30))

for i in days.keys():
    if days[i] == 31:
        c.append((i, 31))
print(c)

# Part E
print("===========- Part E -===========")
month_abbr = input("Enter atleast the first 3 letters of the name of month: ")
Mon_List = list(days.keys())
for i in Mon_List:

    if i[:3].lower() == month_abbr[:3].lower():
        print(f"there are {days[i]} days in {i}")
