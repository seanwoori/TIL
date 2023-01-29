import datetime
now = datetime.datetime.now()
current_time = now.strftime(f'%Y-%m-%d')
print(current_time)
#print(f'{now.year}-{now.month}-{now.day}')