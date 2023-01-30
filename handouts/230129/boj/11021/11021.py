test_num = int(input())

for num in range(1, test_num+1):
    a, b = map(int, input().split())
    result = a+b

    print(f'Case #{num}: {a} + {b} = {result}')