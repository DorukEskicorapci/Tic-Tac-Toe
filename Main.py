from game import tablefunctions, Coordinates

#x, y = 3, 3

size = input("Enter the board size: ")
x, y = int(size),int(size)

if x > 9 or y > 9:
    print("Board size too large. Please enter a value less than 10." + "\n")
    exit()

gameboard = tablefunctions.createboard(x, y)

tablefunctions.displayboard(gameboard)

user1move = input("Enter the coordinates for player 1: ")

move_x = Coordinates.translate_x(user1move)
move_y = Coordinates.translate_y(user1move)

gameboard[move_y][move_x] = "X"



tablefunctions.updateboard(gameboard, 1, 1, "x")


tablefunctions.displayboard(gameboard)

"""
tablefunctions.updateboard(gameboard, 2, 1, "X")

tablefunctions.displayboard(gameboard)

tablefunctions.updateboard(gameboard, 3, 3, "X")

tablefunctions.displayboard(gameboard)

"""

'''
#command for printing the whole board 

for xs in gameboard:
    print(*xs, sep="\t")
            
'''



#Coordinates.obj.print_value()

'''  
      y1 y2 y3       
   x1 -  -  -
   x2 -  -  -
   x3 -  -  -

     a  b  c       
   1 -  -  -
   2 -  -  -
   3 -  -  -

'''