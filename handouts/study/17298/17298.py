import sys
sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
# 2
'''
clst=lst[:]
dct={}
# for loop 2개 O(n^2) => 시간초과
# pointer는 다음 원소를 가리키는 인덱스
# cnt==len(lst) ~ while문 break
cnt=0 # dictionary에 값을 저장한 횟수. cnt==len(lst)일때 while문 break
ipt=0 # 초기값 인덱스
npt=0 # 비교 인덱스
while cnt<=len(lst):
    # 초기원소는 clst의 pointer 인덱스
    # npt는 init과 비교할 값을 훑는 인덱스, npt의 범위는 len(clst)-1
    # [1] clst[ipt]가 clst[npt] 보다 작으면,
    # dct저장. dct[clst[ipt]]=clst.pop(npt)
    # 초기값 인덱스를 비교 인덱스로 갱신. ipt=npt
    # 이후 npt+=1하면서 clst[ipt]와 비교
    # 시간초과 !!!!!!!!!!!!!!!!!!!
    # O(n)으로 어떻게 짜지??
    if len(clst)<=1:
        dct[clst.pop()]=-1
        cnt+=1
        break
    else:
        npt+=1

    if npt>(len(clst)-1):
        if clst:
            if not ipt:
                dct[clst.pop(ipt)]=-1
            else:
                dct[clst[ipt]]=-1
            cnt+=1
            ipt=0
            npt=ipt
        else:
            break
    elif clst[ipt]<clst[npt]:
        if clst:
            dct[clst.pop(ipt)]=clst[npt]
            cnt+=1
            npt-=1
            ipt=npt
        else:
            break
for num in lst:
    print(dct[num], end=' ')
'''

# 3
ans=[-1]*N
stk=[0]

for i in range(1,N):
    while stk and lst[stk[-1]]<lst[i]:
        ans[stk.pop()]=lst[i]
    stk.append(i)
print(*ans)
