import random
class Coin:
  def __init__(self, amount, sideup):

    self.__amount = amount
    self.__sideup = sideup

  def toss(self):
    random_sideup = 0
    random_sideup =random.randint(0, 1)
    if random_sideup == 1:
      self.__sideup = "Heads"
    elif random_sideup == 0:
      self.__sideup = "Tails"

  def set_amount(self, result1, result2):
    if result1 == result2:
      self.__amount += 1
    elif result1 != result2:
      self.__amount -= 1

  def get_sideup(self):
    return self.__sideup

  def get_amount(self):
    return self.__amount

