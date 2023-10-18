import random

class Hangman:
  def __init__(self, word_list, num_lives=5):
    self.__word = random.choice(word_list)
    self.__word_guessed = ['_'] * len(self.__word)
    self.num_letters = self.__word_guessed.count("_")
    self.num_lives = num_lives
    self.__word_list = word_list
    self.__list_of_guesses = []

  def __check_guess(self, guess):
    guess = guess.lower()

    if guess in self.__word:
      print(f"Good guess! {guess} is in the word.")

      for index, letter in enumerate(self.__word):
        if letter == guess and self.__word_guessed[index] == "_":
          self.__word_guessed[index] = letter
        else:
          next  

      self.num_letters = self.__word_guessed.count("_")
    else:
      self.num_lives -= 1
      print(f"Sorry, {guess} is not in the word. Try again.")
      print(f"You have {self.num_lives} lives left.")

    print(self.__word_guessed)

  def ask_for_input(self):
    guessed_letter = input("Enter a letter to guess")

    if len(guessed_letter) != 1 and guessed_letter.isalpha() == False:
      print("Invalid letter. Please, enter a single alphabetical character")
    elif guessed_letter in self.__list_of_guesses:
      print(f"You already tried {guessed_letter}")
    else:
      self.__check_guess(guessed_letter)
      self.__list_of_guesses.append(guessed_letter)

def play_game(word_list):
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

play_game(["apple", "orange"])

