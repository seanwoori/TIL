# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    lst_num = list(numbers)
    if len(lst_num) == 1:
        return 3.14 * int(lst_num[0]) ** 2
    elif len(numbers) == 2:
        if sum(lst_num) % 2 == 1:
            return int(lst_num[0]) * int(lst_num[1]) / 2
        elif sum(lst_num) % 2 == 0:
            return int(lst_num[0]) * int(lst_num[1])
    elif len(numbers) >= 3:
        sum_lst = sum(lst_num)
        avg_lst = sum_lst / len(lst_num)
        return (sum_lst, avg_lst,)
    else:
        return 0
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0