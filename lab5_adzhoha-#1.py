###Roll of dice. Alisa Dzhoha. This program asks the user to hit Enter to roll the dice, and then gives the result as a total, with the numbers shown from both dice, and the term associated with it. 09/26/2025
import random

userChoice = input('Hit enter to roll the dice: ')

while userChoice != None:
  dice1 =random.randint(1, 6)
  dice2 = random.randint(1, 6)
  totalPoint = dice1 + dice2
  if totalPoint == 2:
    term = 'Snake Eyes'
  elif totalPoint == 3:
    term = 'Ace Caught a Deuce'
  elif dice1 == 2 and dice2 == 2:
    term = 'Little Joe from Kokomo'
  elif totalPoint == 5:
    term = 'Little Phoebe'
  elif dice1 == 3 and dice2 == 3:
    term = 'Jimmy Hicks from the Sticks'
  elif (dice1 == 6 and dice2 == 1) or (dice1 == 1 and dice2 == 6):
    term = 'Six Ace'
  elif dice1 == 4 and dice2 == 4:
    term = 'Eight from Decatur'
  elif totalPoint == 9:
    term = 'Nina from Pasadena'
  elif dice1 == 5 and dice2 == 5:
    term = 'Puppy Paws'
  elif (dice1 == 6 and dice2 == 5) or (dice1 == 5 and dice2 == 6):
    term = 'Six Five no Jive'
  elif totalPoint == 12:
    term = 'Boxcars'
  else:
    term = 'No term'
  
  print(f'The outcome of the roll: {totalPoint}, with dice showing value of {dice1} and {dice2}')
  print(f'The term for your roll is: {term}')
  userChoice = input('Hit enter to roll the dice: ')