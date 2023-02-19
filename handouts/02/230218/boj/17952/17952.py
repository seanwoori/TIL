import sys
sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline
N = int(input())
# 1 A T : 과제의 만점 A, 해결하는데 T분, A와 T는 모두 정수임.
# [1] stk에 처음 원소는 과제점수를, 이후에는 (시간-2)만큼 0을 append.
# [0] 해당 시점에는 과제가 주어지지 않음.
# 이후 sm에 stk.pop()으로 나온 점수들을 모두 더해줄 것임.
sm=0
stk=[]
clst=[]
for _ in range(N):
    st = input().split()
    # 만약 st에 원소 하나 apppend 되어있다면, 시간+=1하고 다음줄 계속 진행.
    # 만약 stk가 빈 리스트라면, pass.
    if len(st)==1:
        if stk:
            # stk의 가장 끝에 저장된 원소가 int면, 정답에 바로 더해줌.
            if type(stk[-1])==int:
                sm+=stk.pop()
            # stk에 저장된 원소가 str이면, count므로 -1해줌.
            # 이후 stk[-1] 0보다 같거나 작으면 count stk.pop()
            # 그리고 그 다음 있는 과제 점수 정답에 append
            # stk[-1]이 0보다 크면 -1을 뺀 int형 원소를 str로 저장.
            elif type(stk[-1])==str:
                stk[-1]=int(stk[-1])-1
                if int(stk[-1])<=0:
                    stk.pop()
                    sm+=stk.pop()
                else:
                    stk[-1]=str(stk[-1])
        else:
            pass
    else:
        # stk 처음에 과제 점수 append.
        # 이후 (시간-1)만큼 0을 append, 받자마자 바로 시작하였으므로.
        # 하지만 시간만큼 0을 append하면 메모리 초과 문제 발생!
        # 0을 append 하지말고, 깔끔하게 해결할 방법 없을까?
        # stk에 과제 점수는 int로, 시간은 str로 저장.
        # 너무 하드코딩이긴한데, 생각하기 귀찮다.
        # 시간이 1인 경우, stk에 append 하지않고 바로 sm에 점수를 더함.
        if int(st[2])>2:
            stk.append(int(st[1]))
            stk.append(str((int(st[2])-1)))
        elif int(st[2])==2:
            stk.append(int(st[1]))
        else:
            sm+=int(st[1])

print(sm)