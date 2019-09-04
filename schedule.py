import itertools

teams = [
    "Flynnsanity"

    ]

def rotate(l, n):
    return l[n:] + l[:n]

# generate the order, there are 13 weeks total, and we just simply rotate
division1 = [1, 2, 3, 4, 5, 6]
division2 = [7, 8, 9, 10, 11, 12]
team_numbers = [1, 2, 3, 7, 8, 9, 4, 5, 6, 10, 11, 12]

week_numbers = team_numbers.copy()

current_week = 1
# everyone plays an out of division team once, except for 1 team twice - 6 games
# everyone plays divisional opponents for the remaining 7 games

# out of division games, and just replicate the last one twice
starting_opp_idx = 0
for ood_games in range(0, len(division1)+1):

    print("Week {} Schedule: ".format(current_week))
    print('=============================')

    for div_idx in range(0, len(division1)):
        div_idx_opp = (div_idx + starting_opp_idx) % len(division1)
        print("Team {} vs. Team {}".format(division1[div_idx], division2[div_idx_opp]))

    starting_opp_idx += 1
    current_week += 1
    print("")

div1 = division1.copy()
div2 = division2.copy()

games_div1 = list(itertools.combinations(div1, 2))
games_div2 = list(itertools.combinations(div2, 2))
print("Games Div1: {} ".format(games_div1))
print("Games Div2: {} ".format(games_div2))

print("")
print("Week {} Schedule: ".format(current_week))
print('=============================')
current_week += 1

print("Team {} vs. Team {}".format(games_div1[0][0], games_div1[0][1]))
print("Team {} vs. Team {}".format(games_div1[9][0], games_div1[9][1]))
print("Team {} vs. Team {}".format(games_div1[14][0], games_div1[14][1]))
print("Team {} vs. Team {}".format(games_div2[0][0], games_div2[0][1]))
print("Team {} vs. Team {}".format(games_div2[9][0], games_div2[9][1]))
print("Team {} vs. Team {}".format(games_div2[14][0], games_div2[14][1]))

print("")
print("Week {} Schedule: ".format(current_week))
print('=============================')
current_week += 1

print("Team {} vs. Team {}".format(games_div1[1][0], games_div1[1][1]))
print("Team {} vs. Team {}".format(games_div1[7][0], games_div1[7][1]))
print("Team {} vs. Team {}".format(games_div1[13][0], games_div1[13][1]))
print("Team {} vs. Team {}".format(games_div2[1][0], games_div2[1][1]))
print("Team {} vs. Team {}".format(games_div2[7][0], games_div2[7][1]))
print("Team {} vs. Team {}".format(games_div2[13][0], games_div2[13][1]))

print("")
print("Week {} Schedule: ".format(current_week))
print('=============================')
current_week += 1

print("Team {} vs. Team {}".format(games_div1[2][0], games_div1[2][1]))
print("Team {} vs. Team {}".format(games_div1[8][0], games_div1[8][1]))
print("Team {} vs. Team {}".format(games_div1[10][0], games_div1[10][1]))
print("Team {} vs. Team {}".format(games_div2[2][0], games_div2[2][1]))
print("Team {} vs. Team {}".format(games_div2[8][0], games_div2[8][1]))
print("Team {} vs. Team {}".format(games_div2[10][0], games_div2[10][1]))

print("")
print("Week {} Schedule: ".format(current_week))
print('=============================')
current_week += 1

print("Team {} vs. Team {}".format(games_div1[3][0], games_div1[3][1]))
print("Team {} vs. Team {}".format(games_div1[6][0], games_div1[6][1]))
print("Team {} vs. Team {}".format(games_div1[9][0], games_div1[11][1]))
print("Team {} vs. Team {}".format(games_div2[3][0], games_div2[3][1]))
print("Team {} vs. Team {}".format(games_div2[6][0], games_div2[6][1]))
print("Team {} vs. Team {}".format(games_div2[11][0], games_div2[11][1]))

print("")
print("Week {} Schedule: ".format(current_week))
print('=============================')
current_week += 1

print("Team {} vs. Team {}".format(games_div1[4][0], games_div1[4][1]))
print("Team {} vs. Team {}".format(games_div1[5][0], games_div1[5][1]))
print("Team {} vs. Team {}".format(games_div1[12][0], games_div1[12][1]))
print("Team {} vs. Team {}".format(games_div2[4][0], games_div2[4][1]))
print("Team {} vs. Team {}".format(games_div2[5][0], games_div2[5][1]))
print("Team {} vs. Team {}".format(games_div2[12][0], games_div2[12][1]))

print("")
print("Week {} Schedule: ".format(current_week))
print('=============================')
current_week += 1

print("Team {} vs. Team {}".format(games_div1[0][0], games_div1[0][1]))
print("Team {} vs. Team {}".format(games_div1[9][0], games_div1[9][1]))
print("Team {} vs. Team {}".format(games_div1[14][0], games_div1[14][1]))
print("Team {} vs. Team {}".format(games_div2[0][0], games_div2[0][1]))
print("Team {} vs. Team {}".format(games_div2[9][0], games_div2[9][1]))
print("Team {} vs. Team {}".format(games_div2[14][0], games_div2[14][1]))


