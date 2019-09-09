import random
import os
import time
import platform

def guessing(bottom, top):
    guessThis = random.randint(bottom+1, top-1)
    while True:
        userGuess = input("Please make your guess %d - %d \n" % (bottom, top))
        userGuess = int(userGuess)
        if userGuess < bottom:
            print ('You cannot enter a number less then %d \n' % bottom)
        elif userGuess > top:
            print ('You cannot enter a number larger then %d \n' % top)
        elif userGuess < guessThis:
            bottom = userGuess
        elif userGuess > guessThis:
            top = userGuess
        else:
            print ('Congratulations! You have won the game!')
            time.sleep(3)
            break

def menu():
  print ("Welcome to Number Guesser! \n")
  print ("Please select the mode you wanted: \n")
  print ("1. The Normal mode (1-100) \n")
  print ("2. Self-Defined (??-??) \n")
  print ("3. Exit Game \n")
  
def clear():
    if platform.system() == "Windows":
       os.system('cls')
    else:
       os.system('clear')

while True:
  clear()
  menu()
  optionSelected = input()
  if optionSelected == "1" :
    print ("Normal mode selected")
    guessing(1,100)
    break
  elif optionSelected == "2" : 
    print ("Self-Defined mode selected")
    while True:
        clear()
        definedA = int(input("Please define your first number: "))
        definedB = int(input("Please define your second number: "))
        
        if abs(definedA-definedB)<2:
            print ("Two numbers are too near")
            time.sleep(3)
            break
        elif definedA > definedB:
            guessing(definedB, definedA)
            break
        elif definedA < definedB:
            guessing(definedA, definedB) 
            break
        else:
            print ("You cannot input two same number") 
  elif optionSelected == "3":
    print ("Thanks for Playing")
    time.sleep(3)
    break
  else:
    print ("There is no such option")
    time.sleep(3)
