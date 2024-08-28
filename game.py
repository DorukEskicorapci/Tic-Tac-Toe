class Coordinates:
    def translate_y(usermove_x):
        
        move_x = usermove_x[0]
        #lowercase = move_x.lower()
        casefold = move_x.casefold()
        i = 0
        letters = "abcdefghijklmnopqrstuvwxyz"
        while i < len(letters):
            if casefold == letters[i]:
                return i + 1
                break
            i += 1

    
    def translate_x(usermovey):
        
        return int(usermovey[1])

class gameproperties:
    def x_checkwin(gameboard, size):
        
        #vertical check
        k = 1
        while k < size +1:
            repcheck = 0
            j = 1 
            while j < size +1:
                if gameboard[j][k] == "X":
                    repcheck += 1
                else:
                    repcheck = 0
                if repcheck == size :
                    return True
                
                j += 1
            k += 1

        #horizontal check
        k = 1
        while k < size +1:
            repcheck = 0
            j = 1 
            while j < size +1:
                if gameboard[k][j] == "X":
                    repcheck += 1
                else:
                    repcheck = 0
                if repcheck == size :
                    return True
                
                j += 1
            k += 1

        #andiagonal check
        repcheck = 0
        k = -1
        while k <= size:
            j = 1 
            while j <= size:
                if repcheck == size :
                    
                    return True
                else:
                    if gameboard[-j][j] == "X":
                        repcheck += 1
                    else:
                        repcheck = 0
                j += 1
            k += 1
        

        #diagonal check
        repcheck = 0
        k = -1
        while k <= size:
            j = 1 
            while j <= size:
                if repcheck == size :
                    
                    return True
                else:
                    if gameboard[j][j] == "X":
                        repcheck += 1
                    else:
                        repcheck = 0
                j += 1
            k += 1


        return False


    def O_checkwin(gameboard, size):
        
        repcheck = 0
        k = -1
        while k <= size:
            j = 1 
            while j <= size:
                if repcheck == size :
                    
                    return True
                else:
                    if gameboard[j][k] == "O":
                        repcheck += 1
                    else:
                        repcheck = 0
                j += 1
            k += 1

        repcheck = 0
        k = -1
        while k <= size:
            j = 1 
            while j <= size:
                if repcheck == size :
                    
                    return True
                else:
                    if gameboard[k][j] == "O":
                        repcheck += 1
                    else:
                        repcheck = 0
                j += 1
            k += 1

        repcheck = 0
        k = -1
        while k <= size:
            j = 1 
            while j <= size:
                if repcheck == size :
                    
                    return True
                else:
                    if gameboard[-j][j] == "O":
                        repcheck += 1
                    else:
                        repcheck = 0
                j += 1
            k += 1
        


        repcheck = 0
        k = -1
        while k <= size:
            j = 1 
            while j <= size:
                if repcheck == size :
                    
                    return True
                else:
                    if gameboard[j][j] == "O":
                        repcheck += 1
                    else:
                        repcheck = 0
                j += 1
            k += 1


        return False

class tablefunctions:

    def createboard(x, y):
        
        # ideal values: x, y = 3, 3
        x = x + 1
        y = y + 1
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

