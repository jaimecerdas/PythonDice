import random

#Enter the minimum and maximum limits of the dice rolls below
number_of_dice = int(input("How many times do you want to roll the dice, amigo? "))
min_val = 1
max_val = 6
roll = 1

while number_of_dice > 0:
    print("- - - - - - - - - ")
    print("Roll #", roll)
    print("The values are :")
#Printing the randomly generated variables
    print("Dice A: ",random.randint(min_val, max_val))
    print("Dice B: ",random.randint(min_val, max_val))
#Here the user enters yes or y to continue and any other input ends the program
    roll += 1
    number_of_dice -= 1

#Message if selection in not
print("Game over!")