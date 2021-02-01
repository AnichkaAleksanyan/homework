import json

def myFunc(file_name,names,marks):
	myDict = {}
	leng = len(names)
	for i in range(leng):
		myDict[names[i]]=marks[i]
	try:
		file = open(file_name)
		return json.load(file)
	except FileNotFoundError:
		file = open(file_name,"w")
		json.dump(myDict,file)
		return "File created"
				



file_name= "myDict.json"
names = ["Ani","Jessi","Ben"]
marks = [1,2,3]
print(myFunc(file_name,names,marks))




def song(file_name,author,word_song):
	mySong={author:word_song}
	try:
		with open(file_name) as file:
			return json.load(file)
	except FileNotFoundError:
		with open(file_name, "w") as file:
			json.dump(mySong,file)	
			return "file created"

file_name = "my_song.json"
author= "Song"		
word_song = "word song"		

print(song(file_name,author,word_song))



def res(file_name,number):
	Sum = 0
	for i in range(number+1):
		if i%3==0 or i%5==0:
			Sum+=i
	try:
		with open(file_name) as file:
			return json.load(file)
	except FileNotFoundError:
		with open(file_name, "w") as file:
			json.dump(Sum,file)	
			return "file created"

file_name = "Sum.json"
number = int(input("number: "))

print(res(file_name,number))






def MyFunkc(file_name,word):

	word = word.lower()
	vowel_letter = "aeiouy"
	count = 0
	for i in word:
		if i in vowel_letter:
			count+=1
	try:
		file = open(file_name)
		return json.load(file)
	except FileNotFoundError:
		file = open(file_name,"w")
		json.dump(count,file)
		return "file created"			

word = input("write word ")
file_name= "vowel_letter.json"
print(MyFunkc(file_name,word))





def myFunk(file_name,text):

	text = text.split(" ")
	count = 0
	myDict={}

	for i in text:
		count=0
		for j in text:
			if j==i:
				count+=1
		myDict[i]=count
	try:
		file = open(file_name)
		return json.load(file)
	except FileNotFoundError:
		file = open(file_name,"w")
		json.dump(myDict,file,indent = 4)
		return "file created"

text = "Another pause and more eying and siding around each other"
file_name= "Dictionary.json"

print(myFunk(file_name,text))






def myFunkc(file_name,my_list):

	
	newlist=[]
	for i in my_list:
		if i not in newlist:
			newlist.append(i)
	try:
		file = open(file_name)
		return json.load(file)
	except FileNotFoundError:
		file = open(file_name,"w")
		json.dump(newlist,file)
		return "file created"
my_list = ["a","b","c","a","b"]
file_name = "newlist.json"
print(myFunkc(file_name,my_list))




def count_upper_lower(file):

	Upper = 0
	Lower = 0	
	for row in file:
		for i in row:
			if i.islower():
				Lower+=1
			elif i.isupper():
				Upper+=1	
	return Lower,Upper			
file=open("Story.txt")
print(count_upper_lower(file))