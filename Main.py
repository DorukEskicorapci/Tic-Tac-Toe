from game import tablefunctions, Coordinates

#x, y = 3, 3

#creates the board
check = False

size = input("Enter the board size: ")
x, y = int(size),int(size)

if x > 9 or y > 9:
    print("Board size too large. Please enter a value less than 10." + "\n")
    exit()

gameboard = tablefunctions.createboard(x, y)

tablefunctions.displayboard(gameboard)



#starts taking user input for game moves
i = 1
while check == False:
   usermove = input("Enter the coordinates for player " + str(i) + ": ")

   move_x = Coordinates.translate_x(usermove)
   move_y = Coordinates.translate_y(usermove)
   if i == 1:
      i = 2
      gameboard[move_y][move_x] = "X"
        
   else:
      i = 1
      gameboard[move_y][move_x] = "O"

   
   tablefunctions.displayboard(gameboard)

   usermove = input("Do you want to end the game. Enter 'yes' or 'no': ")
   if usermove == "yes":
        check = True
      
        





def checkwin(gameboard):
    


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

#Coordinates.obj.print_value()

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