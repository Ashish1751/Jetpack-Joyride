'''Module to run the game'''
import os
import time
import random
import signal
from colorama import Fore, Style
from board import Board
from background import ObstacleH, ObstacleD, ObstacleV, Coins, Magnet
from enemy import BossEnemy, Enemy
from mandalorian import Mando
from alarmexception import AlarmException
from getch import _getChUnix as getChar

ROWS, COLS = (30, 500)
ARR = [[" " for i in range(COLS)] for j in range(ROWS)]
# coin = Fore.LIGHTCYAN_EX + "$" + Style.RESET_ALL
# ground = Fore.YELLOW + "X" + Style.RESET_ALL

B = Board()
B.create_sky(ARR, COLS)
B.create_ground(ARR, ROWS, COLS)
O1 = ObstacleH(ARR)
O2 = ObstacleD(ARR)
O3 = ObstacleV(ARR)
O4 = Coins()
O5 = Magnet(ARR)
E = BossEnemy(458, 15)
E1 = Enemy(24, 50)
E.createboss(ARR)

O5Y1 = random.randint(100, 150)
O5Y2 = random.randint(250, 300)
O5.create_obstacle(0, O5Y1)
O5.create_obstacle(0, O5Y2)

for i in range(1, 8):
    y2 = random.randint(50*i+31, 50*i+49)
    E1.createboss(ARR, y2)
    for j in range(1, 3):
        y1 = random.randint(50*i, 50*i + 30)
        if j == 1:
            x1 = random.randint(4, 9)
        else:
            x1 = random.randint(17, 22)
        choice = random.randint(0, 100)%4
        if choice == 0:
            O4.create_coins(x1, y1, ARR)
        elif choice == 1:
            O1.create_obstacle(x1, y1)
        elif choice == 2:
            O2.create_obstacle(x1, y1)
        elif choice == 3:
            O3.create_obstacle(x1, y1)

def movemando():
    ''' Method for movement of mandalorian'''
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.25):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    char = user_input()
    print(char)

    if char == "Q":
        quit()

    elif char == " ":
        if MANDO.get_start() == 0 or round(time.time())-MANDO.get_start() > 60:
            MANDO.shield_activate(round(time.time()))

    elif char == 'd' and MANDO.get_x() + 3 < 458:
        MANDO.disappear(ARR)
        if(MANDO.get_x() + 3 < MANDO.get_a() + 110 and MANDO.get_x() + 3 < 458):
            MANDO.set_x(1) #= MANDO._Man__xco + 1
            MANDO.coincheck(ARR, 0)
        if(MANDO.get_x() > O5Y1 -1 and MANDO.get_x() < O5Y1 + 30 and MANDO.get_x() + 4 < MANDO.get_a() + 110):
            MANDO.set_x(2) #= MANDO._Man__xco + 2
            MANDO.coincheck(ARR, 0)
        if(MANDO.get_x() > O5Y2 -1 and MANDO.get_x() < O5Y2 + 30 and MANDO.get_x() + 4 < MANDO.get_a() + 110):
            MANDO.set_x(2) #= MANDO._Man__xco + 2
            MANDO.coincheck(ARR, 0)
        MANDO.appear(ARR)
        MANDO.collisioncheck(ARR, 0, MANDO.get_a())

    elif char == 'a':
        MANDO.disappear(ARR)
        if MANDO.get_x() > MANDO.get_a() +1:
            MANDO.set_x(-2) #= MANDO._Man__xco - 2
            MANDO.coincheck(ARR, 1)
        if(MANDO.get_a() > 389 and MANDO.get_x() > 390):
            MANDO.set_x(-2) #= MANDO._Man__xco - 2
            MANDO.coincheck(ARR, 1)
        MANDO.appear(ARR)
        MANDO.collisioncheck(ARR, 1, MANDO.get_a())

    # elif char == "w":
    #     MANDO.disappear(ARR)
    #     E.bossdisappear(ARR)
    #     if(MANDO._Man__yco>2):
    #         if(MANDO.get_a() > 389 and e._Man__yco > 2):
    #             e._Man__yco = e._Man__yco - 2
    #         MANDO._Man__yco = MANDO._Man__yco - 2
    #         MANDO.coincheck(ARR, 2)
    #         MANDO.collisioncheck(ARR, 2, MANDO.get_a())
    #     MANDO.appear(ARR)
    #     E.bossappear(ARR)

    elif char == "w":
        if MANDO.get_a() > 389:
            MANDO.disappear(ARR)
            E.bossdisappear(ARR)
            if MANDO.get_y() > 2:
                if(MANDO.get_a() > 389 and E.get_y() > 2):
                    E.set_y(-2) #= e._Man__yco - 2
                MANDO.set_y(-2) #= MANDO._Man__yco - 2
                MANDO.coincheck(ARR, 2)
                MANDO.collisioncheck(ARR, 2, MANDO.get_a())
            MANDO.appear(ARR)
            E.bossappear(ARR)
        else:
            if(MANDO.get_y() > 16 and MANDO.get_y() < 25):
                MANDO.disappear(ARR)
                MANDO.set_y(-2) #= MANDO._Man__yco - 2
                MANDO.coincheck(ARR, 2)
                MANDO.collisioncheck(ARR, 2, MANDO.get_a())
                MANDO.appear(ARR)
            elif(MANDO.get_y() > 7 and MANDO.get_y() < 17):
                # MANDO.disappear(ARR)
                l_val = MANDO.get_life()
                for i in range(2):
                    MANDO.disappear(ARR)
                    MANDO.set_y(-2) #= MANDO._Man__yco - 2
                    MANDO.coincheck(ARR, 2)
                    MANDO.collisioncheck(ARR, 2, MANDO.get_a())
                MANDO.appear(ARR)
                if l_val != MANDO.get_life():
                    MANDO.set_life(l_val - 1)
            elif(MANDO.get_y() > 4 and MANDO.get_y() < 8):
                l_val = MANDO.get_life()
                for i in range(3):
                    MANDO.disappear(ARR)
                    MANDO.set_y(-2) #= MANDO._Man__yco - 2
                    MANDO.coincheck(ARR, 2)
                    MANDO.collisioncheck(ARR, 2, MANDO.get_a())
                    MANDO.appear(ARR)
                if l_val != MANDO.get_life():
                    MANDO.set_life(l_val - 1)

    elif char == "s" and MANDO.get_g() == 0:
        MANDO.set_g(1)
        l_val = MANDO.get_life()

        if(MANDO.get_a() < 389 and MANDO.get_x() + 50 < MANDO.get_a() + 110):
            MANDO.disappear(ARR)
            MANDO.set_a(10)
            MANDO.set_x(10) #+= 10
            MANDO.appear(ARR)
        MANDO.set_life(l_val)

    elif char == "b":
        MANDO.bullets(ARR, MANDO.get_y(), MANDO.get_x()+4)

