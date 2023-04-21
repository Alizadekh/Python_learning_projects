import random

action_list = ['rock','paper','scissors']

#set scores

computer_score = 0
player_score = 0

#Raunds
total_raunds = input("How many raund do you want to play? ")

#Raund counter

raund_counter = 0


#make loop

while True:

    raund_counter +=1
    print("Raund Number: ", raund_counter)

    #make computer choice
    computer_choice = random.choice(action_list)

    #make player choice
    player_choice= input("Choose your action: ")

    print("Computer: ",computer_choice)
    print("Player: ", player_choice)

    if computer_choice==player_choice:
        print("Tie, both player choose same actions")

    elif computer_choice=="paper":
        if player_choice=="rock":
            print("Winner is: Computer")
            computer_score += 1
        else:
            print("Winner is Player")
            player_score += 1
    elif computer_choice=="rock":
        if player_choice=="paper":
            print("Winner is player")
            player_score += 1
        else:
            print("Winner is computer")
            computer_score += 1
    elif computer_choice=="scissors":
        if player_choice=="paper":
            print("Winner is Computer")
            computer_score += 1
        else:
            print("Winner is Player")
            player_score += 1

    if raund_counter == int(total_raunds):
        break

if computer_score == player_score:
    print("tie, there is no winner ", computer_score , ":" , player_score )
elif computer_score > player_score:
    print("Computer won!", computer_score , ":" , player_score )
elif computer_score < player_score:
    print("Player won!", computer_score , ":" , player_score )
