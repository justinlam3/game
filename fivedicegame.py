import random
import collections
import re

def roll():
  return random.randint(1,6)

def reRoll():
  reRoll = list(map(int, input("Input the dice(s) wanted to re-roll: ").split()))
  for i in range(len(reRoll)):
    if reRoll[i] == 0:
      break
    else:
      playerDice.remove(playerDice[reRoll[i]-1])
      playerDice.insert(reRoll[i]-1,roll())


def inputCheck(diceValue):
	if re.match('\[0-6]{1}',diceValue):
	  return True
	else:
	  return False
	  
def isStraight(sortList):
  digit=0
  while digit<4:
    if (sortList[digit]+1 != sortList[digit+1]) :
      return False
    else:
      digit+=1
  return True


playerChips = 1000
playerDice = []

while True:
  playerChips -= 100
  playerDice.clear()
  print ("\n100 Chips is deducted, Game will be started \n")
  for i in range(5):
      playerDice.append(roll())

  print ("your 1st roll: ", *playerDice)
  reRoll()
  print ("your 2nd roll: ", *playerDice)
  reRoll()
  print ("Final roll: ", *playerDice)

  playerDice.sort()
  diceCount = list(collections.Counter(playerDice).values())
  diceCount.sort(reverse=True)

  #print (*diceCount)

  if diceCount[0] == 5:
    playerChips += 100*5
    print ("WoW, You got a FIVE A KIND\nYou Won 5x chips\n")
  elif diceCount[0] == 4:
    playerChips += 100*4
    print ("FOUR A KIND!\nYou Won 4x chips\n")
  elif isStraight(playerDice):
    playerChips += 100*3
    print ("A Straight!\nYou have won 3x chips!")
  elif (diceCount == [3,2]):
    playerChips += 100*2.5
    print ("FULL HOUSE\n2.5x chips won")
  elif (diceCount == [3,1,1]):
    playerChips += 100*2
    print ("THREE A KIND\n2x chips")
  elif (diceCount[0] == 2) & (diceCount[1] == 2) :
    playerChips += 100
    print ("TWO PAIR")
  elif (diceCount == [2,1,1,1]):
    playerChips += 100*0.5
    print ("PAIR")
  else:
    print ("sorry you won nothing")

  print ("You have %d Chips\n" %playerChips)
  
  countinue = input("Countinue (Y/N)? ")
  if countinue == "N":
    break
