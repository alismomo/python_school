### Deal Cards. Alisa Dzhoha. The program asks how many cards you want, then randomly 
# picks that many cards by combining values and suits and prints them out. 09/18/2025
import random
cardRequest = int(input("Please input the number of cards in a hand:"))

cardValues = ["A", "2", "3", "4", "5", "6", "7", "8","9", "10", "J", "Q", "K"]
cardSuits = ["♥", "♦", "♣", "♠"]

i = 0
while i != cardRequest:
  for card in random.choice(cardValues):
    for suits in random.choice(cardSuits):
      together = card + suits
      #bug: it prints instead of 10 -> 1 and 0 
      print(together) 
  i += 1