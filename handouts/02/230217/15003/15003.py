import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    st = input()
    # 처음부터 loop를 돌자.
    # 1이 등장하는 시기 => cnt +=1
    # 그리고 등장하는 1은 pass 해야함.
    # 따라서 flag를 통해 이를 판별하고자 함.
    # if 이후 다시 0이 나오면, => cnt += 1
    # else: pass
    cnt = 0
    flag = False

    for char in st:
        if char == '1' and not flag:
            flag = True
            cnt+=1
        elif char=='1' and flag:
            pass
        elif char=='0' and flag:
            cnt+=1
            flag = False
        elif char=='0' and not flag:
            pass

    print(f'#{tc} {cnt}')