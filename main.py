###Simple program that plays game of Nim. Only three players allowed. 2 Human and 1 computer. Each player can only take 1 to 3 stones. First one to get to 0 stones wins the game.

#Introduce computer AI and game
print("Hi this is a game called Taking Stones\n")
print("My name is Computer and I will be playing against you\n")

#Input player 1 details
nim = input("What is player 1's name?: ")
ID = int(input("Great! What is player 1's MIT ID?: "))
name = nim.capitalize()
print("Welcome", name, "to the game of Taking Stones\n")

#Input player 2 details
nim2 = input("What is player 2's name?: ")
name2 = nim2.capitalize()
ID2 = int(input("What is your MIT ID?:"))
print("Welcome", name2 , "to the game of Taking Stones\n")

#Begin Game
print("Let's begin the game. We'll take it turn by turn.")

#set stones and player variable
stones = 0
player = ""

#Input initial amount of stones to play with
Totalstones = int(input( "How many stones should we start with?: "))

###define state of totalstones function
def state():
  global Totalstones
  #Increase global Totalstones variable to inputted amount at start of each game 
  if Totalstones < 0:
    Totalstones = 0
  Popstones = int(input( "How many stones do you want to play with?: "))
  Totalstones += Popstones

###Fuction for player 1 turn
def getstones():
  #make total amount of stones and player global variables
  global Totalstones
  global player
  #Player 1 turn only executed if total amount of stones is more than 0
  if Totalstones > 0:
    #input desired amount of stones to take
    print("\n",name, "'s turn")
    stones = int(input("How many stones does player 1 want to take?: "))
    #reject response if doesn't fulfil conditions
    if stones < 1 or stones > 3:
      print("You can only take 1 to 3 stones.")
      stones = int(input("How many stones do you want to take?: "))
    #decrease total amount of stones by desired amount
    Totalstones -= stones
    print("You have taken", stones, "stones. There are now", Totalstones,"stones left\n")
    #switch players
    if Totalstones == 0:
      player = "1"
    else:
      player = "2"
    
  
def getstones2():
  #make total amount of stones and player global variables
  global Totalstones
  global player
  #Player 2 turn only executed if total amount of stones is more than 0
  if Totalstones > 0:
    print("\n",name2, "'s turn")
    #input desired amount of stones to take
    stones = int(input("How many stones do you want to take?: "))
    #reject response if doesn't fulfil conditions
    if stones < 1 or stones > 3:
      print("You can only take 1 to 3 stones")
      stones = int(input("How many stones do you want to take?: "))
    #decrease total amount of stones by desired amount
    Totalstones -= stones
    print("You have taken", stones, "stones.There are now", Totalstones,"stones left\n")
    #switch players
    if Totalstones == 0:
      player = "2"
    else:
      player = "3"
  

def compstones():
  #make total amount of stones and player global variables
  global Totalstones
  global player
  #Computer optimal strategy
  if Totalstones > 0:
    Taken = Totalstones % 3
    if Taken == 0:
      stones = 2
    else:
      stones = 1
    Totalstones -= stones
    print("Computer has taken", stones,"stones. There are now", Totalstones, " stones left\n")
    #switch players
    if Totalstones == 0:
      player = "3"
    else:
      player = "1"

#continue players turns while Total amount of stones is more than 0
while Totalstones > 0:
  getstones()
  getstones2()  
  compstones()

#def checkTrue function to find out winner of game when Total amount of stones goes to 0
def checkTrue():
  #if player 1 wins, print ID and name
  if (Totalstones < 1) and player == "1":
      print("Player", name, "wins! MIT:", ID, "\n")
  #if player 2 wins, print ID and name    
  elif (Totalstones < 1) and player == "2":
      print("Player", name2,"wins! MIT:", ID2, "\n")
  #if computer wins print computers wins    
  elif (Totalstones < 1) and player == "3":
    print("Computer Wins!\n")
    
checkTrue()
#define playagain function to continue playing again
def playagain():
  play = input("Do you want to play again? Y/N ")
  #if answer is yes, list game functions
  if play in ('Y','y'):
    state()
    getstones()
    getstones2()
    compstones()
    checkTrue()
    playagain()
#if answer is no, exit game
  elif play in ('N', 'n'):
    print("Goodbye.")
  #reject invalid response
  else:
    print("Not a valid response.")
    playagain()

playagain()