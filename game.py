class Coordinates:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj = Coordinates("a")


class tablefunctions:
    def calltable(xs, ys):
        
        #xs, ys = 3, 3
        gametable = [['[]']*xs]*ys
        
        for xs in gametable:
            print(*xs, sep="\t")
        



