import random
#Slot Machine possible values/elements/symbols
x = ["A", "B", "C", "D"]
x1= x[:]
y=x1
# Define and set list x to be random elements that each have possibility level of occurences and number of elements in a new list i.e. since planning a matrix of 3 by 3 making it have 9 possibilities in of elements.
a=random.choices(x, weights=[1,1,1,1], k=9)
z=random.choices(y, weights=[90,4,8,16], k=9)
#bet = input("How much do you want to bet?\n")


#Displays an example of how slots will display so instructions are visual.
def display_slots1():

#output and display of Example of Slots:
	for i in range(9):
	#1st row output display
		if  0 <= i <= 2:
			if  0 <= i < 2:
				print (f"{a[i]}", end= " | ")
			elif i == 2:
				print (f"{a[i]}",end= " \n")
	#2nd row out put:
		if  3 <= i <= 5:
			if  3 <= i < 5:
				print (f"{a[i]}", end= " | ")
			elif i == 5:
				print (f"{a[i]}",end= " \n")
	#3rd row out put:
		if  6 <= i <= 8:
			if  6 <= i < 8:
				print (f"{a[i]}", end= " | ")
			elif i == 8:
				print (f"{a[i]}",end= " \n")
	print()


def display_slots():

#output and display of Slots:
	for i in range(9):
	#1st row output display
		if  0 <= i <= 2:
			if  0 <= i < 2:
				print (f"{z[i]}", end= " | ")
			elif i == 2:
				print (f"{z[i]}",end= " \n")
	#2nd row out put:
		if  3 <= i <= 5:
			if  3 <= i < 5:
				print (f"{z[i]}", end= " | ")
			elif i == 5:
				print (f"{z[i]}",end= " \n")
	#3rd row out put:
		if  6 <= i <= 8:
			if  6 <= i < 8:
				print (f"{z[i]}", end= " | ")
			elif i == 8:
				print (f"{z[i]}",end= " \n")

	print()

def cal_winnings(BET, BET1, BET2, BET3, bet_tot):
	
	BET = input("How much do you want to bet?\n$")
	print()
#adding function to display slot values after bet is made.
	display_slots()

# calculation of Winnings printed results:
	for i in range(9):
		if i == 0:
			if z[i] == z[i+1] == z[i+2]:
				if z[i] == "A":
					BET1 = int(BET) * 8
				elif z[i] == "B":
					BET1 = int(BET) * 4
				elif z[i] == "C" or "D":
					BET1 = int(BET) * 2
			
			
		elif i== 3:
			if z[i] == z[i+1] == z[i+2]:
				if z[i] == "A":
					BET2 = int(BET) * 8
				elif z[i] == "B":
					BET2 = int(BET) * 4
				elif z[i] == "C" or "D":
					BET2 = int(BET) * 2
	
		elif i == 6:
			if z[i] == z[i+1] == z[i+2]:	
				if z[i] == "A":
					BET3 = int(BET) * 8
				elif z[i] == "B":
					BET3 = int(BET) * 4
				elif z[i] == "C" or "D":
					BET3 = int(BET) * 2

#Displaying Results:
	if z[0] == z[1] == z[2] or z[3] == z[4] == z[5] or z[6] == z[7] == z[8]:
		bet_tot=BET1+BET2+BET3
		print(f"Your a winner!!! You won ${bet_tot}")
		
	else:
		BET = int(BET)
		print(f"You lost ${BET}")
		print("Try again.")
	
	
	
	print()

	return BET, BET1, BET2, BET3, bet_tot

def instruct():
	print("""This is how slot choices will display.
If three A's in a row you win 8 times your bet.
If three B's in a row you win 4 times your bet.
If three C's or three D's in a row you win 2 times your bet.
 
Are you ready??
 
Let gamble!!!!!
""")

def start():
	display_slots1()
	instruct()	

def deposit_amount(deposit):
	deposit = input("What is your deposit?\n$")
	deposit = int(deposit)
	return deposit

def main(remaining_balance):
	deposit = deposit_amount(0)
	
	winnings = cal_winnings(0, 0, 0, 0, 0)
	bet = int(winnings[0])
	bet1 = int(winnings[1])
	bet2 = int(winnings[2])
	bet3 = int(winnings[3])
	bet_total = int(winnings[4])

	remaining_balance = (deposit - bet) + (bet1 + bet2 + bet3)
	
	print(f"Your remaiming balance is ${remaining_balance}")	
	return	remaining_balance
		

def play():
	remaining_balance = main(0)
	print (remaining_balance)
	print(type(remaining_balance))



	
	deposit = deposit_amount(0)
	
	
	
	#while True:
	#	if remaining_balance > 0:
	#		play =input("play again?")
	#		if play == "yes": 
	#			main(0)
	#		elif play == "no":
	#			exit
	#	else:
	#		print ("need to deposit more mponey.")
play()	
#		else:
#			print("need to deosit more money")
