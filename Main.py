# Tic--Tac--Toe

import pygame as pg
from setting import *
import random

class Game:
    def __init__(self):
        # initiallize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.board = ['','','','','','','','','']
        self.my_turn = True
        self.player1 = 'X'
        self.player2 = 'O'
        self.empty = ''
        self.all_pos_combo = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def new(self):
        # start a new game
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - update
        pass


    def events(self):
        # Game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mx, self.my = pg.mouse.get_pos()
                print self.mx, self.my


                # the places of the blocks
                self.block_place(self.board, block0, self.player1, "block0", 0)
                self.block_place(self.board, block1, self.player1, "block1", 1)
                self.block_place(self.board, block2, self.player1, "block2", 2)
                self.block_place(self.board, block3, self.player1, "block3", 3)
                self.block_place(self.board, block4, self.player1, "block4", 4)
                self.block_place(self.board, block5, self.player1, "block5", 5)
                self.block_place(self.board, block6, self.player1, "block6", 6)
                self.block_place(self.board, block7, self.player1, "block7", 7)
                self.block_place(self.board, block8, self.player1, "block8", 8)

                # the other player('O') is playing
                if self.my_turn == False and self.is_board_full() is False:
                    self.board[self.computer_ai(self.board, self.player2, self.player1)] = self.player2
                    self.my_turn = True




    def draw(self):
        # Game loop - draw
        self.screen.fill((245,245,245))
        #self.screen.fill((45,45,45))

        #horizontal lines
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 3) , (WIDTH, HEIGHT / 3))
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 1.75) , (WIDTH, HEIGHT / 1.75))
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 1.25) , (WIDTH, HEIGHT / 1.25))

        #vertical lines
        pg.draw.line(self.screen, BLACK, (WIDTH / 3, HEIGHT / 3) , (WIDTH / 3, HEIGHT))
        pg.draw.line(self.screen, BLACK, (WIDTH / 1.5, HEIGHT / 3) , (WIDTH / 1.5, HEIGHT))


        # show to the screen the 'x' or 'o' (only printing stuff on the screen!!!)
        self.draw_on_screen(self.board, block0, 0, self.player1, self.player2, 2, 1.5)
        self.draw_on_screen(self.board, block1, 1, self.player1, self.player2, 1.32, 1.5)
        self.draw_on_screen(self.board, block2, 2, self.player1, self.player2, 1.2, 1.5)
        self.draw_on_screen(self.board, block3, 3, self.player1, self.player2, 2, 1.3)
        self.draw_on_screen(self.board, block4, 4, self.player1, self.player2, 1.3, 1.3)
        self.draw_on_screen(self.board, block5, 5, self.player1, self.player2, 1.19, 1.29)
        self.draw_on_screen(self.board, block6, 6, self.player1, self.player2, 2, 1.2)
        self.draw_on_screen(self.board, block7, 7, self.player1, self.player2, 1.31, 1.2)
        self.draw_on_screen(self.board, block8, 8, self.player1, self.player2, 1.2, 1.2)


        # Check if win, lose or tie
        for player in [self.player1, self.player2]:
            if self.is_winner(self.board, player):
                self.draw_text(player + " Win", 70, BLACK, WIDTH / 2, HEIGHT / 10)
                self.playing = False

        if self.is_board_full():
            self.draw_text("Tie", 70, BLACK, WIDTH / 2, HEIGHT / 10)
            self.playing = False


        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # the start screen
        self.screen.fill((45,45,45))
        self.draw_text("Game", 60, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Start", 60, WHITE, WIDTH / 2, HEIGHT / 2)
        pg.display.flip()
        pg.time.wait(1600)

    def show_go_screen(self):
        # the game-over screen
        self.screen.fill((45,45,45))
        self.draw_text("GAME", 60, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("OVER", 60, WHITE, WIDTH / 2, HEIGHT / 2)
        pg.display.flip()
        pg.time.wait(1200)
        quit()


    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


    def is_winner(self, board, player):
        # check if win!
        for combo in self.all_pos_combo:
            result = True
            for board_in in combo:
                if board[board_in] != player:
                    result = False

            if result == True:
                return True

        return False


    def draw_on_screen(self, board, var, num, player1, player2, _x, _y):
        if board[num] == player1:
            self.draw_text(player1, 50, BLACK, var[1] / _x, var[3] / _y)
        elif board[num] == player2:
            self.draw_text(player2, 50, BLACK, var[1] / _x, var[3] / _y)


    def block_place(self, board, var, player, name, num):
        # check the place of the each block
        if (var[0] < self.mx < var[1]) and (var[2] < self.my < var[3]) and (self.my_turn == True) and (board[num] == self.empty):
            # block0
            board[num] = player
            print name, board
            self.my_turn = False

    def is_board_full(self):
        if self.empty in self.board:
            return False
        else:
            return True



    def computer_ai(self, board, player2, player1):
        # computer movement by AI

        if board[4] == self.empty:
            return 4


        # Atackk AI
        for x, y, z in self.all_pos_combo:

            if (board[x] == player2) and (board[y] == player2) and (board[z] == self.empty):
                return z
                break

            if (board[z] == player2) and (board[y] == player2) and (board[x] == self.empty):
                return x
                break

            if (board[x] == player2) and (board[z] == player2) and (board[y] == self.empty):
                return y
                break

        # Defend AI
        for x,y,z in self.all_pos_combo:

            if (board[x] == player1) and (board[y] == player1) and (board[z] == self.empty):
                return z
                break

            if (board[z] == player1) and (board[y] == player1) and (board[x] == self.empty):
                return x
                break

            if (board[x] == player1) and (board[z] == player1) and (board[y] == self.empty):
                return y
                break

        while True:
            move = random.randint(0,8)
            if board[move] == self.empty:
                return move
                break


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    pg.time.wait(1100)
    g.show_go_screen()

pg.quit()
