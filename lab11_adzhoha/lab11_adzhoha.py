"""
Rotation degrees counter. Alisa Dzhoha. This program takes an input from the user and, based on the degree provided, determines its position on the Cartesian. 11/08/2025
coordinate system.

"""
def calculating_degree_rotation(degree):
  full_degree = 360

  try:
    degree = int(degree)
  except (ValueError, TypeError):
    return "Your input is invalid, please provide a number"
  
  if degree > 0:
    rotation_counter = degree / full_degree
    full_rotation = full_degree * int(rotation_counter)
    answer = degree - full_rotation

    return answer
  
  elif degree < 0:
    rotation_counter = degree / full_degree
    full_rotation = full_degree * int(rotation_counter)
    difference = degree - full_rotation
    answer = full_degree - abs(difference)

    return answer
  else:
    return 0

def main():  
  while True:
    try:
      degree = int(input('Please enter degree of the rotation: '))
      print(f'Your calculated degree is: {calculating_degree_rotation(degree)}')
    except (ValueError, TypeError) as e:
      print(f'Your input is invalid, please provide a number   {e}')

if __name__ == "__main__":
  main()
