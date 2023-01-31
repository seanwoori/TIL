class Creature:
	def __init__(self):
		self.hp = 0
		self.attack = 0
		self.defence = 0

	def attack_target(self, target):
		print(f"{self} attack {target}")
		damage = self.attack - target.defence
		target.hp -= damage if self.attack > target.defence else 1
		if target.hp <= 0:
			print(f"Oh, {target} is down! I repeat. {target} is down!")
		else:
			print(f"{target}'s hp: {target.hp}")


class Hero(Creature):
	def __init__(self):
		super().__init__() # 부모의 클래스를 상속받을 때 super().__init__()을 사용함. 본 형식은 super(class이름, self).__init__(). 상속받는 클래스의 괄호 안에는 상속하는 부모 클래스의 이름이 들어가 있어야함.
		self.hp = 150
		self.attack = 10
		self.defence = 10

	def __str__(self):
		return "Hero"

	def set_magic_power(self):
		# set the Hero Status(hp, attack, deffence)
		self.hp = 150
		self.attack = 600
		self.defence = 40
	

class Dragon(Creature):
	def __init__(self):
		super().__init__()
		self.hp = 1000
		self.attack = 50
		self.defence = 100

	def __str__(self):
		return "Dragon"


hero = Hero()
hero.set_magic_power()
dragon = Dragon()
while (hero.hp > 0) and (dragon.hp > 0):
	hero.attack_target(dragon)
	if dragon.hp > 0:
		dragon.attack_target(hero)
