from game import tablefunctions, Coordinates

x, y = 3, 3

if x > 9 or y > 9:
    print("Board size too large")
    exit()

gameboard = tablefunctions.createboard(x + 1, y + 1)




tablefunctions.updateboard(gameboard, 1, 1, "O")


tablefunctions.displayboard(gameboard)

tablefunctions.updateboard(gameboard, 2, 1, "X")

tablefunctions.displayboard(gameboard)

tablefunctions.updateboard(gameboard, 3, 3, "X")

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

     a  b  c       
   1 -  -  -
   2 -  -  -
   3 -  -  -

'''