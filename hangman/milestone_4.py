import random

class Hangman:
  def __init__(self, word_list, num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = ['_'] * len(self.word)
    self.num_letters = self.word_guessed.count("_")
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  def check_guess(self, guess):
    guess = guess.lower()

    if guess in self.word:
      print("Good guess! {guess} is in the word.")

      for letter in self.word:
        index = self.word.index(letter)

        if letter == guess and self.word_guessed[index] == "_":
          self.word_guessed[index] = letter
        else:
          next

      self.num_letters = self.word_guessed.count("_")
    else:
      self.num_lives -= 1
      print("Sorry, {guessedLetter} is not in the word. Try again.")
      print(f"You have {self.num_lives} lives left.")

    print(self.word_guessed)

  def ask_for_input(self):
    while True:
      guessedLetter = input("Enter a letter to guess")

      if len(guessedLetter) != 1 and guessedLetter.isalpha() == False:
        print("Invalid letter. Please, enter a single alphabetical character")
      elif guessedLetter in self.list_of_guesses:
        print("You already tried that letter!")   
      else:
        self.check_guess(guessedLetter)
        self.list_of_guesses.append(guessedLetter)


Hangman(["apple", "orange"]).ask_for_input()

