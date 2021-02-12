 # 2 Create a class for Car and Person

class Person:
	def __init__(self,name,surname,year_of_birth):
		self.name = name
		self.surname = surname
		self.year_of_birth = year_of_birth
	def print__info(self):
		print(p1.name,p1.surname,p1.year_of_birth)	

p1 = Person("Petros","Petrosyan",1990)	


class Car:
	def __init__(self,model,engine,color):
		self.model = model
		self.engine = engine
		self.color = color
	def print__info(self):
	print(c1.model.c1.engine,c1.color)	
c1 = Car("BMW",2,"red")	



#1 calculyator
class calculyator:
	def __init__(self,x,choice,y):
		self.x = x
		self.choice = choice
		self.y = y
	def gorcoxutyun(self):
		if choice == "+":
			return res.x+res.y
		elif choice == "-":
			return res.x-res.y
		elif choice == "*":
			return res.x*res.y
		elif choice == "/":
			return res.x/res.y			

while True:
	try:
		x = float(input("x:"))
		break
	except ValueError:
		print("pleas write number")	

characters = "+,-,/,*"
while True:
	choice =input("choice:")
	if choice in characters:
		break
	print("Pleas enter ",characters)

while True:
	try:
		y = float(input("y:"))
		if y == 0 and choice == "/":
			raise ZeroDivisionError
		break
	except ValueError:
		print("pleas write number")		
	except ZeroDivisionError:
		print("Don't divaice 0")	


res = calculyator(x,choice,y)
print(res.gorcoxutyun())			



#3 Change.
# Create a class Change:You have 3 methods
# in your class:
# Usd --- Eur
# Usd --- Amd
# Usd --- Ru


class Change:
	def __init__(self,many,currency):
		self.many = many
		self.currency = currency

	def Euro(self):
		return res.many*0.83
	def Amd(self):
		return res.many*524
	def Rub(self):
		return res.many*74

while True:
	try:
		many = float(input("USD= " ))
		break
	except ValueError:
		print("pleas write many in numbers")

while True:
	my_currency = ("euro","amd","rub")
	currency = input("currency ").lower()
	if currency in my_currency:
		break
	print("Pleas enter only",my_currency)			

res = Change(many,currency)
if currency == "euro":
	print(res.Euro())
elif currency == "amd":
	print(res.Amd())
if currency == "rub":
	print(res.Rub())

