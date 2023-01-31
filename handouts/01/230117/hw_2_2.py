orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_lst = list(map(str, orders.split(',')))
total_cups = int(len(orders_lst))

overlap_rm_lst = list(set(orders_lst))
overlap_rm_lst.sort(reverse = True)

print(f'총 주문 잔 수는 {total_cups}이며, 중복 주문을 제외한 리스트는 {overlap_rm_lst}입니다.')
