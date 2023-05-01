import pygame
import copy
import math

class game_of_life():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((750, 500))
        pygame.display.set_caption("GAME OF LIFE")
        self.data = [[0 for n in range(100)] for m in range(100)]
        self.board_run = True
        self.clock = pygame.time.Clock()
        self.start = False
        self.initial = True

    def get_neighbour_cell(self, m, n):
        neighbour_cell = [[m + 1, n], [m - 1, n], [m, n + 1], [m, n - 1], [m + 1, n + 1], [m - 1, n + 1],
                          [m + 1, n - 1], [m - 1, n - 1]]
        neighbour_cell = [m for m in neighbour_cell if 0 <= m[0] < 100 and 0 <= m[1] < 100]
        return neighbour_cell

    def next_generation(self):
        self.last_generation = copy.deepcopy(self.data)
        for m in range(len(self.data)):
            for n in range(len(self.data[m])):
                self.count = [self.last_generation[k[0]][k[1]] for k in self.get_neighbour_cell(m, n)].count(1)
                if self.last_generation[m][n] == 1:
                    self.data[m][n] = 1 if self.count in range(2, 4) else 0
                elif self.last_generation[m][n] == 0:
                    self.data[m][n] = 1 if self.count == 3 else 0

    def updation(self):
        self.screen.fill((0, 0, 0))
        for m in range(len(self.data)):
            for n in range(len(self.data[m])):
                if self.data[m][n] == 1:
                    pygame.draw.rect(self.screen, (255, 255, 255), (n * 10, m * 10, 10, 10))

    def user_initial(self):
        if self.initial:
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                self.data[math.floor(y / 10)][math.floor(x / 10)] = 1
            if pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                self.data[math.floor(y / 10)][math.floor(x / 10)] = 0
            if pygame.mouse.get_pressed()[1]:
                self.initial = False
                self.start = True
            self.clock.tick(60)

    def start_game(self):
        while self.board_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.board_run = False
            self.updation()
            if self.start:
                self.next_generation()
                self.clock.tick(10)
            self.user_initial()
            pygame.display.update()

game = game_of_life()
game.start_game()
