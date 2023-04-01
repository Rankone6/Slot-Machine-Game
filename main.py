#My Slot Machine Program

x = ["A", "B", "C", "D"]
x1= x[:]
y=x1

deposit = 0
BET = 0
BET1=0
BET2 = 0
BET3 = 0
play="y"
balance = 0

import random

def display_slots(z):
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
	return z


def deposit_amount(deposit):
	while True:
		deposit = input("How much would you like to deposit?\n$")
		print()
		if deposit.isdigit():
			deposit = int(deposit)
			break
		else:
			print("Must enter a number,")
	return deposit


def get_BET(BET):
	while True:
		BET = input("How much do you want to bet?\n$")
		print()
		if BET.isdigit():
			BET = int(BET)
			break
		else:
			print("Must enter a number,")
	return BET


def cal_winnings(BET, BET1, BET2, BET3):
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
	return BET, BET1, BET2, BET3 
	

def deposit_balance(deposit, winnings):
	deposit = deposit - winnings[0] + winnings[1]+ winnings[2] +winnings[3]
	return deposit, winnings[0], winnings[1], winnings[2], winnings[3]
	

def won(z,BET, winnings):
	if z[0] == z[1] == z[2] or z[3] == z[4] == z[5] or z[6] == z[7] == z[8]:
		print(f"Your a winner!!! You won ${winnings[1]+ winnings[2] +winnings[3]}")
	else:
		print(f"You lost ${BET}")
		print("Try again.")
	return z, BET, winnings


	
#The run script of slot machine.
while play=="y":
	z=random.choices(y, weights=[2,3,6,8], k=9)
	if deposit <= 0:
		while deposit <= 0:
			print ("Enter an amount greater than $0 please....")
			deposit = deposit_amount(deposit)
			if deposit > 0:
				BET = get_BET(BET)
				while BET > deposit:
					print(f"Enter an amount less than or equal to $ {deposit}")
					BET = get_BET(BET)
					if BET <= deposit:
						break
				
			
	else:
		BET= get_BET(BET)
		while BET > deposit:
			print(f"Enter an amount less than or equal to $ {deposit}")
			BET = get_BET(BET)
			if BET <= deposit:
				break	
	
	z=display_slots(z)
	winnings = cal_winnings(BET,BET1,BET2,BET3)
	balance = deposit_balance(deposit, winnings)
	won(z,BET, winnings)
	deposit = balance[0]
	print( f"Your balance is ${balance[0]}")
	play=input("Do you want to play again? select -y- for yes and anything else for no. \n")

print(f"Thanks for playing! Your Balance is ${deposit}. Collect your Earnings at the table.")



