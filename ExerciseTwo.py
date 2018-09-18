#Program for 'While' loop and continue

while True:
	name = input('Who are you? ')
	if name != 'Sudhamshu':
		continue
	print ('Hello Sudhamshu, what is the password? (It is a fish)')
	password = input()
	if password == 'swordfish':
		break
print("Access granted")