import sys
sys.stdin = open('input.txt', 'r')

# 별 갯수 다르면 별이 많은쪽이 이김
# 별 갯수 같고 동그라미 많은쪽 이김
# 별 동그라미 네모 많은쪽 이김
# 별 동그라미 네모, 세모 많은쪽 이김
# 무승부
# 별 동그 네모 세모 4 3 2 1
N=int(input())
for _ in range(N):
    alst=list(map(int,input().split()))
    aclst=[0,0,0,0]
    alst.pop(0)
    blst = list(map(int, input().split()))
    bclst=[0,0,0,0]
    blst.pop(0)

    for num in alst:
        aclst[num-1]+=1
    for num in blst:
        bclst[num-1]+=1

    for i in range(len(aclst))[::-1]:
        if aclst[i]>bclst[i]:
            print('A')
            break
        elif aclst[i]<bclst[i]:
            print('B')
            break
    else:
        print('D')
