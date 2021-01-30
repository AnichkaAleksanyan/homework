import json
myDict = [{
	"name":"Ani",
	"surname":"Aleksanyan",
	"age":28,
	"phone":"456122123"

}]

with open("about_me.json","w") as file:
	json.dump(myDict,file)


file = open("about_me.json")
a = json.load(file)
for i in a:
	print(i)


name = input("name")
if i["name"]== name:
	print(name, " in my dict")	
else:
	print(name,"not in my dict")	