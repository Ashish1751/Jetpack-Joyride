'''Module for Mandolorian'''
from colorama import Fore, Style

class Man:
    '''Class for creating mando, enemy, boss enemy'''
    def __init__(self, xco, yco):
        self.__xco = xco
        self.__yco = yco

class Mando(Man):
    '''Class for creating mando'''
    def __init__(self, xco, yco):
        Man.__init__(self, xco, yco)
        self.__shape = [["@", "@", "@"], ["@", "@", "@"], [" ", "O", " "], ["^", "^", "^"]]
        self._life = 15
        self._coins = 0
        self._start = 0
        self._shield = 0
        self.__bx = []
        self.__by = []
        self._a = 0
        self._g = 0
        self._score = 0
        self._gr = 0

    def get_x(self):
        '''Returns x coordinate'''
        return self._Man__xco

    def set_x(self, x_val):
        '''Sets x coordinate'''
        self._Man__xco += x_val

    def get_y(self):
        '''Returns y coordinate'''
        return self._Man__yco

    def set_y(self, x_val):
        '''Sets y coordinate'''
        self._Man__yco += x_val

    def get_score(self):
        '''Returns score'''
        if self.get_a() < 389:
            self._score = self.get_a() *10 + self.get_coins() *90
        return self._score

    def set_score(self, x_val):
        '''Sets score'''
        if x_val == 0:
            self._score += 10000
        return self._score

    def get_start(self):
        '''Returns start'''
        return self._start

    def set_start(self, x_val):
        '''Sets start'''
        self._start = x_val

    def get_life(self):
        '''Returns life'''
        return self._life

    def set_life(self, x_val):
        '''Sets life'''
        self._life = x_val

    def get_shield(self):
        '''Returns shield'''
        return self._shield

    def set_shield(self, x_val):
        '''Sets shield'''
        self._shield = x_val

    def get_a(self):
        '''Returns a'''
        return self._a

    def set_a(self, x):
        '''Sets a'''
        self._a += x

    def get_coins(self):
        '''Returns coins'''
        return self._coins

    def set_coins(self, x_val):
        '''Sets Coins'''
        self._coins += x_val

    def get_g(self):
        '''Returns g'''
        return self._g

    def set_g(self, x_val):
        '''Sets g'''
        self._g = x_val

    def shield_activate(self, x_val):
        '''Activates Shield'''
        self.set_start(x_val)
        self.set_shield(1)
        self.__shape = [[Fore.GREEN + "@" + Style.RESET_ALL, Fore.GREEN + "@" + Style.RESET_ALL, Fore.GREEN + "@" + Style.RESET_ALL], [Fore.GREEN + "@" + Style.RESET_ALL, Fore.GREEN + "@" + Style.RESET_ALL, Fore.GREEN + "@" + Style.RESET_ALL], [" ", Fore.GREEN + "O" + Style.RESET_ALL, " "], [Fore.GREEN + "^" + Style.RESET_ALL, Fore.GREEN +  "^" + Style.RESET_ALL, Fore.GREEN +  "^" + Style.RESET_ALL]]

    def shield_deactivate(self):
        '''Deactivates Shield'''
        self.set_shield(0)
        self.__shape = [["@", "@", "@"], ["@", "@", "@"], [" ", "O", " "], ["^", "^", "^"]]

    def disappear(self, grid):
        '''Clears Mando'''
        for i in range(self._Man__yco, self._Man__yco + 4):
            for j in range(self._Man__xco, self._Man__xco + 3):
                grid[i][j] = " "

    def appear(self, grid):
        '''Prints Mando'''
        for i in range(self._Man__yco, self._Man__yco + 4):
            for j in range(self._Man__xco, self._Man__xco + 3):
                grid[i][j] = self.__shape[i-self._Man__yco][j-self._Man__xco]

    def bullets(self, grid, x, y):
        '''Creates Bullets'''
        if self.get_a() > 389:
            grid[x][y] = Fore.LIGHTYELLOW_EX + ")" + Style.RESET_ALL
        else:
            grid[x][y] = ")"
        self.__bx.append(x)
        self.__by.append(y)

    def movebullets(self, grid):
        '''Moves Bullets'''
        for x in range(len(self.__by)):
            if self.get_a() > 389:
                if self.__by[x] + 1 < 458:
                    grid[self.__bx[x]][self.__by[x]] = " "
                    grid[self.__bx[x]][self.__by[x] +1] = Fore.LIGHTYELLOW_EX + ")" + Style.RESET_ALL
                    self.__by[x] += 1
            else:
                if self.__by[x] + 2 < 458:
                    grid[self.__bx[x]][self.__by[x]] = " "
                    for i in range(1, 3):
                        if grid[self.__bx[x]][self.__by[x]+i] == "O":
                            grid[24][self.__by[x]+i] = " "
                            grid[25][self.__by[x]+i] = " "
                            grid[26][self.__by[x]+i] = " "
                            grid[27][self.__by[x]+i] = " "
                            self.__by[x] = 456
                            self.set_coins(1)
                        if grid[self.__bx[x]][self.__by[x]+i] == Fore.LIGHTCYAN_EX + "$" + Style.RESET_ALL:
                            self.set_coins(1)
                            grid[self.__bx[x]][self.__by[x]+i] = " "
                    if(grid[self.__bx[x]][self.__by[x]+2] in ["o", "\\", "|", "-"] or grid[self.__bx[x]][self.__by[x]+1] in ["o", "\\", "|", "-"]):
                        t_val = self.__by[x] - (self.__by[x]%50)
                        if(self.__bx[x] > 3 and self.__bx[x] < 15):
                            for i in range(4, 15):
                                for j in range(t_val, t_val + 40):
                                    if grid[i][j] in ["o", "\\", "|", "-"]:
                                        grid[i][j] = " "
                        elif(self.__bx[x] > 16 and self.__bx[x] < 28):
                            for i in range(17, 28):
                                for j in range(t_val, t_val + 40):
                                    if grid[i][j] in ["o", "\\", "|", "-"]:
                                        grid[i][j] = " "
                        self.__by[x] = 456
                    else:
                        grid[self.__bx[x]][self.__by[x]+2] = ")"
                self.__by[x] += 2

    def collisioncheck(self, grid, choice, a):
        '''Checks for collision'''
        if choice == 0:
            if (grid[self._Man__yco][self._Man__xco + 3] in ["o", "-", "\\", "|"] or grid[self._Man__yco+1][self._Man__xco + 3] in ["o", "-", "\\", "|"] or grid[self._Man__yco+2][self._Man__xco + 3] in ["o", "-", "\\", "|"] or grid[self._Man__yco+3][self._Man__xco + 3] in ["o", "-", "\\", "|"]):
                if self.get_shield() == 0:
                    self.set_life(self.get_life()-1)
                    self.disappear(grid)
                    if self._Man__xco + 12 < a + 110:
                        self._Man__xco = self._Man__xco + 10
                    self.appear(grid)
                else:
                    self.__shape = [["@", "@", "@"], ["@", "@", "@"], [" ", "O", " "], ["^", "^", "^"]]
        elif choice == 1:
            if (grid[self._Man__yco][self._Man__xco -1] in ["o", "-", "\\", "|"] or grid[self._Man__yco+1][self._Man__xco -1] in ["o", "-", "\\", "|"] or grid[self._Man__yco+2][self._Man__xco -1] in ["o", "-", "\\", "|"] or grid[self._Man__yco+3][self._Man__xco -1] in ["o", "-", "\\", "|"]):
                if self.get_shield() == 0:
                    self.set_life(self.get_life()-1)
                    self.disappear(grid)
                    if self._Man__xco + 12 < a + 110:
                        self._Man__xco = self._Man__xco + 10
                    self.appear(grid)
                else:
                    self.__shape = [["@", "@", "@"], ["@", "@", "@"], [" ", "O", " "], ["^", "^", "^"]]
        elif choice == 2:
            if (grid[self._Man__yco-1][self._Man__xco + 2] in ["o", "-", "\\", "|"] or grid[self._Man__yco-1][self._Man__xco + 1] in ["o", "-", "\\", "|"] or grid[self._Man__yco-1][self._Man__xco] in ["o", "-", "\\", "|"]):
                if self.get_shield() == 0:
                    self.set_life(self.get_life()-1)
                    self.disappear(grid)
                    if self._Man__xco + 12 < a + 110:
                        self._Man__xco = self._Man__xco + 10
                    self.appear(grid)
                else:
                    self.__shape = [["@", "@", "@"], ["@", "@", "@"], [" ", "O", " "], ["^", "^", "^"]]
        elif choice == 3:
            if (grid[self._Man__yco+4][self._Man__xco + 2] in ["o", "-", "\\", "|"] or grid[self._Man__yco+4][self._Man__xco + 1] in ["o", "-", "\\", "|"] or grid[self._Man__yco+4][self._Man__xco] in ["o", "-", "\\", "|"]):
                if self.get_shield() == 0:
                    self.set_life(self.get_life()-1)
                    self.disappear(grid)
                    if self._Man__xco + 13 < a + 110:
                        self._Man__xco = self._Man__xco + 11
                    self.appear(grid)
                else:
                    self.__shape = [["@", "@", "@"], ["@", "@", "@"], [" ", "O", " "], ["^", "^", "^"]]

    def coincheck(self, grid, choice):
        '''Checks for coins'''
        coin = Fore.LIGHTCYAN_EX + "$" + Style.RESET_ALL
        if choice == 0:
            if grid[self._Man__yco][self._Man__xco+3] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+1][self._Man__xco+3] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+2][self._Man__xco+3] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+3][self._Man__xco+3] == coin:
                self.set_coins(1)
        elif choice == 1:
            if grid[self._Man__yco][self._Man__xco-1] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+1][self._Man__xco-1] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+2][self._Man__xco-1] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+3][self._Man__xco-1] == coin:
                self.set_coins(1)
        elif choice == 2:
            if grid[self._Man__yco-1][self._Man__xco] == coin:
                self.set_coins(1)
            if grid[self._Man__yco-1][self._Man__xco+1] == coin:
                self.set_coins(1)
            if grid[self._Man__yco-1][self._Man__xco+2] == coin:
                self.set_coins(1)
        elif choice == 3:
            if grid[self._Man__yco+4][self._Man__xco] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+4][self._Man__xco+1] == coin:
                self.set_coins(1)
            if grid[self._Man__yco+4][self._Man__xco+2] == coin:
                self.set_coins(1)

    def magneticeffect(self, grid, o5y1, o5y2):
        '''creates magnetic effect'''
        if(self._Man__xco > o5y1-30 and self._Man__xco < o5y1):
            self.disappear(grid)
            if self._Man__xco + 4 < self.get_a() + 110:
               self._Man__xco += 2
               self.coincheck(grid, 0)
            self.appear(grid)
        if(self._Man__xco > o5y1 - 1 and self._Man__xco < o5y1 + 30 and self.get_a() < o5y1):
            self.disappear(grid)
            if self._Man__xco < self.get_a() + 110:
               self._Man__xco -= 2
               self.coincheck(grid, 0)
            self.appear(grid)

        if(self._Man__xco > o5y2-30 and self._Man__xco < o5y2):
            self.disappear(grid)
            if self._Man__xco + 6 < self.get_a() + 110:
               self._Man__xco += 4
               self.coincheck(grid, 0)
            self.appear(grid)
        if(self._Man__xco > o5y2 - 1 and self._Man__xco < o5y2 + 30 and self.get_a() < o5y2):
            self.disappear(grid)
            if self._Man__xco < self.get_a() + 110:
               self._Man__xco -= 2
               self.coincheck(grid, 0)
            self.appear(grid)
        self.coincheck(grid, 0)
        self.coincheck(grid, 1)
        self.coincheck(grid, 2)
        self.coincheck(grid, 3)
        self.collisioncheck(grid, 0, self.get_a())
        self.collisioncheck(grid, 1, self.get_a())
        self.collisioncheck(grid, 2, self.get_a())
        self.collisioncheck(grid, 3, self.get_a())
