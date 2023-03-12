def change(now, to):
    l=now[:]
    press=0
    for i in range(1,N):
        if l[i-1]==to[i-1]:
            continue
        press+=1
        for j in range(i-1,i+2):
            if j<N:
                l[j]=1-l[j]
    return press if l==to else 1e9

N=int(input())
now = list(map(int, input()))
to = list(map(int, input()))

ans=change(now,to)
now[0]=1-now[0]
now[1]=1-now[1]
ans=min(ans,change(now,to)+1)
print(ans if ans!=1e9 else -1)