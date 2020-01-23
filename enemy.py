'''This module create Boss Enemy'''
from colorama import Fore, Style
from mandalorian import Man

class BossEnemy(Man):
    '''Class for Boss Enemy'''
    def __init__(self, xco, yco):
        Man.__init__(self, xco, yco)
        self._life = 30
        self.__boss = []
        self.__list1 = []
        self.__list2 = []

    def get_x(self):
        '''Returns x coordinate'''
        return self._Man__xco

    def set_x(self, x_val):
        '''Sets x co-ordinate'''
        self._Man__xco += x_val

    def get_y(self):
        '''Returns y coordinate'''
        return self._Man__yco

    def set_y(self, x_val):
        '''Sets y coordinate'''
        self._Man__yco += x_val

    def get_life(self):
        '''Returns enemy life'''
        return self._life

    def set_life(self, x_val):
        '''Sets enemy life'''
        self._life -= x_val

    def createboss(self, grid):
        '''Function for creating boss'''
        with open("./dragon.txt") as obj:
            for line in obj:
                self.__boss.append(line.strip('\n'))

        for i in range(13):
            for j in range(41):
                grid[15+i][458+j] = self.__boss[i][j]

    def bossdisappear(self, grid):
        '''Function to clear Boss'''
        for i in range(self._Man__yco, self._Man__yco + 13):
            for j in range(self._Man__xco, self._Man__xco + 41):
                grid[i][j] = " "

    def bossappear(self, grid):
        '''Function to print Boss'''
        for i in range(self._Man__yco, self._Man__yco + 13):
            for j in range(self._Man__xco, self._Man__xco + 41):
                grid[i][j] = self.__boss[i-self._Man__yco][j-self._Man__xco]

    def bullets(self, grid, y_val):
        '''Function for bullets'''
        grid[y_val][456] = "("
        self.__list1.append(y_val)
        self.__list2.append(456)

    def movebullets(self, grid, life, w_val):
        '''Function to move bullets'''
        for x in range(0, len(self.__list2)):
            if self.__list2[x]-1 > 387:
                grid[self.__list1[x]][self.__list2[x]] = " "
                if grid[self.__list1[x]][self.__list2[x]-1] in ["@", "O", "^", Fore.GREEN + "@" + Style.RESET_ALL, Fore.GREEN + "O" + Style.RESET_ALL, Fore.GREEN + "^" + Style.RESET_ALL]:
                    if w_val != 1:
                        life -= 1
                    self.__list1[x] = 0
                    self.__list2[x] = 0
                else:
                    grid[self.__list1[x]][self.__list2[x]-1] = "("
            self.__list2[x] -= 1
        return life

class Enemy(Man):
    '''Class for creating small enemies'''
    def __init__(self, xco, yco):
        Man.__init__(self, xco, yco)

    def createboss(self, grid, y_val):
        '''function to create small enemies'''
        grid[24][y_val] = "O"
        grid[25][y_val] = ":"
        grid[26][y_val] = ":"
        grid[27][y_val] = "<"
