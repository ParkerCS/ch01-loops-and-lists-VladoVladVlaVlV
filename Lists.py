# There is no check for a draw in tic-tac-toe
# nice work on the game though.
# There are some places where the code could be more efficient.  Particularly in the checks.  You check both x and o for every combination.
# Think about the DRY principle.
# It would be easier to send the player (x or o) to the check.  This would be easier than copy paste and adding unnecessary lines of code and conditional checks. 

# LISTS (35PTS TOTAL)
# In these exercises you write functions. Of course, you should not only write the functions,
# you should also write code to test them. For practice, you should also comment your
# functions as explained above.
import random

# PROBLEM 1 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = ["It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
               "Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful"]


def magicball():
    question = input("Ask the magic ball anything: ")
    if question:
        print(answer_list[random.randrange(len(answer_list))])


magicball()





# PROBLEM 2 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
def deckprinter():
    suit = ["Heart", "Diamond", "Club", "Spade"]
    value = []
    deck = []
    for i in range(2, 11):
        value.append(i)
    value.extend(["J", "Q", "K", "A"])

    for i in range(13):
        for j in range(4):
            deck.append(str(value[i]) + " of " + str(suit[j]))
    for i in range(52):
        deck[i] = deck[random.randrange(1, 52)]
    print(deck)


deckprinter()


# PROBLEM 3 (The sieve of Eratosthenes - 10pts)
# The sieve of Eratosthenes is a method to find all prime numbers between
# 1 and a given number using a list. This works as follows: Fill the list with the sequence of
# numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime.
# Now loop over the list. Find the next number on the list that is not zero,
# which, at the start, is the number 2. Now set all multiples of this number to zero.
# Then find the next number on the list that is not zero, which is 3.
# Set all multiples of this number to zero. Then the next number, which is 5
# (because 4 has already been set to zero), and do the same thing again.
# Process all the numbers of the list in this way. When you have finished,
# the only numbers left on the list are primes.
# Use this method to determine all the primes between 1 and 1000.

def eras(n):
    number_list = []
    new_list = []

    for i in range(1, n + 1):
        number_list.append(i)
    number_list[0] = 0
    for i in range(1, len(number_list)):
        if number_list[i] != 0:
            new_list.append(number_list[i])
            for j in range(i + 1, len(number_list)):
                if number_list[j] % number_list[i] == 0:
                    number_list[j] = 0
    print(new_list)


# eras(1000)



# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def show_board():
    print(" ", board[0][0], "|", board[1][0], "|", board[2][0])
    print("--------------")
    print(" ", board[0][1], "|", board[1][1], "|", board[2][1])
    print("--------------")
    print(" ", board[0][2], "|", board[1][2], "|", board[2][2])


def win_check():
    if board[0][0] == board[1][0] == board[2][0] == "X" :
        print("X Wins")
        return 1
    elif board[0][0] == board[1][0] == board[2][0] == "O":
        print("O wins")
        return 1
    elif board[0][1] == board[1][1] == board[2][1] == "X" :
        print("X wins")
        return 1
    elif board[0][1] == board[1][1] == board[2][1] == "O":
        print("O wins")
        return 1
    elif board[0][2] == board[1][2] == board[2][2] == "X":
        print("X wins")
        return 1
    elif board[0][2] == board[1][2] == board[2][2] == "O":
        print("O wins")
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        print("X wins")
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        print("O wins")
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print("X wins")
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        print("O wins")
        return 1
    elif board[0][0] == board[0][1] == board[0][2] == "X":
        print("X wins")
        return 1
    elif board[0][0] == board[0][1] == board[0][2] == "O":
        print("O wins")
        return 1
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        print("X wins")
        return 1
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        print("O wins")
        return 1
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print("X wins")
        return 1
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print("O wins")
        return 1
    elif board[0][0] != board[1][0] != board[2][0] != board[0][1] != board[1][1] != board[2][1] != board[0][2] != \
            board[1][2] != board[2][2]:
        print("Tie")
        return 1


def mainfunc():
    i = 0
    done = False
    '''
    def choose(i):
        m=0
        row = input("Choose your row: ")
        row = int(row)
        colum = input("Choose your column: ")
        colum = int(colum)
        if (row <= 3 > 0) and (colum <= 3 > 0):
            if board[colum - 1][row - 1] != "X" and board[colum - 1][row - 1] != "O":
                if i % 2 == 0:
                    board[colum - 1][row - 1] = "X"
                else:
                    board[colum - 1][row - 1] = "O"
                show_board()

            else:
                print("Sorry the spot is taken")
                i-=1
        else:
            print("Sorry that point does not exist")
            i-=1
        return i
    '''
    while not done:
        win_check()
        win = win_check()
        if win == 1:
            done = True

        i += 1
        row = input("Choose your row: ")
        row = int(row)
        colum = input("Choose your column: ")
        colum = int(colum)
        if (row <= 3 > 0) and (colum <= 3 > 0):
            if board[colum - 1][row - 1] != "X" and board[colum - 1][row - 1] != "O":
                if i % 2 == 0:
                    board[colum - 1][row - 1] = "X"
                else:
                    board[colum - 1][row - 1] = "O"
                show_board()

            else:
                print("Sorry the spot is taken")
                i -= 1
        else:
            print("Sorry that point does not exist")
            i -= 1




mainfunc()


# The main program will be something along the lines of (in pseudo-code):
# display board
# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player

# CHALLENGE PROBLEM 5 (Battleship NO CREDIT, JUST IF YOU WANT TO TRY IT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
