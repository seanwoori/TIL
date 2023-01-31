str_lst = input('문자열을 입력하세요. : ')
str_lst_space = list(map(str, str_lst.split()))
count = 0

for idx, char in enumerate(str_lst_space):
    if idx == len(str_lst_space) - 1:
        break
    if str_lst_space[idx][-1] == str_lst_space[idx+1][0]:
        count += 1
        if count == len(str_lst_space) - 1:
            print('pass')
    else:
        print('fail')
        break
