import random

while True:
    hidden = random.randrange(1, 50)
 
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
        print("Dumb Bitch")
        break

#the same as RPS, there's the "play_again.lower() != "y":" 
#Just like RPS, there's the break if the input is not equal to "y" and it will print out "Thank you for playing"

