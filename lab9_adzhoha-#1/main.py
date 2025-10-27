###coin game. Alisa Dzhoha. This program is supposed to be a two-player coin toss game where both players start with 20 coins and should win or lose coins depending on if their flips match. 10/25/2025
from coin import Coin

continue_game = True

player1 = Coin(20, "Heads")
player2 = Coin(20, "Heads")
print("Welcome! You are player #1")
while continue_game == True:
  user_input = input("Hit enter to flip the coin: ")
  if user_input == "":
    player1.toss()
    player2.toss()

    outcome_player1 = player1.get_sideup()
    outcome_player2 = player2.get_sideup()

    print(f"Your coin shows: {outcome_player1}")
    print(f"Your oponent got: {outcome_player2}")

    if outcome_player1 == outcome_player2:
        coins_left1 = player1.set_amount(outcome_player1, outcome_player2) 
        print("Coins match! You take a coin from player #2.")
    elif outcome_player1 != outcome_player2: 
        coins_left2 = player2.set_amount(outcome_player2, outcome_player1) 
        print("Coins do not match. Player #2 takes a coin from you.")

    print(f"You have coins left: {player1.get_amount()}")
    print(f"Your oponent has coints left: {player2.get_amount()}")

  else:
    continue_game = False