from itertools import count
from tkinter import N
import pygame
import numpy as np
from queue import PriorityQueue
import queue
import os
import sys
import argparse
import time

#colors
one = (246, 244, 210)
two = (203, 223, 189)

pygame.init()

size = (716, 716)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Conway's Game of Life")

width = 15
height = 15
margin = 2

grid = [[0 for x in range(44)] for y in range(44)]

done = False
clock = pygame.time.Clock()
neighbour=[]

def neighbourr():
    global grid,neighbour
    neighbour = [0 for col in range(len(grid)) for row in range(len(grid))]
    count=0
    N = len(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (i > 0 and grid[i - 1][j] == 1):
                neighbour[count]=neighbour[count]+1
            if (j > 0 and grid[i][j - 1] == 1):
                neighbour[count]=neighbour[count]+1
            if (i > 0 and j > 0 and
                grid[i - 1][j - 1] == 1):
                neighbour[count]=neighbour[count]+1
            if (i < N - 1 and grid[i + 1][j] == 1):
                neighbour[count]=neighbour[count]+1
            if (j < N - 1 and grid[i][j + 1] == 1):
                neighbour[count]=neighbour[count]+1
            if (i < N - 1 and j < N - 1
                and grid[i + 1][j + 1] == 1):
                neighbour[count]=neighbour[count]+1
            if (i < N - 1 and j > 0
                and grid[i + 1][j - 1] == 1):
                neighbour[count]=neighbour[count]+1
            if (i > 0 and j < N - 1
                and grid[i - 1][j + 1] == 1):
                neighbour[count]=neighbour[count]+1
                
            count+=1
    
               
def cgol():
    global grid,neighbour
    neighbourr()
    N = len(grid)
    arr=grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if grid[i][j]  == 1:
                if (neighbour[i*len(grid[0]) +j] < 2) or (neighbour[i*len(grid[0]) +j] > 3):
                   arr[i][j] = 0
            else:
                if neighbour[i*len(grid[0]) +j] == 3:
                    arr[i][j] = 1
    grid = arr


def cgol_auto():
    exitt = True
    while exitt:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("done")
                    exitt = False
                    break
        count = 0
        for i in range(len(grid)):
            if(1 not in grid[i]):
                count+=1
        if(count==len(grid)):
            print("done")
            exitt = False
            break
        print("wag1")
        cgol()
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    color = two
                else:
                    color = one
                pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
        pygame.display.flip()
        clock.tick(60)
        time.sleep(0.3)
        
                

def savegrid():
    global grid
    np.savetxt(r"./Downloads/Conways-Game-of-Life-main/example.txt",grid)



def loadgrid(index):
    global grid
    if(index ==0):
        grid = np.loadtxt(r"./Downloads/Conways-Game-of-Life-main/example.txt").tolist()
    elif(index ==1):
        grid = np.loadtxt(r'./Downloads/Conways-Game-of-Life-main/Ship/example.txt').tolist()
    elif(index ==2):
        grid = np.loadtxt(r'./Downloads/Conways-Game-of-Life-main/Ship2/example.txt').tolist()
    elif(index ==3):
        grid = np.loadtxt(r'./Downloads/Conways-Game-of-Life-main/Diamond/example.txt').tolist()
    elif(index ==4):
        grid = np.loadtxt(r'./Downloads/Conways-Game-of-Life-main/A for all/example.txt').tolist()
    elif(index ==5):
        grid = np.loadtxt(r'./Downloads/Conways-Game-of-Life-main/Martins/example.txt').tolist()


while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                    print("Exit")
                    pygame.quit()
             if event.key == pygame.K_s:
                 print("Saving Shape")
                 savegrid()
             if event.key == pygame.K_l:
                 print("Loading Shape")
                 loadgrid(0)
             if event.key == pygame.K_1:
                 print("Loading Shape 1")
                 loadgrid(1)
             if event.key == pygame.K_2:
                 print("Loading Shape 2")
                 loadgrid(2)
             if event.key == pygame.K_3:
                 print("Loading Shape 3")
                 loadgrid(3)
             if event.key == pygame.K_4:
                 print("Loading Shape 4")
                 loadgrid(4)
             if event.key == pygame.K_5:
                 print("Loading Shape 5")
                 loadgrid(5)
             if event.key == pygame.K_RETURN:
                cgol_auto()
                    
             if event.key == pygame.K_r:
                grid = [[0 for x in range(44)] for y in range(44)]
             if event.key == pygame.K_RIGHT :
                cgol()

        if pygame.mouse.get_pressed()[2]:
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            grid[row][column] = 0
        if pygame.mouse.get_pressed()[0]:
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            grid[row][column] = 1
        
                
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    screen.fill(two)
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                color = two
            else:
                color = one
            pygame.draw.rect(screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
