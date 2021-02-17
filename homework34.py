# Ticket numbers usually consist of an even number of digits.A ticket number is
# considered lucky if the sum of the first half of the digits is equal to the sum of the
# second half.Given a ticket numb
# 

class Lucky_Ticket:
	def __init__(self,ticket):
		self.ticket=ticket

	def check_lucky(self):
		while True:
			# ticket = input("number of ticket: ")
		    if len(ticket) > 4 or len(ticket) < 4 :
		        print("Pleas write 4 numbere")
		        continue
		    elif not ticket.isdigit():
		        print("Pleas enter only numbers")
		        # continue

		    first = ticket[:2]
		    second = ticket[2:]

		    res = int(first[0]) + int(first[1]) == int(second[0]) + int(second[1])
		    return res
		    break		

ticket = input("number of ticket: ")
a = Lucky_Ticket(ticket)
print(a.check_lucky())
		    


# 6. List sort
# Create a class: Some people are standing in a row in a park. There are trees
# between them which cannot be moved. Your task is to rearrange the people by
# their heights in a non-descending order without moving the trees. People can be
# very tall!

class Sort_list:
	def __init__(self,old_list):
		self.old_list = old_list

	def myFunc(self):

		new_list = [i for i in old_list if i !=-1 ]
		new_list.sort()

		for i in range(len(old_list)):
		    if old_list[i] == -1:
		        new_list.insert(i,-1)
		return new_list
old_list =  [-1, 150, 190, 170, -1, -1, 160, 180]
a = Sort_list(old_list)		
print(a.myFunc())


# 7. Weight
# Several people are standing in a row and need to be divided into two teams. The
# first person goes into team 1, the second goes into team 2, the third goes into
# team 1 again, the fourth into team 2, and so on.You are given an array of positive
# integers - the weights of the people. Return an array of two integers, where the
# first element is the total weight of team 1, and the second element is the total
# weight of team 2 after the division is complete.


class Weight:
	def __init__(self,List):
		self.List = List
	def MyFunc(self):
		b = [a[i] for i in range(0,len(a),2)]
		c = [a[i] for i in range(1,len(a),2)]
		return [sum(b),sum(c)]
		return 
a = [50, 60, 60, 45, 70]
d = Weight(a)
print(d.MyFunc())