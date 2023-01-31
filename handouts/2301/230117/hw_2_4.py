orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_lst = list(map(str, orders.split(',')))
orders_lst.sort(reverse = True)

overlap_rm_lst = list(set(orders_lst))

count_ice = 0
count_cups_lst = []

for char in orders_lst:
    count_cups = 1
    if '아이스' in char:
        count_ice += 1

for char_rm in overlap_rm_lst:
    init_cups = 0
    for char_orgin in orders_lst:
        if char_rm == char_orgin:
            init_cups += 1
    else:
        count_cups_lst.append(init_cups)

cups_per_menu = dict(zip(overlap_rm_lst, count_cups_lst))

print(f'아이스 메뉴는 총 {count_ice}잔 입니다.')

for keys, values in cups_per_menu.items():
    print(f'메뉴 {keys} {values}잔의 주문이 들어왔습니다.')



