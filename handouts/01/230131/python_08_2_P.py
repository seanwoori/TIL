class Person:
    name = ''
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def get_age(self, name_inp, birth_year_inp):
        self.name = name_inp
        self.age = 2023 - birth_year_inp 
        return Person(self.name, self.age)
    
    '''
    @classmethod
    def get_age(cls, name_inp, birth_year_inp):
        cls.name = name_inp
        cls.age = 2023 - birth_year_inp
        return Person(cls.name, cls.age)
   '''
   
    def check_age(self):
        if self.age <= 19:
            return True
        else:
            return False




#Driver's code
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)


print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())

