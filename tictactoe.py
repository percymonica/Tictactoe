import pygame, sys
import numpy as np

pygame.init()

#constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (200,0,0)
WINLINECOLOR = (200,200,200)
BG_COLOR = (28,100,156)
LINE_COLOR = (50,50,100)

#screen specifications
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )  
pygame.display.set_caption('TICTACTOE')
screen.fill( BG_COLOR )

#console board
board=np.zeros( (BOARD_ROWS,BOARD_COLS) )



def draw_lines():
    #1st horizontal line
    pygame.draw.line( screen,LINE_COLOR, (0,200), (600,200), LINE_WIDTH)  #func(screen,colorline,linestartingpoint,lineendingpoint,linewidth)
    #2nd horizontal line
    pygame.draw.line( screen,LINE_COLOR, (0,400), (600,400), LINE_WIDTH) 

    #1st vertical
    pygame.draw.line( screen,LINE_COLOR, (200,0), (200,600), LINE_WIDTH) 
    #2nd vertical
    pygame.draw.line( screen,LINE_COLOR, (400,0), (400,600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:     #if equal to 1 player1 is drawing
                pygame.draw.circle( screen, RED, (int(col*200+100),int(row*200+100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen,RED,(col*200+SPACE,row*200+200-SPACE),(col*200+200-SPACE,row*200+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,RED,(col*200+SPACE,row*200+SPACE),(col*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)

def mark_square(row,col,player):   #to mark square in console board depending on which player marked the square
    board[row][col] = player

def available_square(row,col):     #to check availability: if square is available prints true or if not available prints false
    return board[row][col] == 0

def is_board_full():               #returns true if the board is full else returns false
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_winning_line(col,player)
            return True

    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True

    #asc diagonal win check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True

    #decs diagonal win check
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diagonal(player)
        return True
    
    return False

def draw_vertical_winning_line(col,player):
    posX=col*200+100

    if player==1:
        color=WINLINECOLOR
        print("player1 wins")
    elif player==2:
        color=WINLINECOLOR
        print("player2 wins")

    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)

def draw_horizontal_winning_line(row,player):
    posY=row*200+100

    if player==1:
        color=WINLINECOLOR
        print("player1 wins")
    elif player==2:
        color=WINLINECOLOR
        print("player2 wins")

    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)

def draw_asc_diagonal(player):
    if player==1:
        color=WINLINECOLOR
        print("player1 wins")
    elif player==2:
        color=WINLINECOLOR
        print("player2 wins")

    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_desc_diagonal(player):
    if player==1:
        color=WINLINECOLOR
        print("player1 wins")
    elif player==2:
        color=WINLINECOLOR
        print("player2 wins")

    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player=1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0


draw_lines()

player=1
game_over = False

#main loop
 #screen board
while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:   #checks whether the user clicked the screen


                    mouseX = event.pos[0] #acess x coordinate
                    mouseY = event.pos[1] #acess y coordinate

                    clicked_row = int(mouseY // 200) #makes sure in a box whwrever the mouse clicks it returns same x coordinate value
                    clicked_col = int(mouseX // 200) #makes sure in a box whwrever the mouse clicks it returns same x coordinate value

                    if available_square( clicked_row, clicked_col ):
                        if player == 1:
                            mark_square( clicked_row, clicked_col,1 )
                            if check_win(player):
                                game_over=True
                            player=2
                            
                        elif player == 2:
                            mark_square( clicked_row, clicked_col,2 )
                            if check_win(player):
                                game_over=True
                            player=1

                        draw_figures()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        restart()
                     
                        
            pygame.display.update()
