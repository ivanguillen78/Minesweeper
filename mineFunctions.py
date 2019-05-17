#-*- coding: utf-8 -*-

from __future__ import print_function
from random import randint

def printTable(table, length):
    print("   |", end = ' ')
    for k in range(length):
        if (k < 9):
            print(k + 1, end = " | ")
        else:
            print(k + 1, end = "| ")
    print('\t')
    for i in range(len(table)):
        print('——— ' * (length + 1))
        if (i < 9):
            print("", i + 1, "| ", end = "")
        else:
            print(i + 1, "| ", end = "")
        for j in range(len(table[i])):
            if (table[i][j] == 0):
                print("  |", end = ' ')
            else:
                print(table[i][j], "|", end = ' ')
        print()
    print('——— ' * (length + 1))
    print('\t')

def randNums(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = randint(1, 100)

def assignBombs(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if (table[i][j] > 20):
                table[i][j] = 0
            else:
                table[i][j] = '*'

def gameOver(x, y, key):
    if (key[x][y] == '*'):
        return True
    return False
    
def writeToFile(table):
    fileName = raw_input("File name: ")
    with open(fileName, "w") as file:
        for i in range(len(table)):
            for j in range(len(table[i])):
                file.write(table[i][j])
                file.write(" ")
            file.write('\n')
    
def errorCheck(prompt, low, high):
    while True:
        try:
            value = input(prompt)
        except NameError:
            print("Please enter a number")
            continue
        except SyntaxError:
            print("Please enter a number")
            continue
        if (value <= low or value > high):
            print("Please enter a value between", end = " ")
            print(low + 1, end = " ")
            print("and", end = " ")
            print(high)
            continue
        else:
            break
    return value
    
def numberOfBombs(key):
    bombs = 0
    for i in range(len(key)):
        for j in range(len(key[i])):
            if (key[i][j] == '*'):
                bombs += 1
    return bombs
    
def remainingSpaces(table):
    spaces = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if (table[i][j] == 'o'):
                spaces += 1
    return spaces

def reveal(x, y, table, key, rowSize, colSize):
    bombCounter = 0
    if (x == 0 and y == 0):
        if (key[x][y + 1] == '*'):
            bombCounter += 1
        if (key[x + 1][y] == '*'):
            bombCounter += 1
        if (key[x + 1][y + 1] == '*'):
            bombCounter += 1
        table[x][y] = bombCounter
    elif (x == 0 and y == colSize - 1):
        if (key[x][y - 1] == '*'):
            bombCounter += 1
        if (key[x + 1][y - 1] == '*'):
            bombCounter += 1
        if (key[x + 1][y] == '*'):
            bombCounter += 1
        table[x][y] = bombCounter
    elif (x == rowSize - 1 and y == 0):
        if (key[x - 1][y] == '*'): # Top middle
            bombCounter += 1
        if (key[x - 1][y + 1] == '*'): # Top right
            bombCounter += 1
        if (key[x][y + 1] == '*'): # Middle right
            bombCounter += 1
        table[x][y] = bombCounter
    elif (x == rowSize - 1 and y == colSize - 1):
        if (key[x - 1][y] == '*'): # Top middle
            bombCounter += 1
        if (key[x - 1][y - 1] == '*'): # Top left
            bombCounter += 1
        if (key[x][y - 1] == '*'): # Middle left
            bombCounter += 1
        table[x][y] = bombCounter    
    elif (x > 0 and x < rowSize - 1 and y == colSize - 1):
        if (key[x - 1][y - 1] == '*'): # Top left
            bombCounter += 1
        if (key[x - 1][y] == '*'): # Top middle
            bombCounter += 1
        if (key[x][y - 1] == '*'): # Middle left
            bombCounter += 1       
        if (key[x + 1][y - 1] == '*'): # Bottom left
            bombCounter += 1
        if (key[x + 1][y] == '*'): #Bottom middle
            bombCounter += 1
        table[x][y] = bombCounter
    elif (x > 0 and x < rowSize - 1 and y == 0):
        if (key[x - 1][y] == '*'): # Top middle
            bombCounter += 1
        if (key[x + 1][y] == '*'): #Bottom middle
            bombCounter += 1
        if (key[x + 1][y + 1] == '*'): #Bottom right
            bombCounter += 1
        if (key[x - 1][y + 1] == '*'): # Top right
            bombCounter += 1
        if (key[x][y + 1] == '*'): # Middle right
            bombCounter += 1
        table[x][y] = bombCounter
    elif (x == 0 and y > 0 and y < colSize - 1):
        if (key[x][y - 1] == '*'): # Middle left
            bombCounter += 1
        if (key[x][y + 1] == '*'): # Middle right
            bombCounter += 1
        if (key[x + 1][y - 1] == '*'): # Bottom left
            bombCounter += 1
        if (key[x + 1][y] == '*'): #Bottom middle
            bombCounter += 1
        if (key[x + 1][y + 1] == '*'): #Bottom right
            bombCounter += 1
        table[x][y] = bombCounter
    elif (x == rowSize - 1 and y > 0 and y < colSize - 1):
        if (key[x - 1][y - 1] == '*'): # Top left
            bombCounter += 1
        if (key[x - 1][y] == '*'): # Top middle
            bombCounter += 1
        if (key[x - 1][y + 1] == '*'): # Top right
            bombCounter += 1
        if (key[x][y - 1] == '*'): # Middle left
            bombCounter += 1
        if (key[x][y + 1] == '*'): # Middle right
            bombCounter += 1
        table[x][y] = bombCounter
    else:    
        if (key[x - 1][y - 1] == '*'): # Top left
            bombCounter += 1
        if (key[x - 1][y] == '*'): # Top middle
            bombCounter += 1
        if (key[x - 1][y + 1] == '*'): # Top right
            bombCounter += 1
        if (key[x][y - 1] == '*'): # Middle left
            bombCounter += 1
        if (key[x][y + 1] == '*'): # Middle right
            bombCounter += 1
        if (key[x + 1][y - 1] == '*'): # Bottom left
            bombCounter += 1
        if (key[x + 1][y] == '*'): #Bottom middle
            bombCounter += 1
        if (key[x + 1][y + 1] == '*'): #Bottom right
            bombCounter += 1
    table[x][y] = bombCounter
    
def revealNeighbors(i, j, table, key, row, col):
    if (i == 0 and j == 0):
        reveal(i + 1, j, table, key, row, col) # Bottom middle reveal
        reveal(i, j + 1, table, key, row, col) # Middle right reveal
        reveal(i + 1, j + 1, table, key, row, col) # Bottom right reveal
    elif (i == 0 and j == col - 1): # Top right boundary
        reveal(i + 1, j, table, key, row, col) # Bottom middle reveal
        reveal(i, j - 1, table, key, row, col) # Middle left reveal
        reveal(i + 1, j - 1, table, key, row, col) # Bottom left reveal
    elif (i == row - 1 and j == 0): # Bottom left boundary
        reveal(i - 1, j, table, key, row, col) # Top middle reveal
        reveal(i - 1, j + 1, table, key, row, col) # Top right reveal
        reveal(i, j + 1, table, key, row, col) # Middle right reveal
    elif (i == row - 1 and j == col - 1): # Bottom right boundary
        reveal(i - 1, j, table, key, row, col) # Top middle reveal
        reveal(i - 1, j - 1, table, key, row, col) # Top left reveal
        reveal(i, j - 1, table, key, row, col) # Middle left reveal
    elif (i > 0 and i < row - 1 and j == col - 1): # Right boundary
        reveal(i - 1, j - 1, table, key, row, col) # Top left reveal
        reveal(i - 1, j, table, key, row, col) # Top middle reveal
        reveal(i, j - 1, table, key, row, col) # Middle left reveal
        reveal(i + 1, j - 1, table, key, row, col) # Bottom left reveal
        reveal(i + 1, j, table, key, row, col) # Bottom middle reveal
    elif (i > 0 and i < row - 1 and j == 0): # Left boundary
        reveal(i - 1, j, table, key, row, col) # Top middle reveal
        reveal(i - 1, j + 1, table, key, row, col) # Top right reveal
        reveal(i, j + 1, table, key, row, col) # Middle right reveal
        reveal(i + 1, j, table, key, row, col) # Bottom middle reveal
        reveal(i + 1, j + 1, table, key, row, col) # Bottom right reveal
    elif (i == 0 and j > 0 and j < col - 1): # Top boundary
        reveal(i, j - 1, table, key, row, col) # Middle left reveal
        reveal(i, j + 1, table, key, row, col) # Middle right reveal
        reveal(i + 1, j - 1, table, key, row, col) # Bottom left reveal
        reveal(i + 1, j, table, key, row, col) # Bottom middle reveal
        reveal(i + 1, j + 1, table, key, row, col) # Bottom right reveal
    elif (i == row - 1 and j > 0 and j < col - 1): # Bottom boundary
        reveal(i - 1, j - 1, table, key, row, col) # Top left reveal
        reveal(i - 1, j, table, key, row, col) # Top middle reveal
        reveal(i - 1, j + 1, table, key, row, col) # Top right reveal
        reveal(i, j - 1, table, key, row, col) # Middle left reveal
        reveal(i, j + 1, table, key, row, col) # Middle right reveal
    else:
        reveal(i - 1, j - 1, table, key, row, col) # Top left reveal
        reveal(i - 1, j, table, key, row, col) # Top middle reveal
        reveal(i - 1, j + 1, table, key, row, col) # Top right reveal
        reveal(i, j - 1, table, key, row, col) # Middle left reveal
        reveal(i, j + 1, table, key, row, col) # Middle right reveal
        reveal(i + 1, j - 1, table, key, row, col) # Bottom left reveal
        reveal(i + 1, j, table, key, row, col) # Bottom middle reveal
        reveal(i + 1, j + 1, table, key, row, col) # Bottom right reveal