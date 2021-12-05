#Program 2: prediction the number
#Generate 1 random number (0-100)
#Ask the user to prediction the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.


# Added import and from (built in function for python)
from random import randint  
import os
os.system('cls')



# Main
print('---------------------------------------------------------------------------------------------------------------------------')
print("                                   Welcome to Carlito's Guess the Number Game!")
print('---------------------------------------------------------------------------------------------------------------------------')
name = input('Please state your name: ')
print(f'Hi, {name}! Please follow the given instructions carefully!')
print('---------------------------------------------------------------------------------------------------------------------------')
print('                                                 DIRECTIONS:')
print('       For today, we are be playing a GAME!. You only need to do is to guess the correct number between 0 to 100!')
print("         Don't Worry, The program will still give you some clues so that it will become easy for you to answer!")
print('            When you still not get the correct answer, the program continues to loop! Good luck and Have Fun!')
print('---------------------------------------------------------------------------------------------------------------------------')

# Added randint from 0, 99 and input function
Rndm_Numb = randint(0, 99)
prediction = int(input("Enter an integer from 1 to 99: \n>> "))

# While loop was made to make the user guess the right random number given.
while Rndm_Numb != 'prediction':
    if prediction < Rndm_Numb:
        print ("\nGreater Than!")
        print('---------------------------------------------------------------------------------------------------------------------------')
        prediction = int(input("Enter an integer from 1 to 99: \n>> "))
    elif prediction > Rndm_Numb:
        print ("\nLess Than!")
        print('---------------------------------------------------------------------------------------------------------------------------')
        prediction = int(input("Enter an integer from 1 to 99: \n>> "))
   
    else:
        print('---------------------------------------------------------------------------------------------------------------------------')
        print ("Congratulations! You Did It!")
        break
