import random

def main():
  # Generate a random number
  secret_number = random.randint(1, 100)

  # Initialize the number of guesses
  guesses_left = 10

  # Play the game
  while guesses_left > 0:
    # Get the player's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Check the guess
    if guess < secret_number:
      print("Your guess is too low.")
      guesses_left -= 1
    elif guess > secret_number:
      print("Your guess is too high.")
      guesses_left -= 1
    else:
      print("You guessed it right!")
      break

  # Check if the game is over
  if guesses_left == 0:
    print("You ran out of guesses. The secret number was", secret_number)

if __name__ == "__main__":
  main()
  
