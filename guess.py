import random

while True:
    hidden = random.randrange(1, 201)
 
    guess = int(input("Please enter your guess: "))
 
    if guess == hidden:
        print("Hit!")
    elif guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    print(hidden)
    
    play_again = input("Try again? (y/n): ")
    if play_again.lower() != "y":
        print("Thank you for playing")
        break