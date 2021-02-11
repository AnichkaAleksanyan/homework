"""1. Odd
Write a recursive function to determine whether all
digits of the number are odd or not.
Input Output
"""
def odd_num(n):
	
	for i in n:
		if int(i)%2==1:
			return True
		else:
			return False	

try:
	n = input()
	print(odd_num(n))
except ValueError:
	print("pleas write number")	
	n = input()
	print(odd_num(n))


"""2. Threading
Write a python function all even number in
10.000 use threading and print time."""


import threading
import time


def zuyg(file_name,start,end):
	with open(file_name, "a") as file:
		for i in range(start,end +1)[start:end]:
			if i%2 ==0:
				file.write(str(i))

	
t1 = threading.Thread(target = zuyg, args=("zuyger.txt",1,3500))							
t2 = threading.Thread(target = zuyg, args=("zuyger.txt",3501,7000))							
t3 = threading.Thread(target = zuyg, args=("zuyger.txt",7001,10000))	

Strat = time.time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

End = time.time()
print(Strat-End)



'''3. Numbers
Given N number. Write a recursive function that
should print from 1 to N numbers.
Input Output
5 1, 2, 3, 4, 5'''



def num(n):
	a = [i for i in range(n+1)]
	return a
n = int(input("number "))	
print(num(n))	


'''4. Longest Word
Write a python program to find the longest word from the file content.Need to use
<try-except> block in the file reading process and print time. example:'''



def find_long_word(file_name):
	try: 
		with open(file_name) as f:
			f = f.split(" ")
		return max(f)	
	except FileNotFoundError:
		with open(file_name,"w") as f:
			f.write("Hello my name is Ani")
	

file_name = "text.txt"
print("The longest word is",find_long_word(file_name))