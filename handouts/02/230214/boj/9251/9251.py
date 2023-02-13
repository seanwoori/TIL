import sys
sys.stdin = open('input.txt', 'r')

st1 = input() # 길이 짧거나 같은
st2 = input() # 길이 길거나 같은

l1 = len(st1)
l2 = len(st2)

mat = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if st1[i-1]==st2[j-1]:
            mat[i][j] = mat[i-1][j-1]+1
        else:
            mat[i][j]=max(mat[i-1][j], mat[i][j-1])

print(mat[-1][-1])