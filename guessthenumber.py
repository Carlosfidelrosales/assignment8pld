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
print('\033[1m\033[33m---------------------------------------------------------------------------------------------------------------------------\033[0m\033[0m')
print("                                   \033[93m\033[1mWelcome to Carlito's Guess the Number Game!\033[0m\033[0m")
print('\033[1m\033[33m---------------------------------------------------------------------------------------------------------------------------\033[0m\033[0m')
name = input('Please state your \033[4mname\033[0m: ')
print(f'\033[92m\033[1mHi, \033[4m{name}\033[0m!\033[0m\033[0m \033[92m\033[1mPlease follow the given instructions carefully!\033[0m\033[0m')
print('\033[1m\033[33m---------------------------------------------------------------------------------------------------------------------------\033[0m\033[0m')
print('                                                 \033[96mDIRECTIONS\033[0m:')
print('       \033[96mFor today, we are be playing a GAME!. You only need to do is to guess the correct number between 0 to 100!\033[0m')
print("         \033[96mDon't Worry, The program will still give you some clues so that it will become easy for you to answer!\033[0m")
print('            \033[96mWhen you still not get the correct answer, the program continues to loop! Good luck and Have Fun!\033[0m')
print('\033[1m\033[33m---------------------------------------------------------------------------------------------------------------------------\033[0m\033[0m')

# Added randint from 0, 99 and input function
Rndm_Numb = randint(0, 99)
prediction = int(input("\033[95mEnter an integer from \033[4m0 to 99\033[0m: \n>>\033[0m "))

# While loop was made to make the user guess the right random number given.
while Rndm_Numb != 'prediction':
    if prediction < Rndm_Numb:
        print ("\033[91m\nGreater Than!\033[0m")
        print('\033[1m\033[33m---------------------------------------------------------------------------------------------------------------------------\033[0m\033[0m')
        prediction = int(input("\033[95mEnter an integer from 0 to 99: \n>>\033[0m "))
    elif prediction > Rndm_Numb:
        print ("\033[91m\nLess Than!\033[0m")
        print('\033[1m\033[33m---------------------------------------------------------------------------------------------------------------------------\033[0m\033[0m')
        prediction = int(input("\033[95mEnter an integer from 0 to 99: \n>>\033[0m "))
   
    else:
        print('\033[1m\033[33m---------------------------------------------------------------------------------------------------------------------------\033[0m\033[0m')
        print ("\033[1m\033[91mCongratulations! You Did It!\033[0m\033[0m")
        break
