from game import tablefunctions, Coordinates

x, y = 3, 3

gameboard = tablefunctions.createboard(x, y)

tablefunctions.updateboard(gameboard, 1, 2, "O")


tablefunctions.displayboard(gameboard)

tablefunctions.updateboard(gameboard, 2, 1, "X")

tablefunctions.displayboard(gameboard)





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

'''