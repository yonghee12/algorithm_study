year = int(input())

def func(year):
    if year%4 == 0 and year%100 != 0:
        return 'yes'
    elif year%400 == 0:
        return 'yes'
    else:
        return 'no'

print(func(year))