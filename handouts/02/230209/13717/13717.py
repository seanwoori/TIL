import sys
sys.stdin = open('input.txt', 'r')

def isin(a, b):
    clk=i=0
    while i<=(len(a)-len(b)+1):
        if a[i:i+len(b)]==b:
            clk+=1
            i+=len(b)
        else:
            i+=1
    ans = len(a)-(len(b)-1)*clk
    return ans

T = int(input())
for tc in range(1, 1+T):
    a, b = map(str, input().split())
    print(f'#{tc} {isin(a, b)}')