MANDO = Mando(0, 24)
MANDO.appear(ARR)
MANDO.set_a(0)
# p=1
START = round(time.time())

while True:
    os.system('clear')
    T = 150-round(time.time()) + START
    print("LIVES:", MANDO.get_life(), end='\t \t')
    print("SCORE:", MANDO.get_score(), end='\n')
    print("ENEMY LIVES:", E.get_life(), end='\t \t')
    print("TIME REMAINING:", T)
    if T == 0:
        print("Time Up")
        quit()
    B.print_board(ARR, ROWS, MANDO.get_a())
    MANDO.collisioncheck(ARR, 0, MANDO.get_a())
    movemando()
    MANDO.magneticeffect(ARR, O5Y1, O5Y2)
    MANDO.disappear(ARR)
    MANDO.set_a(1)

    if MANDO.get_shield() == 1 and round(time.time()) - MANDO.get_start() == 10:
        MANDO.shield_deactivate()
    if(ARR[16][O5Y1] == " " or ARR[16][O5Y2] == " "):
        ARR[16][O5Y1] = ARR[16][O5Y2] = "🧲"

    if MANDO.get_a() < 389:
        MANDO.set_x(1) #= MANDO._Man__xco + 1
        MANDO.coincheck(ARR, 0)
    MANDO.appear(ARR)

    FLAG = 0
    R1 = E.get_y()
    for x in range(R1, R1 + 14):
        if ARR[x][457] == ")":
            ARR[x][457] = " "
        if ARR[x][457] == Fore.LIGHTYELLOW_EX + ")" + Style.RESET_ALL:
            ARR[x][457] = " "
            FLAG = 1
            break

    if FLAG == 1:
        FLAG = 0
        E.set_life(1)

    for x in range(1, 27):
        if ARR[x][457] == ")":
            ARR[x][457] = " "
        if ARR[x][457] == Fore.LIGHTYELLOW_EX + ")" + Style.RESET_ALL:
            ARR[x][457] = " "

    #     if (MANDO._Man__yco+p+3<27 and ARR[MANDO._Man__yco+p+3][MANDO._Man__xco+2] != ground and ARR[MANDO._Man__yco+3+p][MANDO._Man__xco+1] != ground and ARR[MANDO._Man__yco+3+p][MANDO._Man__xco] != ground):
    #         MANDO.disappear(ARR)
    #         E.bossdisappear(ARR)
    #         MANDO.collisioncheck(ARR, 3, MANDO.get_a()) # Need to change if p is implemented
    #         if(e._Man__yco+12<27):
    #             e._Man__yco += 1
    #         MANDO._Man__yco = MANDO._Man__yco + p
    #         MANDO.coincheck(ARR, 3) # Need to change if p is implemented
    #         MANDO.appear(ARR)
    #         E.bossappear(ARR)
    #         # p=p+1
    #     else:
    #         p=1
    #         if (ARR[MANDO._Man__yco+p+3][MANDO._Man__xco+2] in [" ", coin] and ARR[MANDO._Man__yco+3+p][MANDO._Man__xco+1] in [" ", coin] and ARR[MANDO._Man__yco+3+p][MANDO._Man__xco] in [" ", coin]):
    #             MANDO.disappear(ARR)
    #             MANDO._Man__yco = MANDO._Man__yco + p
    #             MANDO.appear(ARR)

    #         E.bossdisappear(ARR)
    #         if(e._Man__yco+12<27 and ARR[MANDO._Man__yco+p+3][MANDO._Man__xco+2] == ground and ARR[MANDO._Man__yco+3+p][MANDO._Man__xco+1] == ground and ARR[MANDO._Man__yco+3+p][MANDO._Man__xco] == ground):
    #             e._Man__yco += 1
    #         E.bossappear(ARR)

    if MANDO.get_a() > 389:
        MANDO.disappear(ARR)
        E.bossdisappear(ARR)
        if MANDO.get_y() + 4 < 28:
            if(MANDO.get_a() > 389 and E.get_y() + 12 < 27):
                E.set_y(1) #= e._Man__yco + 1
            MANDO.set_y(1) #= MANDO._Man__yco + 1
            MANDO.collisioncheck(ARR, 3, MANDO.get_a())
        MANDO.appear(ARR)
        E.bossappear(ARR)
    else:
        if(MANDO.get_y() > 14 and MANDO.get_y() < 24):
            MANDO.disappear(ARR)
            MANDO.set_y(1) #= MANDO._Man__yco + 1
            MANDO.coincheck(ARR, 3)
            MANDO.collisioncheck(ARR, 3, MANDO.get_a())
            MANDO.appear(ARR)
        elif(MANDO.get_y() > 7 and MANDO.get_y() < 15):
            l_val = MANDO.get_life()
            # MANDO.disappear(ARR)
            for i in range(2):
                MANDO.disappear(ARR)
                MANDO.set_y(1) #= MANDO._Man__yco + 1
                MANDO.coincheck(ARR, 3)
                MANDO.collisioncheck(ARR, 3, MANDO.get_a())
                MANDO.appear(ARR)
            if l_val != MANDO.get_life():
                MANDO.set_life(l_val - 1)
        elif(MANDO.get_y() > -2 and MANDO.get_y() < 8):
            l_val = MANDO.get_life()
            for i in range(3):
                MANDO.disappear(ARR)
                MANDO.set_y(1) #= MANDO._Man__yco + 1
                MANDO.coincheck(ARR, 3)
                MANDO.collisioncheck(ARR, 3, MANDO.get_a())
                MANDO.appear(ARR)
            if l_val != MANDO.get_life():
                MANDO.set_life(l_val - 1)

    MANDO.movebullets(ARR)
    if(MANDO.get_a() > 389 and MANDO.get_a()%8 == 0):
        E.bullets(ARR, MANDO.get_y())
    if MANDO.get_a() > 389:
        U = E.movebullets(ARR, MANDO.get_life(), MANDO.get_shield())
        MANDO.set_life(U)
    if E.get_life() <= 0:
        os.system('clear')
        print("LIVES:", MANDO.get_life(), end='\t \t')
        print("SCORE:", MANDO.set_score(0), end='\n')
        print("ENEMY LIVES:", E.get_life(), end='\t \t')
        print("TIME REMAINING:", T)
        print("You Won")
        quit()
    if MANDO.get_life() <= 0:
        os.system('clear')
        print("LIVES:", MANDO.get_life(), end='\t \t')
        print("SCORE:", MANDO.set_score(1), end='\n')
        print("ENEMY LIVES:", E.get_life(), end='\t \t')
        print("TIME REMAINING:", T)
        print("You Loose")
        quit()
