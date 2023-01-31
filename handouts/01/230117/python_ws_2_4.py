# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

price_steak = int(50000)
VAT = int(50000 * 15/100)
overall = int(price_steak + VAT)

print(f'스테이크 {price_steak}\nVAT {VAT}\n총계 {overall}')
