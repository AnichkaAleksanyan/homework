# Write a python class to find max, min num and
# and sum in your list:

class MyClass:

	def Max(self,my_list):
		maximum = my_list[0]
		for i in my_list:
			if i > maximum:
				maximum = i
		return maximum		

	def Min(self,my_list):
		minimum = my_list[0]
		for i in my_list:
			if i < minimum:
				minimum = i
		return minimum

	def Sum(self,my_list):
		res = 0
		for i in my_list:
			res+=i
		return res	
a = MyClass()
print(a.Max([10,20,30]))
print(a.Min([10,20,30]))
print(a.Sum([10,20,30]))



# Write a python class to find two highest values in
# your dict:

class highest_value:

	def get_highest_value(self,hight):
		res = max(hight.values())
		return res
hight = {
	"Aram" : 156,
	"Ani": 120,
	"Arev":135
	}
a = highest_value()
print(a.get_highest_value(hight))




# Write a python class where your child class takes
# all methods in parent class and print them.


class Person:
	def __init__(self,firstname,lastname):
		self.firstname = firstname
		self.lastname = lastname

	def print_info(self):
		print(self.firstname,self.lastname)

	def count_age(self,year_birth):
		age = 2021-year_birth
		return age	

class Doctor(Person):
	pass


p = Person("Petros","Petrosyan")
d = Doctor("Petros","Petrosyan")
print(d.count_age(1992))
d.print_info()


# Write a Python class named Rectangle
# constructed by a length and width and a method
# which will compute the area of a rectangle


class Rectangle:
	def __init__(self,lenght,width):
		self.lenght = lenght
		self.width = width
	def count_area(self):
		area = lenght*width
		return area

lenght = int(input(""))
width = int(input(""))
a = Rectangle(lenght,width)	
print(a.count_area())	


	