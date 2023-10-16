import random

word_list = ["Apple", "Banana", "Orange", "Mango", "Kiwi"]

randomFruit = random.choice(word_list)
print(randomFruit)

def check_guess(guess):
  guess = guess.lower()

  if guess in randomFruit.lower():
    print("Good guess! {guess} is in the word.")
  else:
    print("Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
  while True:
    guess = input("Enter a letter to guess")

    if len(guess) == 1 and guess.isalpha():
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")

  check_guess(guess)    

ask_for_input()