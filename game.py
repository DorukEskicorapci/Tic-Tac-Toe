class Coordinates:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj = Coordinates("a")


class tablefunctions:
    def callboard(xs, ys):
        
        #xs, ys = 3, 3
        gameboard = [['▢']*xs]*ys
        
        print("Board:" + "\n")
        for xs in gameboard:
            print(*xs, sep="  ")
        print()