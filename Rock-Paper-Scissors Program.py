#Rock-Paper-Scissors Program
import random


#Program Greeting
print("\n\nWelcome to the game of Rock-Paper-Scissors")

#Start Tournament
print("\n\nNew Tournament")

#Declaring default variables
Game = 1
user_wins = 0
npc_wins = 0
Tournament = 'y'

#Stop when user says 'n'
while Tournament == 'y':
    
    #Stop when either the user or computer has scored 2 points
    while not(user_wins >= 2) and not(npc_wins >= 2):

        #Display the number of the game
        print("\n\nGame", Game, ": ")

        #Get User's choice
        user_choice = int(input("\nMake a choice: 1-Rock, 2-Paper, 3-Scissors: "))
        #Prompt User to try again if his input was not 1, 2, or 3
        while (not(user_choice == 1) and not(user_choice == 2) and not(user_choice == 3)):
            print("Incorrect input. Try again.")
            user_choice = int(input("\nMake a choice: 1-Rock, 2-Paper, 3-Scissors: "))    

        #Get computer's random choice
        random_choice = int(random.uniform(1,100))  
        if 1 <= random_choice <= 33:    #Computer chooses rock if random number is less than 33
            npc_choice = 1
            print("\nThe computer's choice is: 1-Rock")
        if 33 < random_choice <= 66:    #Computer chooses paper if random number is between 33 and 66
            npc_choice = 2
            print("\nThe computer's choice is: 2-Paper")
        if 66 < random_choice <= 100:   #Computer chooses scissors if random number is greater than 66
            npc_choice = 3
            print("\nThe computer's choice is: 3-Scissors")

        #Determine winner
        #Scissors beat Paper, Rock beat Scissors, and Paper beats Rock.
        if user_choice == npc_choice:   #Game is a draw when both parties chose the same play
            print("\nThis game is a draw")
        if (user_choice == 3 and npc_choice == 2) or (user_choice == 1 and npc_choice == 3) or (user_choice == 2 and npc_choice == 1): #Three ways for User to win
            user_wins += 1
            print("\nYou win!")
        if (npc_choice == 3 and user_choice == 2) or  (npc_choice == 1 and user_choice == 3) or (npc_choice == 2 and user_choice == 1): #Three ways for Computer to win
            npc_wins += 1
            print("\nThe computer wins!")

        #Display Score
        print("\nScore: User", user_wins, "- Computer", npc_wins)
        Game +=1

        #Display Winner when either the User or Computer wins 2 games
        if user_wins >= 2:
            print("\nUSER is the WINNER!!!")
        if npc_wins >= 2:
            print("\nCOMPUTER is the WINNER!!!")

    #Ask User to continue into another tournament or end the program 
    Tournament = input("\nDo you want to play another tournament? (y/n): ")
    #Prompt User to try again if his input was not the letter y or n.
    while not(Tournament == 'y') and not(Tournament == 'n'):
        print("Incorrect input. Try again.")
        Tournament = input("\nDo you want to play another tournament? (y/n): ")
    #Reset default variables if user wants to continue into another tournament 
    if Tournament == 'y':
        print("\n\nNew Tournament")
        user_wins = 0
        npc_wins = 0
        Game = 1
    #End program if player does not want to continue
    if Tournament == 'n':
        print("Have a great day!")
    

        
