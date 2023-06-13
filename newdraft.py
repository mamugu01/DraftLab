import csv
import numpy
# You may or may not want to use this package, or others like it
# this is just a starting point for you
from sklearn.linear_model import LinearRegression

# Read the player database into an array of dictionaries
players = []
with open('playerDB.csv', mode='r') as player_csv:
    player_reader = csv.DictReader(player_csv)
    line_count = 0
    for row in player_reader:
        players.append(dict(row))

# Read the draft database into an array of dictionaries
draftPicks = []
with open('draftDB.csv', mode='r') as draft_csv:
    draft_reader = csv.DictReader(draft_csv)
    line_count = 0
    for row in draft_reader:
        draftPicks.append(dict(row))


def getWS48(draftPicks, players):
    averages = numpy.zeros(60)
    number_points = numpy.zeros(60)
    pick_num = 0
    for player in draftPicks:
        pick_num = player["numberPickOverall"]
        name = player["namePlayer"]
        lst = []
        for item in players:
            if item["Player"] == name:
                lst.append(item)
        for item in lst:
            if name != "Damion James" and name != "JamesOn Curry" and int(pick_num) < 61:
                number_points[int(pick_num) - 1] +=1
                averages[int(pick_num) - 1] += float(item["WS/48"])
                if(int(item["Age"]) >= 26 and int(item["Age"]) <= 28):
                    averages[int(pick_num) - 1] += float(item["WS/48"])

    return averages, number_points





averages, number_points = getWS48(draftPicks, players)

# Get the draft picks to give/receive from the user
# You can assume that this input will be entered as expected
# DO NOT CHANGE THESE PROMPTS
print("\nSelect the picks to be traded away and the picks to be received in return.")
print("For each entry, provide 1 or more pick numbers from 1-60 as a comma-separated list.")
print("As an example, to trade the 1st, 3rd, and 25th pick you would enter: 1, 3, 25.\n")
give_str = input("Picks to give away: ")
receive_str = input("Picks to receive: ")


# Convert user input to an array of ints
give_picks = list(map(int, give_str.split(',')))
receive_picks = list(map(int, receive_str.split(',')))

success = True
if (len(give_picks) == 1) and (len(receive_picks) == 1):
    success = (give_picks[0] > receive_picks[0])
else:
    give_num = 0
    away_num = 0
    for i in give_picks:
        give_num += (averages[i - 1]/float(number_points[i - 1]))
    for j in receive_picks:
        away_num += (averages[j - 1]/float(number_points[j - 1]))

    success = give_num < away_num


# Success indicator that you will need to update based on your trade analysis




# YOUR SOLUTION GOES HERE



# Print feeback on trade
# DO NOT CHANGE THESE OUTPUT MESSAGES
if success:
    print("\nTrade result: Success! This trade receives more value than it gives away.\n")
    # Print additional metrics/reasoning here
else:
    print("\nTrade result: Don't do it! This trade gives away more value than it receives.\n")
    # Print additional metrics/reasoning here
