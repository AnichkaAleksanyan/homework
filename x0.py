import random 
all_steps = [1,2,3,4,5,6,7,8,9]
steps = []
win = True

print('       Hi you play Tic Tac Toe ')
print('')

def start(firstplayer):

	if firstplayer == 'pc':
		return 'pc'
	else:
		return "user"	


def print_tablo():
	print('')
	print('')
	print('     ',all_steps[0],'|',all_steps[1],'|',all_steps[2],' ')
	print('     --- --- --- ')
	print('     ',all_steps[3],'|',all_steps[4],'|',all_steps[5],'')
	print('     --- --- --- ')
	print('     ',all_steps[6],'|',all_steps[7],'|',all_steps[8],' ')
	print('')
	print('')



def win():

	if all_steps[:3]==["x","x","x"] or all_steps[4:7]==["x","x","x"] or all_steps[7:10]==["x","x","x"]  or all_steps[0:9:4]==["x","x","x"] or all_steps[2:7:2]==["x","x","x"] or all_steps[0:7:3]==["x","x","x"] or all_steps[1:8:3] == ["x","x","x"] or all_steps[2:9:3]==["x","x","x"]:
		print("win user")
		return False
		

	elif all_steps[:3]==["0","0","0"] or all_steps[4:7]==["0","0","0"] or all_steps[7:10]==["0","0","0"] or all_steps[0:9:4]==["0","0","0"] or all_steps[2:7:2]==["0","0","0"] or all_steps[0:7:3]==["0","0","0"] or all_steps[1:8:3] == ["0","0","0"] or all_steps[2:9:3]==["0","0","0"]:
		print("win pc")
		return False
		
	return True	


print_tablo()

def ssss(startPlayer):
	while True:
		if (startPlayer == 'user'):
			while win():
				user = int(input("user")) 
				if user in all_steps:
					all_steps[user-1]="x"
					steps.append(user)
					startPlayer = 'pc'
					print_tablo()
					break
					
				else:
					print("Ayd tex@ zbaxvac e")
		else:
			while win():
				pc = random.randint(1,9)
				print(pc)
				if pc in all_steps:
					all_steps[pc-1]="0"
					steps.append(pc)
					startPlayer = 'user'
					print_tablo()
					break
					
		if len(steps)==9 or not win():
			break


firstplayer = random.choice(["pc","user"])
ssss(print(start(firstplayer)))





