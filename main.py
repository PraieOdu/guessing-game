
from art import logo
import random

def num_gen():     # Generate number
  global num_list
  for _ in range(1,101):
    num_list.append(_)
  return random.choice(num_list)
def diff(level):   # Select number of attempts based on difficulty
  if level == "easy":
    return 10
  elif level == "hard":
    return 5
  
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

num_list = []
attempts = 0
guessed_num = 0

ran_num = num_gen() #Assign generated number
level = input("Choose a difficulty. Easy or Hard: ").lower()
attempts = diff(level) # Assign num of attempts based on difficulty
print (f"You have {attempts} attempts remaining to guess the number")


while not guessed_num == ran_num and attempts > 0:
  guessed_num = int(input("Guess a number: "))
  
  if guessed_num < ran_num:
    print("Too Low")
    print("Guess again")
    attempts = attempts - 1
    print(f"You have {attempts} attempts remaining to guess the number")
  elif guessed_num > ran_num:
    print("Too High")
    print("Guess again")
    attempts = attempts - 1
    print(f"You have {attempts} attempts remaining to guess the number")
  elif guessed_num == ran_num:
    print(f"You got it! The answer was {guessed_num}")



if attempts == 0:
  print("Ran out of attempts. Game over")