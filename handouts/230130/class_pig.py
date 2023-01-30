class Pig:
    belly_price = 1000 # 클래스 변수
    stock = 10000
    def __init__(self, stock):
        self.stock = stock

    # 주문이 들어왔을 때의 가격 -> 메서드
    def order_price(self, amount):
        if self.stock >= amount:
            return self.belly_price * amount

        else:
            return "재고가 없어요."
            # return f"재고가 {self.stock}만큼 있습니다"
        

    def order(self, amount, money):
        
        price = self.order_price(amount)
        if price <= money:
            self.stock = self.stock - amount
            change = money - price
            return change
        else: 
            return '못삼'
        
    def sale_price(self, perc, amount):
        prc = self.order_price(amount)
        sale_prc = prc * (100-perc) / 100
        return sale_prc, prc 


    @staticmethod
    def func(cls, *args):
        pass

a_pig = Pig(100)
b_pig = Pig(150)
# print(a_pig.belly_price)
# print(b_pig.belly_price)

b_pig.belly_price = 500
# print(a_pig.belly_price)
# print(b_pig.belly_price)

print(a_pig.stock)
print(a_pig.order(50, 10000000))
print(a_pig.stock)
print(b_pig.stock)
# print(a_pig.order_price(150))


# b 돼지의 가격이 20% 할인됨
# b 돼지에서 원래 가격도 접근 가능함
# b 돼지를 50만큼 샀을 때, 원래 가격, 할인된 가격 둘다 반환.
print(f'원래가격은?: ')
print(b_pig.sale_price(20, 50))