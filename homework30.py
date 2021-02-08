def my_funktion(a,b,step):
	my_list = []
	if step>0:
		for i in range(a,b+1,step):
			my_list.append(i)
	else:
		for i in range(b,a-1,step):
			my_list.append(i)
	return my_list

a = 1
b = 5
step = 1	
print(my_funktion(a,b,step))		



def my_funktion(old_list):
	new_list = []
	for i in range(len(old_list)-1):
		j =old_list[i]*old_list[i+1] 
		new_list.append(j)
	return new_list
old_list = [3,7,12,5,20,0]
print(my_funktion(old_list))	



def my_funk(text, my_list):
	text = text.split(" ")
	n= 0
	for i in range(len(text)):
		if text[i] == "_":
			text[i]=my_list[n]
			n+=1
	text = " ".join(text)
	return text	
text = "_ we have a _"	
my_list = ["Hyuston","problem"]		
print(my_funk(text, my_list))




def my_funk(my_list):
	new_list = []
	for i in my_list:
		new_list.append(len(i))
	a = max(new_list)
	b = min(new_list)	
	return a + b
my_list = ["anymor", "raven", "me","communicate"]	
print(my_funk(my_list))	



def my_funk(my_list,search):

	if search in my_list:
		return my_list.index(search)
	else:
		res = []
		for i in my_list:
			c = abs(search - i)
			res.append(c)

		return res.index(min(res))		
				


my_list =[35,113,143,12,-123,15]
search = 12
print(my_funk(my_list,search))




def creat_dict(n):
	my_dict = {}
	for i in range(1,n+1):
		my_dict[i]=i**2
	return my_dict

n = int(input())
print(creat_dict(n))




my_list = []
new_dict = {}
def invert_dict(my_dict):
	for i,j in my_dict.items():
		i,j = j,i
		my_list.append([i,j])
	for a in my_list:
		if a[0] in new_dict.keys():
			new_dict[a[0]]=[new_dict[a[0]],a[1]]
		else:
			new_dict[a[0]]=a[1]	
	return new_dict

my_dict = {
	1:"one",
	2:"two",
	3:"tree",
	4:"two",
	5:"tree"
}		
print(invert_dict(my_dict))



def fibonachi(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonachi(n-1)+fibonachi(n-2)
print(fibonachi(3))				