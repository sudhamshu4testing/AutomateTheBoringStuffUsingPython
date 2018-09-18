"""As another for loop example, consider this story about the mathematician
Karl Friedrich Gauss. When Gauss was a boy, a teacher wanted to give
the class some busywork. The teacher told them to add up all the numbers
from 0 to 100. Young Gauss came up with a clever trick to figure out the
answer in a few seconds, but you can write a Python program with a for
loop to do this calculation for you """

# Program to use for loop
total = 0
for num in range(101):
	total = total + num
print(total)