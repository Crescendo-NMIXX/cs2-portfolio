secret = 7
guess = int(input("Please enter a number to guess: "))

while secret != guess:
    if guess < secret:
        print("Too low")
        guess = int(input("Please enter a number to guess: "))
    elif guess > secret:
        print("Too high!")
        guess = int(input("Please enter a number to guess: "))
    else:
        break
print("you guessed it right!!")
