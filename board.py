'''Module for printing Board'''
from colorama import Fore, Style

class Board:
    '''Class for printing board'''
    def __init__(self):
        self.__sky = Fore.BLUE + 's' + Style.RESET_ALL
        self.__ground = Fore.YELLOW + "X" + Style.RESET_ALL

    def create_sky(self, grid, cols):
        '''Function to print sky'''
        for i in range(cols):
            grid[0][i] = self.__sky

    def create_ground(self, grid, rows, cols):
        '''Function to print ground'''
        for i in range(2):
            for j in range(cols):
                grid[rows-i-1][j] = self.__ground

    def print_board(self, grid, rows, pos): # print the board
        '''Function to print board'''
        if pos < 389:
            for i in range(rows):
                for j in range(pos, pos+110): # 110 columns at a time
                    print(grid[i][j], end='')
                print()

        elif pos >= 389:
            for i in range(rows):
                for j in range(389, 389+110): # 110 columns at a time
                    print(grid[i][j], end='')
                print()
