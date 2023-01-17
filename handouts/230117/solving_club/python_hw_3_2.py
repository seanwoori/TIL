year = 400

yoon = False

def print_yoon(n):
    if n == True:
        print('윤년입니다.')
    else:
        print('윤년이 아닙니다.')

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    yoon = True
else:
    yoon = False

print_yoon(yoon)