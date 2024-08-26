class Coordinates:
    def __init__():
        
        
        print("obj")


class tablefunctions:

    def createboard(x, y):
        
        # ideal values: x, y = 3, 3
        i = 0
        gameboard = [['▢' for _ in range(x)] for _ in range(y)]

       

        letters = " abcdefghijklmnopqrstuvwxyz"
        while i < y:
            gameboard[0][i] = letters[i]
            i += 1
        i = 0
        while i < x:
            gameboard[i][0] = i
            i += 1
        gameboard[0][0] = " "


            

        return gameboard

    
    
    def displayboard(gameboard):
        i = 0

        print("\n" + "Current Board:" + "\n")
        for x in gameboard:
           
            
            print(*x, sep="  ")
            
            
        print()
    
    def updateboard(gameboard, x, y, player):
        
        
        if player == "X":
            gameboard[x][y] = "X"
        elif player == "O":
            gameboard[x][y] = "O"
        
        return gameboard


    """
    def autodisplayboard(gameboard):
        
        print("\n" + "New Board:" + "\n")
        for x in gameboard:
            print(*x, sep="  ")
        print()
    """