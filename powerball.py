#!/usr/bin/env python3

# base version for github

import random
import time
import datetime
import sys

def generate_powerball_numbers():
    white_balls = random.sample(range(1, 70), 5)
    powerball = random.randint(1, 26)
    return white_balls, powerball

def check_ticket(ticket, winning_numbers):
    white_matches = len(set(ticket[0]) & set(winning_numbers[0]))
    powerball_match = (ticket[1] == winning_numbers[1])
    
    if white_matches == 5 and powerball_match:
        return "Jackpot"
    elif white_matches == 5:
        return "Match 5 white balls"
    elif white_matches == 4 and powerball_match:
        return "Match 4 white balls + Powerball"
    elif white_matches == 4:
        return "Match 4 white balls"
    elif white_matches == 3 and powerball_match:
        return "Match 3 white balls + Powerball"
    elif white_matches == 3:
        return "Match 3 white balls"
    elif white_matches == 2 and powerball_match:
        return "Match 2 white balls + Powerball"
    elif white_matches == 1 and powerball_match:
        return "Match 1 white ball + Powerball"
    elif powerball_match:
        return "Match Powerball"
    else:
        return "No win"

def simulate_lottery(draw_time_seconds, user_numbers):
    wins = {
      "Jackpot": 0,
      "Match 5 white balls": 0,
      "Match 4 white balls + Powerball": 0,
      "Match 4 white balls": 0,
      "Match 3 white balls + Powerball": 0,
      "Match 3 white balls": 0,
      "Match 2 white balls + Powerball": 0,
      "Match 1 white ball + Powerball": 0,
      "Match Powerball": 0
    }
    running_totals = {
      "Jackpot": 0,
      "Match 5 white balls": 0,
      "Match 4 white balls + Powerball": 0,
      "Match 4 white balls": 0,
      "Match 3 white balls + Powerball": 0,
      "Match 3 white balls": 0,
      "Match 2 white balls + Powerball": 0,
      "Match 1 white ball + Powerball": 0,
      "Match Powerball": 0,
      "No win": 0
    }
    prizes = {
      "Jackpot": 1000000000,
      "Match 5 white balls": 1000000,
      "Match 4 white balls + Powerball": 50000,
      "Match 4 white balls": 100,
      "Match 3 white balls + Powerball": 100,
      "Match 3 white balls": 7,
      "Match 2 white balls + Powerball": 7,
      "Match 1 white ball + Powerball": 4,
      "Match Powerball": 4,
      "No win": 0
   }

    
    start_time = time.time()
    end_time = start_time + draw_time_seconds
    total_games = 0 
   
    if draw_time_seconds > 0:
        while time.time() < end_time:
            winning_numbers = generate_powerball_numbers()
        
            #print(f"Winning Numbers: {winning_numbers[0]} Powerball: {winning_numbers[1]}")
            total_games += 1 
            result = check_ticket(user_numbers, winning_numbers)
            # print(f"You have {result}")
            if total_games%100000 == 0:
                 print(f'{total_games:,}')      
            if result in wins:
                 wins[result] += 1
                 running_totals[result] += prizes[result]
    
    elif draw_time_seconds == 0:
        while wins["Jackpot"] == 0:
            winning_numbers = generate_powerball_numbers()

            # print(f"Winning Numbers: {winning_numbers[0]} Powerball: {winning_numbers[1]}")
            total_games += 1
            result = check_ticket(user_numbers, winning_numbers)
            # print(f"You have {result}")
            if total_games%100000 == 0:
                 print(f'{total_games:,}')
            if result in wins:
                 wins[result] += 1
                 running_totals[result] += prizes[result]

    finish_time = time.time() 
    if wins["Jackpot"] > 0:
        print("YOU WAVE WON THE JACKPOT!\n\n") 
    formatted_total_games = f'{total_games:,}' 
    print("\nSimulation complete. Results:")
    print(f"Your numbers were {user_numbers[0]} and PB {user_numbers[1]}")
    print("Simulated ",formatted_total_games," drawings\n")
    print("If you had played these numbers in this many real drawings, you would have had to play for",round(total_games/(54*3),2),"years!")
    grand_total = 0
    overall_wins = 0
    print("\nHere are your results:\n")
    for category, count in wins.items():

        #print(f"{category} wins:", count, prizes[category],"   Your total winnings $", running_totals[category], "!!!")
        print(f"{category} payout: $", f'{prizes[category]:,}',"                   Your total wins:", count, "                      Your total earnings $", f'{running_totals[category]:,}')
        grand_total += running_totals[category]
        overall_wins += count

    print("\nYou spent $",f'{total_games*2:,}'," in order to win $", f'{grand_total:,}', ".")
    print("\nYou won a prize in", f'{overall_wins:,}', "drawings out of", f'{total_games:,}', "drawings played.")
    ROI = round(grand_total/(total_games*2),8)
    print("Your return on investment was ", ROI, " of what you put in to play.")
    Win_percentage = round(overall_wins/total_games/100,6)
    print("Your percentage of drawings winning a price was", Win_percentage, "%.")
    print("\nStarted at",datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'))
    print("Finished at",datetime.datetime.fromtimestamp(finish_time).strftime('%Y-%m-%d %H:%M:%S'))
    # We try to figure out the elapsed time later 
    #elapsed_time = finish_time-start_time
    #print("Total elapsed runtime",datetime.datetime.fromtimestamp(elapsed_time).strftime('%H:%M:%S'))
 
# Get the user's picks
if __name__ == "__main__":
    user_numbers_input = input("Enter your Powerball numbers (1 - 69), then the Powerball (1 - 26): ")
    user_numbers = [int(num) for num in user_numbers_input.split()]

# Validating the numbers entered by the user
    pb_iterator = 0
    if len(user_numbers) != 6:                         # If more or less than 6 numbers given
        sys.exit("Invalid input, you need exactly six numbers to play.  Goodbye!")
    elif (user_numbers[5] > 26 or user_numbers[5] <= 0):        # If the powerball is out of the range used by the game
        sys.exit("Your powerball selecion ts out of range.  Read the directions next time!")
    elif len(user_numbers[0:4]) != len(set(user_numbers[0:4])):           # If duplicate numbers were entered for any of the 5 white balls, which is not possible on a PB ticket
        sys.exit("You have entered duplicate numbers in your five white picks.  This is not possible.")
    else:                                               # Last check - now iterate through the list and check to make sure all 5 picks are between 1 and 69
        while pb_iterator < 5:
            if ((user_numbers[pb_iterator] < 1) or (user_numbers[pb_iterator] > 69)):
                  sys.exit("One or more of your five numbers is out of range.  Read the directions next time!")     # Die program, die.
            pb_iterator += 1

# Run the drawing
    draw_time_seconds = int(input("Enter the length of time to simulate drawings in seconds. Enter 0 to run indefinitely until a jackpot win: "))
    simulate_lottery(draw_time_seconds, (user_numbers[:5], user_numbers[5]))

