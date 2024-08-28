from game import tablefunctions, Coordinates, gameproperties


def userinput(gameboard, size): #starts taking user input for game moves
   check = False
   i = 1
   x, y = int(size),int(size)
   while check == False:
      usermove = input("Enter the coordinates for player " + str(i) + ": ")

      move_x = Coordinates.translate_x(usermove)
      move_y = Coordinates.translate_y(usermove)

      if move_x > x or move_y > y:
         print("Invalid coordinates. Please try again" + "\n")
         continue

      if gameboard[move_x][move_y] == "X" or gameboard[move_x][move_y] == "O":
         print("There is already a sign in the desired position. Please try again" + "\n")
         continue

 
      if i == 1:
         i = 2
         gameboard[move_x][move_y] = "X"
         
      else:
         i = 1
         gameboard[move_x][move_y] = "O"

      
      tablefunctions.displayboard(gameboard)

      if gameproperties.x_checkwin(gameboard, x):
         print("Player 1 (X) wins!" + "\n")
         check = True
         break
      elif gameproperties.O_checkwin(gameboard, y):
         print("Player 2 (O) wins!" + "\n")
         check = True
         break
      elif gameproperties.checkdraw(gameboard, x):
          print("The game is a draw!" + "\n")
          check = True
          break


#creates the board
def startgame():
  
  size = input("Enter the board size: ")
  x, y = int(size),int(size)

  if x > 9 or y > 9:
      print("Board size too large. Please enter a value less than 10." + "\n")
      exit()

  gameboard = tablefunctions.createboard(x, y)

  tablefunctions.displayboard(gameboard)

  userinput(gameboard, size)

continuegame = True
while continuegame == True:
    startgame()
    usermove = input("Do you want to play again? Enter 'yes' or 'no': ")
    lowercaseusermove = usermove.lower()
    if usermove == "no":
      continuegame = False
    else:
      continuegame = True
      print("New game started!" + "\n")
   



""" Code for manuel game end

   gameboard[0][i] = letters[i]
         i += 1

   usermove = input("Do you want to end the game. Enter 'yes' or 'no': ")
   if usermove == "yes":
        check = True
   """
        





    


""" update and display the board
tablefunctions.updateboard(gameboard, 1, 1, "x")


tablefunctions.displayboard(gameboard)


tablefunctions.updateboard(gameboard, 2, 1, "X")

tablefunctions.displayboard(gameboard)

tablefunctions.updateboard(gameboard, 3, 3, "X")

tablefunctions.displayboard(gameboard)


#command for printing the whole board 

for xs in gameboard:
    print(*xs, sep="\t")
            
"""

""" scenarios  
      y1 y2 y3         
   x1 x  x  x
   x2 -  -  -
   x3 -  -  -

      y1 y2 y3       
   x1 x  -  -
   x2 -  x  -
   x3 -  -  x

      y1 y2 y3       
   x1 x  -  -
   x2 x  -  -
   x3 x  -  -

"""


'''  coordinates for the board
      y1 y2 y3       
   x1 -  -  -
   x2 -  -  -
   x3 -  -  -

     a  b  c       
   1 -  -  -
   2 -  -  -
   3 -  -  -

'''