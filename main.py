import random

user_input = input("Enter a choice of either Rock(R), Paper(P) or Scissor(S) using the initials:")

print("PLAYER:", user_input)
likely_choice = ["R", "P", "S"]
computers_randchoice = random.choice(likely_choice)
print("CPU:", computers_randchoice)

if user_input != likely_choice:
    print("Invalid choice")

#while True:

   
    if (user_input == "R") and (computers_randchoice == "P"):
        print("Paper beats Rock COMPUETR WINS")

    elif (user_input == "R") and (computers_randchoice == "S"):
        print("Rock beats Scissors USER WINS")

    elif (user_input == "P") and (computers_randchoice == "R"):
        print("Paper beats Rock USER WINS")

    elif (user_input == "P") and (computers_randchoice == "S"):
        print("Scissors beats Paper COMPUTER WINS")

    elif (user_input == "S") and (computers_randchoice == "R"):
        print("Rock beats Scissors COMPUTER WINS")

    elif (user_input == "S") and (computers_randchoice == "P"):
        print("Scissors beats Paper USER WINS")

    else:
         print("Its a TIE")
        


    
    #break