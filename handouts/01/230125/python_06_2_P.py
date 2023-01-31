grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]


price_lst = []

for i in range(len(grain_lst)):
    price_lst.append(grain_lst[i][1])
    
max_price = max(price_lst)

for val in range(len(grain_lst)):
    if grain_lst[val][1] == max_price:
        print(f'가장 높은 가격을 가진 작물은 {grain_lst[val][0]}입니다.')

