import sys
sys.stdin = open('input.txt', 'r')

st=list(map(str, input()))
N=len(st)
lst=[]
ans=''
C=1
R=N
if N<=2:
    ans=st
else:
    for r in range(1,N+1)[::-1]:
        if not N%r:
            c=N//r
            if c>r:
                break
            elif c>C:
                C,R=c,r

    # 행이 R개이고 열이 C개인 행렬
    arr=[['']*C for _ in range(R)]
    for ch in st:
        for i in range(R):
            for j in range(C):
                arr[i][j]=st.pop(0)
    garr=list(zip(*arr))
    for l in garr:
        for ch in l:
            ans+=ch
print(ans)
