class Max:

	def __init__(self,myList):
		self.myList = myList
	

	def get_max_dif(self):
		newList = [myList[i]-myList[i+1] for i in range(len(myList)-1)]
		return max(newList)	

myList = [2, 4, 1, 0]
a = Max(myList)
print(a.get_max_dif())