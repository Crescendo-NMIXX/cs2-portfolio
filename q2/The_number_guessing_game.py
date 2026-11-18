attempts = 0
secret = 7

while True:
  guess = int(input("Please enter a number to guess: "))
   attempts += 1
  if guess < secret:
      guess = int(input("Please enter a number to guess: "))
  elif guess > secret:
      guess = int(input("Please enter a number to guess: "))
  else:
      break
    
print("you guessed it right!!")
print("Number of attempts made: ", attempts)
