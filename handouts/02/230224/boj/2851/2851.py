import sys
sys.stdin = open('input.txt', 'r')
lst=[]
for _ in range(10):
    lst.append(int(input()))
N=len(lst)
ans=0
a=[abs(lst[0]-100)]
for i in range(1,N+1):
    temp=lst[:i]
    if abs(sum(temp)-100)<=a[i-1]:
        ans=sum(temp)
        a.append(abs(sum(temp)-100))
    else:
        break
print(ans)