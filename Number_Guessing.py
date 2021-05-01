#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on April 30, 2021
# This file runs the number guessing game


def main():
    # Function that runs the game
    print("Welcome to guess the number!\n")
    User_number = int(input("Input a number from 0-9: "))
    # User input
    Program_number = 6
    if User_number == Program_number:
        print("You have guessed the correct number!")
    else:
        print("Try again next time!")


if __name__ == "__main__":
    main()
