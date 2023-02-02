class PublicTransport:
    def __init__(self, name, fare):
        self.name = name
        self.fare = int(fare)
        self.passenger = 0

    def get_in(self, num_in):
        self.passenger += int(num_in)
        return self.passenger
        
    def get_off(self, num_off):
        self.passenger -= int(num_off)
        return self.passenger
    
    def overall_pass(self):
        self.inpass = input('들어온 승객의 수를 입력하세요: ')
        self.offpass = input('나간 승객의 수를 입력하세요 : ')
        return self.get_in(self.inpass) - self.get_off(self.offpass)
    
    def profit(self):
        print(f'총 수익은 {self.fare * self.overall_pass()}원 입니다.')

class Bus(PublicTransport):
    def __init__(self, name, fare):
        super().__init__(name, fare)


pt = Bus('버스', 500)
pt.profit()