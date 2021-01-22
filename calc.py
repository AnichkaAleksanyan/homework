
def	getX():
	try:
		global x
		x = int(input("x="))
	except ValueError:
		print("Write only number")
		getX()
getX()
def getChar():
	try:
		global char		 	
		char = input("char=")
		if not char in "+-*/":
			raise ValueError("Please Write only +-*/")

	except ValueError:
		print("Write only +-*/ characters")	
		getChar()
getChar()
def getY():				
	try:
		global y
		y = int(input("y="))
	except ValueError:
		print("Write only number")
		getY()	
getY()
def res(x,char,y):
	if char == "+":
		return x+y
	elif char == "-":
		return x-y
	elif char == "/":
		return x/y
	elif char == "*":
		return x*y
try:
	print(res(x,char,y))			
except ZeroDivisionError:
	print("don't divice 0")

