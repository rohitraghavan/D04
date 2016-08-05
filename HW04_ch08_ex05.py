# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate(word, rotationno):
	newword = ""
	for char in word:
		#Convert char to number
		numchar = ord(char)
		#Rotate the chars
		newnumchar = numchar + rotationno
		#Handle upper case chars which go outside bounds on rotating
		if 65 <= numchar <= 90 and newnumchar > 90:
			newnumchar = 65 + (newnumchar - 90 -1)
		#Handle lower case chars which go outside bounds on rotating
		elif 97 <= numchar <= 122 and newnumchar > 122:
			newnumchar = 97 + (newnumchar - 122 -1)
		#Append chars (converted from rotated numbers) to new word
		newword = newword + chr(newnumchar)
	return newword

def main():
	print(rotate('Rohit',1))
	print(rotate('abcxyz',1))
	print(rotate('ABCXYZ',1))
	print(rotate('abcxyz',26))

if __name__ == "__main__":
	main()
			

