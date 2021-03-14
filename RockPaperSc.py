import random

while True:   #WHILE TRUE MEANS THAT IT LOOPS FOREVER/INDEFINITELY BUT SINCE THERE'S THE BREAK AT THE END, THE BREAK CUTS IT OFF 
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    #print("You chose {user_action}, computer chose {computer_action}.")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock > scissors! You win!")
        else:
            print("Paper > rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper > rock! You win!")
        else:
            print("Scissors > paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors > paper! You win!")
        else:
            print("Rock > scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Weak mental EZ Clap")
        break

#LEARN HOW THIS WORKS PROPERLY

#elif is just a contracted "else if" statement. 
#I.e., the first section saying that if the values are equal, print "it's a tie"
#And then the if/else statement under it, followed by another elif for the case of input being paper, scissors, etc. 

#if user_action == computer_action: 
    #print(f"both players selected {user_action}. It's a tie!")
                #^^ The above is the syntax for a tie in the RPS

#IF AND ELIF IS THE SAME AS JS IN THAT PICTURE BORDER LAB
#understand the "while True:" section 
#user_action, possible_actions, and computer_action is pretty self explanatory