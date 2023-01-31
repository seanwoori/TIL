class CarSharing:
    
    def __init__(self, time, dist):
        self.time = time
        self.dist = dist

    def fee_share(self):
        fee_sh = self.time // 10 * 1200
        return fee_sh 
    
    def insurance(self):
        fee_in = 0
        fee_in = self.time // 30 * 525
        if ((self.time // 30 % 2) == 1) and ((self.time % 30) >= 20):
            fee_in += 525
        return fee_in
    
    def drv_fee(self):
        if self.dist > 100:
            fee_drv = 100 * 170
            fee_drv += (self.dist - 100) * 85
        else:
            fee_drv = self.dist * 170
        return fee_drv

    def result(self):
        return self.fee_share() + self.insurance() + self.drv_fee()

'''
def fee(time, dist):
    a = CarSharing(time, dist)
    print(a.result())
'''

class fee(CarSharing):
    
    def __init__(self, time, dist):
        super().__init__(time, dist)
        #self.time = time
        #self.dist = dist
        print(self.result())
#__init__(self)는 무조건 하나의 변수를 받아야 하나?



fee(600, 50) #=> 91000
fee(600, 110) #=> 10
