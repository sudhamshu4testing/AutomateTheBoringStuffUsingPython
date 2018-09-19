#Program for the collatz sequence

def collatz(number):
	try:
		if number % 2 == 0:
			n = number // 2
			return n
		else:
			s = 3 * number + 1
			return s
	except ValueError:
		print ("Error: Invalid number, you should enter a valid integer")

n = int(input("Enter a number: "))
print (collatz(n))

