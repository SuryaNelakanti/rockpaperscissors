import random
print("Welcome to Rock Paper Scissors\n")#A simple Intro
def rocker():#Made the taking of input a function so i can call it recursively
	sele=input("Enter R for Rock \nEnter P for paper\nEnter S for scissors\n")
	global sel
	sel = sele.upper()
	"""if sel!="R" or sel!="P" or sel!= "S":
		print("Invalid Input")
		rocker()
	else:"""
	ai()	
def ai():# A simple code to make computer choose between rock paper and scissor
	ai = random.choice([1,2,3])
	global comp
	if ai==1:
		comp ="R"
	elif ai==2:
		comp ="P"
	else: 
		comp = "S"
	result()
def result():# comparing user input and computer selection and printing result
	print("User has given " +sel + "\nComputer has given " + comp)
	if sel==comp:
		print("\nIt is a draw\n")
	elif sel=="R" and comp=="S":
		print("\nWinner is User!\n")
	elif sel=="R" and comp=="P":
		print("\nWinner is Computer!\n")
	elif sel=="P" and comp=="R":
		print("\nWinner is User!\n")
	elif sel=="P" and comp=="S":
		print("\nWinner is Computer!\n")
	elif sel=="S" and comp=="R":
		print("\nWinner is Computer!\n")
	elif sel=="S" and comp=="P":
		print("\nWinner is User!\n")
rocker()
rmk = input("\nDo you want to play again? Y/N\t")
if rmk.upper()=="Y":
	rocker()
else:
	print("\nGame Finished\n")

