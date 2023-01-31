# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar as cl

day_lst = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

year = int(input('연도를 입력하시오 : '))

if (year % 4 == 0)  and (year % 100 != 0) or (year % 400 == 0):
    year = int(input('입력하신 연도는 윤년입니다. 연도를 다시 입력하시오 : '))
else:
    print(cl.calendar(year))

month = int(input('월을 입력하시오 : '))
if month > 12 or month < 1:
    month = int(input('월을 다시 입력하시오 : '))

date = int(input('일을 입력하시오 : '))
if date > 31 or month < 1:
    date = int(input('일을 다시 입력하시오 : '))

if cl.weekday(year, month, date) == cl.MONDAY:
    print('경고 월요일입니다.')

real_day = day_lst[int(cl.weekday(year, month, date))]

keys_dict = ['년', '월', '일', '요일']
vals_dict = [str(year), str(month), str(date), str(real_day)]

dict_input_cal = dict(zip(keys_dict, vals_dict))
print(dict_input_cal)
