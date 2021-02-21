import math
import random

class Coronavirus:
	def __init__(self,temperature):
		self.temperature = temperature

	def check_coronavirus(self):
		res = math.pi * temperature
		print(res)
		if math.ceil(res)-res > 0.5:
			res = math.ceil(res)
			print(res)
		else:
			res = int(res)	

		if 120<=res<=128:
			return "You have coronavirus"
		else:
			return "Everything is ok"		
temperature = float(input(" your body temperature by Celsus: "))
a = Coronavirus(temperature)
print(a.check_coronavirus())



class WidespreadName:
	def __init__(self,name):
		self.name = name
	def check_Widespread(self):
		myDict = {
			1 : "ajs",
			2 : "bkt",
			3 :	"clu",
			4 : "dmv",
			5 : "enw",
			6 :	"fox",
			7 : "gpy",
			8 : "hqz",
			9 : "ir"

		}
		count = 0

		for i in name:
	 		for k,v in myDict.items():
	 			if i in v:
	 				count += k
		if count**0.5 < 5:
			return f"{count} no" 
		else:
			return f"{count} yes" 		



name = input("write your name: ").lower()
a = WidespreadName(name)
print(a.check_Widespread())




import random
class MyClass:

    def __init__(self, magic_words):
        self.magic_words = magic_words

    def game(self):
        count_Harry = 0
        count_Voldemort = 0
        while True:
            LordVoldemort = random.choice(magic_words)
            print("LordVoldemort: ",LordVoldemort)
            HarryPotter = input("HarryPotter: ")
            if LordVoldemort == HarryPotter:
                count_Harry += 1
                print("HarryPotter - ", count_Harry)
                print("LordVoldemort - ", count_Voldemort)
                if count_Harry == 2:
                    print("Win Harry Potter")
                    break
            else:
                count_Voldemort += 1
                print("HarryPotter - ", count_Harry)
                print("LordVoldemort - ", count_Voldemort)
                if count_Voldemort == 2:
                    print("Win Lord Voldemort ")
                    break


magic_words = ("Avada Kedavra", "Crucio", "Imperio")
a = MyClass(magic_words)
a.game()
