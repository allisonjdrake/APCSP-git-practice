#dictionary for the number of wins per player
Score_count = {"player1": 0, "player2": 0}

#user input decides # of rounds
#there cannot be an even number of rounds to prevent ties
rounds = int(input("How many rounds would you like to play?"))
if rounds%2 == 0:
  rounds = int(input("Please choose an odd number."))
count = rounds - 1

#get the names of each player
print("Welcome to the rock, paper, scissors competition!")
print("Chose what you want to play by writing the name of the object (capitalized and without extra spaces)!")
player_1 = input("Player 1 please enter your name.")
player_2 = input("Player 2 please enter your name.")

#play the number of rounds set earlier, saving who wins each
while count >= 0:
  player1 = input(f"{player_1}: Would you like to pick Rock, Paper, or Scissors?")
#print a block that helps prevent the person from seeing the previous response
  print("_"*3000)
  player2 = input(f"{player_2}: Would you like to pick Rock, Paper, or Scissors?") 
  
  if player1 == player2:
    print("shoot again")
    count += 1
  elif player1 == "Rock":
    if player2 == "Paper":
      print("Player 2 wins")
      Score_count["player2"] += 1
    else: 
      print("Player 1 wins")
      Score_count["player1"] += 1
  elif player1 == "Paper":
    if player2 == "Rock":
      print("Player 1 wins")
      Score_count["player1"] += 1
    else: 
      print("Player 2 wins")
      Score_count["player2"] += 1
  elif player1 == "Scissors":
    if player2 == "Paper":
      print("Player 1 wins")
      Score_count["player1"] += 1
    else:
      print("Player 2 wins")
      Score_count["player2"] += 1
  else: 
    print("shoot again please")
    count += 1
  count -= 1
  print("NEXT ROUND") 

#determine and print the winner
if Score_count["player1"] > Score_count["player2"]:
  print(f'{player_1} WINS!' "\U0001F600")
else:
  print(f'{player_2} WINS!' "\U0001F600")
