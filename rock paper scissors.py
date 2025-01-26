# start of game, allows user to input a choice
answer = input("Choose rock, paper, or scissors     ")


if answer.lower() == "rock": #the three possible options the user can make, and the option that tells the user they lost
    print("I choose paper, so I win!")
elif answer.lower() == "paper":
    print("I choose scissors, so I win!")
elif answer.lower() == "scissors":
    print("I choose rock, so I win")
else:
    print("You suck at this") #in case the user doesnt put it in one of the options