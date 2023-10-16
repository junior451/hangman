import random

word_list = ["Apple", "Banana", "Orange", "Mango", "Kiwi"]

randomFruit = random.choice(word_list)

def check_guess(guessedLetter):
  guessedLetter = guessedLetter.lower()

  if guessedLetter in randomFruit.lower():
    print("Good guess! {guessedLetter} is in the word.")
  else:
    print("Sorry, {guessedLetter} is not in the word. Try again.")

def ask_for_input():
  while True:
    guessedLetter = input("Enter a letter to guess")

    if len(guessedLetter) == 1 and guessedLetter.isalpha():
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")

  check_guess(guessedLetter)    

ask_for_input()