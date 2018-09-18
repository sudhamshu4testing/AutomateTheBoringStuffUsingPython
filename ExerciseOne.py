#This program says hello and asks for my name

print ("Hello World!")
# print ("What is your name? ") #This is taken from the book
# myName = input() #This is taken from the book
myName = input("What is your name? ") # I modified this

print ("It is good to meet you, " +myName) #This is taken from the book
# print ("The length of your name is: ") #This is taken from the book
# print (len(myName)) #This is taken from the book

print ("The length of your name is: " + str(int(len(myName)))) # I modified this

#print ("What is your age? ") #This is taken from the book
# myAge = input() #This is taken from the book
myAge = input ("What is your age? ") # I modified this
print ('You will be ' + str(int(myAge) + 1) + ' in a year.') #This is taken from the book
