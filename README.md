# Table of Contents
1. [Hangman](#hangman)
2. [Description](#description)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Licence Information](#licence-information)

# Hangman

## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Installation and Setup
```
$ git clone git@github.com:junior451/hangman.git
$ cd hangman/hangman
$ python3 milestone_5.py
```

## Usage
Once the game start, you will be prompted to enter a letter to guess the word

If you guess it correctly, you will be shown a list containing the letters you have guessed so far and in the positon of that letter in the orignal word

If you guess the wrong letter, you will be shown an output saying you have guessed it wrong and your number of lives will also be reduced and shown

If the letter you gussed has already been guessed, you will be shown an output saying "That letter has already been guessed"

When your number of lives reaches 0, you will be shown the output "You Lost!"

If you manage to guess the correct word, you will be shown "Congratulations. You won the game!"

## File Structure

- hangman
  - milestone_2.py
  - milestone_3.py
  - milestone_4.py
  - milestone_5.py
- .gitignore
- readme 



## License Information
&nbsp; &nbsp; MIT Lincense
