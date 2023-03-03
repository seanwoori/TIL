import sys
sys.stdin = open('input.txt', 'r')

N=int(input())
ans=''
T=N%3
if N//3%2 == 0:
    if T == 0 or T == 2:
        ans='CY'
    else:
        ans='SK'
else:
    if T==0 or T==2:
        ans="SK"
    else:
        ans="CY"
print(ans)
