# Escape the Plantation

# Set the initial variables
distance_to_freedom = 100  # Distance to freedom in miles
hunger = 0  # Hunger level on a scale of 0-10
tiredness = 0  # Tiredness level on a scale of 0-10
money = 0  # Amount of money you have

# Main game loop
while distance_to_freedom > 0:
  # Print current status
  print("Distance to freedom:", distance_to_freedom)
  print("Hunger:", hunger)
  print("Tiredness:", tiredness)
  print("Money:", money)

  # Get user input
  print ("What would you like to do?")
  print ("[w]alk, [r]est, [e]at, [s]teal money?")
  action = input()

  # Handle user input
  if action.lower() == "w":
    distance_to_freedom -= 10
    hunger += 2
    tiredness += 3
    print("You walked 10 miles.")
  elif action.lower() == "r":
    # Check if player is too tired to rest
    if tiredness == 0:
      print("You are not tired enough to rest.")
    else:
      distance_to_freedom -= 1
      hunger += 1
      tiredness -= 2
      print("You rested for a while.")
  elif action.lower() == "e":
    distance_to_freedom -= 1
    hunger -= 2
    tiredness += 1
    if hunger < 0:
      hunger = 0
    print("You ate some food.")
  elif action.lower() == "s":
    distance_to_freedom -= 1
    hunger += 1
    tiredness += 1
    money += 10
    print("You stole some money.")
  else:
    print("Invalid action.")

  # Check for game over conditions
  if hunger > 8:
    print("You died of hunger.")
    break
  elif tiredness > 8:
    print("You collapsed from exhaustion.")
    break

# Print game over message
if distance_to_freedom <= 0:
  print("Congratulations! You have escaped the plantation and are now free.")
else:
  print("Game over.")
