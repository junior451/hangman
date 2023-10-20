import random


class Hangman:
  '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    word_list: list
        List of words to be used in the game    
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
  
  def __init__(self, word_list, num_lives=5):
    self.__word = random.choice(word_list)
    self.__word_guessed = ['_'] * len(self.__word)
    self.num_letters = self.__word_guessed.count("_")
    self.num_lives = num_lives
    self.__word_list = word_list
    self.__list_of_guesses = []

  def __check_guess(self, guess):
    '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked
    '''

    guess = guess.lower()

    if guess in self.__word:
      print(f"Good guess! {guess} is in the word.")

      for index, letter in enumerate(self.__word):
        if letter == guess and self.__word_guessed[index] == "_":
          self.__word_guessed[index] = guess

      self.num_letters = self.__word_guessed.count("_")
    else:
      self.num_lives -= 1
      print(f"Sorry, {guess} is not in the word. Try again.")
      print(f"You have {self.num_lives} lives left.")

    print(self.__word_guessed)

  def ask_for_input(self):
    '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
    '''

    guessed_letter = input("Enter a letter to guess")

    if len(guessed_letter) != 1 or guessed_letter.isalpha() == False: # this ensures the user input is a single character
      print("Invalid letter. Please, enter a single alphabetical character")
    elif guessed_letter.lower() in self.__list_of_guesses:
      print(f"You already tried {guessed_letter.lower()}")
    else:
      self.__check_guess(guessed_letter)
      self.__list_of_guesses.append(guessed_letter.lower())

def play_game(word_list):
  '''
  Main function to play the game

  Args:
    word_list: List of words which a random will be chosen for user to guess
  '''

  num_lives = 5
  game = Hangman(word_list, num_lives)

  while True:
    if game.num_lives == 0:
      print("You Lost!")
      break
    elif game.num_letters == 0:
      print("Congratulations. You won the game!")  
      break
    elif game.num_lives > 0:
      game.ask_for_input()

if __name__ == "__main__":
  play_game(["apple", "orange"])