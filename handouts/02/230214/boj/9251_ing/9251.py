import sys
sys.stdin = open('input.txt', 'r')

def isin(st1, st2):
    n = len(st1)
    for i in range(1,n+1)[::-1]: # st1의 길이 인덱스 i, n부터 1까지
        for j in range(n-i+1): # st1의 위치 인덱스 j, 0부터 n-i+1까지
            if st1[j:j+i] in st2:
                return i

st1 = input() # 길이 짧거나 같은
st2 = input() # 길이 길거나 같은

if len(st1)>len(st2):
    st1, st2 = st2, st1

print(isin(st1, st2))