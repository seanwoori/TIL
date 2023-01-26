# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    if position[0] == 0:
        if M == 0:
            return False
        elif position[1] == 0: 
            if M == 2:
                return False
        elif position[1] == (N-1):
            if M == 3:
                return False
    else:
        return True


    if position[0] == (N-1):
        if M == 1:
            return False
        elif position[1] == 0:
            if M == 2:
                return False
        elif position[1] == (N-1):
            if M == 3:
                return False
    else:
        return True

    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
