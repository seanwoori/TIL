a = 3
b = 6
c = -5

result_pos = (-b + (b ** 2 - 4* a*c) ** (1/2))/(2*a)
result_neg = (-b - (b ** 2 - 4* a*c) ** (1/2))/(2*a)
answer = (result_pos, result_neg)

print(answer)