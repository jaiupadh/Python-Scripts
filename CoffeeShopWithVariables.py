#This is a Python Program to simulate a Coffee Show using Variables 

#Robo Barista Welcome Message
print('Hey There Buddy ;) Welcome to My Coffee Shop !!! \n')

name = input(" What is your name ? \n")

print ('Hello ' + name + ', thank you for coming in today. \n')

menu = "Black Coffee, Espresso, Latte, Cappuccino"

print ('So ' + name + ', what would you like from our menu today ? Here is what we are serving. \n' + menu)

order = input()

price = 8

quantity = input("How many coffee would you like ? \n")

total = price * int(quantity)

print ("Thank you. that'll be a total of : $" +str(total))

print ('\n Sounds good ' + name + ', We will have your ' + quantity + " " + order + ' ready for you in a moment.')
