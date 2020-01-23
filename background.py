'''Module to create Obstacles and Coins'''
from colorama import Fore, Style

class ObstacleH:
    '''Class for horizontal obstacles'''
    def __init__(self, grid):
        self.__grid = grid

    def create_obstacle(self, x_val, y_val):
        '''Method to create obstacle'''
        self.__grid[x_val][y_val] = "o"
        self.__grid[x_val][y_val + 10] = "o"
        for i in range(y_val + 1, y_val + 10):
            self.__grid[x_val][i] = "-"

class ObstacleV(ObstacleH):
    ''''Class for vertical obstacles'''
    def __init__(self, grid):
        ObstacleH.__init__(self, grid)

    def create_obstacle(self, x_val, y_val):
        '''Method to create obstacle'''
        self._ObstacleH__grid[x_val][y_val] = "o"
        self._ObstacleH__grid[x_val + 5][y_val] = "o"
        for i in range(x_val + 1, x_val + 5):
            self._ObstacleH__grid[i][y_val] = "|"

class ObstacleD(ObstacleH):
    ''''Class for diagonal obstacles'''
    def __init__(self, grid):
        ObstacleH.__init__(self, grid)

    def create_obstacle(self, x_val, y_val):
        '''Method to create obstacle'''
        self._ObstacleH__grid[x_val][y_val] = "o"
        self._ObstacleH__grid[x_val + 5][y_val + 5] = "o"
        for i in range(1, 5):
            self._ObstacleH__grid[x_val + i][y_val + i] = "\\"

class Magnet(ObstacleH):
    ''''Class for Magnet'''
    def __init__(self, grid):
        ObstacleH.__init__(self, grid)

    def create_obstacle(self, x_val, y_val):
        '''Method to create magnet'''
        self._ObstacleH__grid[16][y_val] = "🧲"

class Coins:
    ''''Class for coins'''
    def create_coins(self, x_val, y_val, grid):
        '''Method to create coins'''
        for i in range(0, 10):
            grid[x_val][y_val+i] = Fore.LIGHTCYAN_EX + "$" + Style.RESET_ALL
