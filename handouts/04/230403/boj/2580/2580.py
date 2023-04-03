import sys
sys.stdin = open('input.txt', 'r')


def is_promising(i,j):
    promising = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if arr[i][k] in promising:
            promising.remove(arr[i][k])
        if arr[k][j] in promising:
            promising.remove(arr[k][j])
    
    i//=3
    j//=3

    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if arr[p][q] in promising:
                promising.remove(arr[p][q])
    
    return promising

flag = False

def dfs(n):
    global flag

    if flag:
        return
    
    if n==len(zeros):
        for row in arr:
            print(*row)
        flag = True
        return
    
    else:
        (i,j)=zeros[n]
        promising = is_promising(i,j)
        for num in promising:
            arr[i][j]=num
            dfs(n+1)
            arr[i][j]=0



arr = [list(map(int,input().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if arr[i][j]==0]
dfs(0)