class Coordinates:
    def __init__():
        
        
        print("obj")


class tablefunctions:

    def createboard(x, y):
        
        #x, y = 3, 3
        
        gameboard = [['▢' for _ in range(x)] for _ in range(y)]
        
        return gameboard

    
    
    def displayboard(gameboard):
        
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