#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
def guess():
	#Set a random number
	randomno = random.randrange(1, 25, 2)
	for counter in range(0, 5):
		try:
			inputno = int(input("Guess a number (between 1-25):"))
			# If numbers match exit, if greater print Too high, if lower, print Too low
			if inputno == randomno:
				print("You guessed correctly!")
				break
			elif inputno < randomno:
				print("Too low")
			elif inputno > randomno:
				print("Too high")
		#If not a number, print message
		except:
			print("Try again. Not a number")
	else:
		print("Out of guesses.")



################################################################################
def main():


    guess()
    

if __name__ == '__main__':
    main()