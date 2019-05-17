#-*- coding: utf-8 -*-

# Ivan Guillen
# CPTR 108
# May 3, 2019

# Minesweeper Project:

import mineFunctions
import sys

bombs = 0
remain = -1

print("Welcome to Minesweeper!")
print('\t')
print("1) Start New Game")
print("2) Load Saved Game")
print('\t')

option = mineFunctions.errorCheck("What would you like to do: ", 0, 2)
    
if (option == 1):
    print('\t')
    print("Your table must have at least 8 rows and at most 20 rows")
    print("Your table must have at least 8 columns and at most 30 columns")
    print('\t')
    row = mineFunctions.errorCheck("How many rows would you like your table to have: ", 7, 20)
    col = mineFunctions.errorCheck("How many columns would you like your table to have: ", 7, 30)
    table = [['o'] * col for i in range(row)]
    key = [['O'] * col for i in range(row)]
    print('\t')
    mineFunctions.randNums(key)
    mineFunctions.assignBombs(key)
    mineFunctions.printTable(table, col)
    
print('\t')

bombs = mineFunctions.numberOfBombs(key)

while (bombs != remain):
    print("1) Select block")
    print("2) Place flag")
    print("3) Save Game to File and Exit")
    print("4) End Game Without Saving")
    print('\t')
    
    option2 = mineFunctions.errorCheck("What would you like to do: ", 0, 5)
    
    if (option2 == 1):
        print('\t')
        counter = 0
        mineFunctions.printTable(table, col)
        x = mineFunctions.errorCheck("Row #: ", 0, row) - 1
        y = mineFunctions.errorCheck("Column #: ", 0, col) - 1
        mineFunctions.reveal(x, y, table, key, row, col)
        while (counter < 20):
            if (table[x][y] == 0):
                for i in range(len(table)):
                    for j in range(len(table[i])):
                        if (table[i][j] == 0):
                            mineFunctions.revealNeighbors(i, j, table, key, row, col)
            counter += 1
        remain = mineFunctions.remainingSpaces(table)
        print('\t')
        if (mineFunctions.gameOver(x, y, key) == True):
            mineFunctions.printTable(key, col)
            print('\t')
            print("You have hit a bomb.")
            sys.exit("GAME OVER")
        elif (bombs == remain):
            print('\t')
            mineFunctions.printTable(table, col)
            mineFunctions.printTable(key, col)
            sys.exit("Congratulations! You won!")
        else:
            mineFunctions.printTable(table, col)
            print('\t')
            
    if (option2 == 2):
        print('\t')
        mineFunctions.printTable(table, col)
        x = mineFunctions.errorCheck("Row #: ", 0, row) - 1
        y = mineFunctions.errorCheck("Column #: ", 0, col) - 1
        table[x][y] = 'F'
        print('\t')
        mineFunctions.printTable(table, col)

    if (option2 == 3):
        print('\t')
        mineFunctions.writeToFile(table)
        print('\t')
        sys.exit("Goodbye!")
        
    if (option2 == 4):
        print('\t')
        sys.exit("Goodbye!")