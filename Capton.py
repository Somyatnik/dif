#!/usr/bin/python

import sys
import os
import pygame
import random
import time
import math

pygame.init()

back_color = (0, 0, 0)
front_color = (192, 192, 192)
pers_color = (0, 255, 0)
bot_color = (255, 0, 0)
bullet_color = (255, 255, 255)

pygame.display.set_caption("Capton")
resolution = (601, 601)
flag = 0 # pygame.FULLSCREEN
depth = 32
screen = pygame.display.set_mode(resolution, flag, depth)

show_text = False

dim = 2

cell_count_i = 30
cell_count_j = 30
cell_size = 20

x_max = cell_count_i * cell_size
y_max = cell_count_i * cell_size

block_count = 200

pole = [[0 for i in range(cell_count_i)] for j in range(cell_count_j)]
for k in range(block_count):
    i = random.randint(0, cell_count_i - 1)
    j = random.randint(0, cell_count_j - 1)
    pole[i][j] = 1

class Entity:
    def __init__(self):
   	 self.i = 0
   	 self.j = 0
   	 self.i_ = 1
   	 self.j_ = 0
    def fill(self, pole, i_max, j_max):
   	 isRun = True
   	 while isRun:
   		 self.i = random.randint(0, i_max)
   		 self.j = random.randint(0, j_max)
   		 if pole [self.i][self.j] == 0:
   			 pole[self.i][self.j] = 2
   			 isRun = False
   	 self.i_ = 1
   	 self.j_ = 0
   	 return self
    def move(self):
   	 self.i += self.i_
   	 self.j += self.j_
    def rotate(self):
   	 t = self.i_
   	 self.i_ = -self.j_
   	 self.j_ = t
    def K_LEFT(self):
   	 self.i_ = -1
   	 self.j_ = -0
    def K_RIGHT(self):
   	 self.i_ = +1
   	 self.j_ = +0
    def K_UP(self):
   	 self.i_ = -0
   	 self.j_ = -1
    def K_DOWN(self):
   	 self.i_ = +0
   	 self.j_ = +1
    def K_SPACE(self):
   	 bullet = Entity()
   	 bullet.i = self.i;
   	 bullet.j = self.j;
   	 bullet.i_ = self.i_;
   	 bullet.j_ = self.j_;
   	 return bullet
    def update(self, pole, i_max, j_max):
   	 new_i = self.i + self.i_
   	 new_j = self.j + self.j_
   	 if new_i < 0 or i_max <= new_i or new_j < 0 or j_max <= new_j or pole[new_i][new_j] > 0:
   		 self.rotate()
   	 else:
   		 pole[self.i][self.j] = 0
   		 self.move()
   		 pole[self.i][self.j] = 2
    def draw(self, screen, color, size):
   	 pygame.draw.rect(screen, color, [self.i * size, self.j * size, size, size])

entities = [Entity().fill(pole, cell_count_i - 1, cell_count_j - 1)]
entities += [Entity().fill(pole, cell_count_i - 1, cell_count_j - 1)]

bullets = []

while True:
    for event in pygame.event.get():
   	 if event.type == pygame.QUIT:
   		 pygame.quit()
   		 os._exit(0) # sys.exit(0)
   	 if event.type == pygame.KEYUP:
   		 if event.key == pygame.K_ESCAPE:
   			 pygame.quit()
   			 os._exit(0) # sys.exit(0)
   		 if event.key == pygame.K_F1:
   			 show_text = not show_text
   		 if event.key == pygame.K_F5:
   			 pole = [[0 for i in range(cell_count_i)] for j in range(cell_count_j)]
   			 for k in range(block_count):
   				 i = random.randint(0, cell_count_i - 1)
   				 j = random.randint(0, cell_count_j - 1)
   				 pole[i][j] = 1
   			 for enitty in entities:
   				 entity.fill(pole, cell_count_i - 1, cell_count_j - 1)
   		 if event.key == pygame.K_LEFT:
   			 entities[0].K_LEFT();
   		 if event.key == pygame.K_RIGHT:
   			 entities[0].K_RIGHT();
   		 if event.key == pygame.K_UP:
   			 entities[0].K_UP();
   		 if event.key == pygame.K_DOWN:
   			 entities[0].K_DOWN();
   		 if event.key == pygame.K_SPACE:
   			 bullet = entities[0].K_SPACE()
   			 bullet.update(pole, cell_count_i, cell_count_j);
   			 bullets += [bullet]

    for entity in entities:
   	 entity.update(pole, cell_count_i, cell_count_j)

    for bullet in bullets:
   	 bullet.update(pole, cell_count_i, cell_count_j)
   	 bullet.update(pole, cell_count_i, cell_count_j)

    screen.fill(back_color)  
    for j in range(cell_count_j):
   	 for i in range(cell_count_i):
   		 x = i * cell_size
   		 y = j * cell_size
   		 if pole[i][j] > 0:
   			 pygame.draw.rect(screen, front_color, [x, y, cell_size, cell_size])
   		 else:
   			 pygame.draw.rect(screen, back_color, [x, y, cell_size, cell_size])

    for i in range(cell_count_i + 1):
   	 x = i * cell_size
   	 pygame.draw.line(screen, front_color, (x, 0), (x, y_max))
    for j in range(cell_count_j + 1):
   	 y = j * cell_size
   	 pygame.draw.line(screen, front_color, (0, y), (x_max, y))

    for entity in entities:
   	 entity.draw(screen, bot_color, cell_size)
    entities[0].draw(screen, pers_color, cell_size)

    for bullet in bullets:
   	 bullet.draw(screen, bullet_color, cell_size)

    if show_text:
   	 font = pygame.font.Font(None, 16)
   	 text = font.render("Run...", 1, text_color)
   	 text_position = text.get_rect()
   	 screen.blit(text, text_position)

    pygame.display.update()

    time.sleep(0.1)

#if __name__ == "__main__":
#  main()
