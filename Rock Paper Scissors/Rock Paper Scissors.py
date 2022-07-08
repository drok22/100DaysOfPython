# Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_should_continue = True
player_score = 0
cpu_score = 0

while game_should_continue == True:

    game_count = player_score + cpu_score + 1

    print("*** GAME " + str(game_count) + " BEST OF 3 ***")
    print("*** Score - Player: " + str(player_score) + " / CPU: " + str(cpu_score) + " ***")

    is_legal_choice = False
    player_choice = input("Rock, Paper, Scissors, Shoot! (choose Rock, Paper, or Scissors)\n")
    player_choice = player_choice.lower()

    while is_legal_choice == False:
        if(player_choice == "rock" or player_choice == "paper" or player_choice == "scissors"):
            is_legal_choice = True
        else:
            player_choice = input("Please make a valid choice between Rock, Paper, or Scissors\n")

    cpu_input = random.randint(0,2)
    cpu_choice = "";

    if(player_choice == "rock"):
        print("You chose: " + rock)
    if(player_choice == "paper"):
        print("You chose: " + paper)
    if(player_choice == "scissors"):
        print("You chose: " + scissors)

    if(cpu_input == 0):
        cpu_choice = "rock"
        print("CPU chose " + rock)
    elif(cpu_input == 1):
        cpu_choice = "paper"
        print("CPU chose " + paper)
    elif(cpu_input == 2):
        cpu_choice = "scissors"
        print("CPU chose " + scissors)

    if(player_choice == "rock"):
        if(cpu_choice == "rock"):
            print("Game is a tie!")
        elif(cpu_choice == "paper"):
            cpu_score += 1
            print("CPU Wins!")
        elif(cpu_choice == "scissors"):
            player_score += 1
            print("You Win!")
    elif(player_choice == "paper"):
        if(cpu_choice == "rock"):
            player_score += 1
            print("You Win!")
        elif(cpu_choice == "paper"):
            print("Game is a tie!")
        elif(cpu_choice == "scissors"):
            cpu_score += 1
            print("CPU Wins!")
    elif(player_choice == "scissors"):
        if(cpu_choice == "rock"):
            cpu_score += 1
            print("CPU Wins!")
        elif(cpu_choice == "paper"):
            player_score += 1
            print("You Win!")
        elif(cpu_choice == "scissors"):
            print("Game is a tie!")

    if(player_score > 1 or cpu_score > 1):
        if(player_score > cpu_score):
            print("Player wins the match!")
        else:
            print("CPU wins the match!")

        play_again = input("Play again? y or n\n")
        if(play_again.lower() == "n"):
            game_should_continue = False
        else:
            game_count = 0
            player_score = 0
            cpu_score = 0

    game_count += 1



