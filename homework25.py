file1 = open("file1.txt","x")
file1.write("Hello my name is Ani")


file2 = open("file2.txt","w")
file2.write("I em from Yerevan")

file3 = open("file3.txt")
print(file3.read())


file4 = open("file4.txt")
print(file4.read())


file5 = open("file5.txt")
print(file5.read())



file = open("file1.txt")
for row in file:
	print(row)


file = open("file1.txt")
for i in range(2):
	print(file.readline())


file = open("file1.txt","a")
file.write("123456789")



file = open("file4.txt")
c = file.read().split(" ")
print(c)
maxLen = c[0]
for i in c:
	if len(i) > len(maxLen):
		maxLen=i
print(i)		



file = open("file4.txt")
for row in file:
	for i in row:
		if i.isdigit():
			print(i)



file = open("password.txt","w")
login = input("Write your login: ")
password = input("Write your password: ")
a = login + " " +password
file.write(a)
print(file.read)
file.close()


with open("password.txt","w") as file:
	login = input("Write your login: ")
	password = input("Write your password: ")
	a = login + " " +password
	file.write(a)

with open ("password.txt") as file:
	print(file.read())
