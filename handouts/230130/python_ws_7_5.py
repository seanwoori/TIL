import random



class ClassHelper:
    
    def __init__(self, *args):
        self.name_lst = []
        for name in args:
            self.name_lst.append(name)
        self.name_lst = self.name_lst[0]
        
    def shuffle(self):
        random.shuffle(self.name_lst)
        return self.name_lst
        #return self.temp
    
    def pick(self, n):  
        return self.shuffle()[:n]
    
    def match_pair(self):
        self.rslt_lst = []
        
        while True:    
            self.temp_lst = []
            
            if (len(self.shuffle()) == 3):
                for i in range(3):
                    self.temp_lst.append(self.shuffle().pop(0))
                self.rslt_lst.append(self.temp_lst)
                break
            
            if (len(self.shuffle()) == 0):
                break

            for j in range(2):
                self.temp_lst.append(self.shuffle().pop(0))    
            
            self.rslt_lst.append(self.temp_lst)
        
        return self.rslt_lst
                


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])


print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
