"""
BRIEF:

Noel is creating a music quiz game. 
The game stores a list of song names and their artist (e.g. the band or solo artist name). 
The player needs to try and guess the song name. 
The game is played as follows:
•	A random song name and artist are chosen.
•	The artist and the first letter of each word in the song title are displayed.
•	The user has two chances to guess the name of the song.
•	If the user guesses the answer correctly the first time, they score 3 points.
•	If the user guesses the answer correctly the second time, they score 1 point. The game repeats.
•	The game ends when a player guesses the song name incorrectly the second time. 

Only authorised players can play the game. 
Where appropriate, input from the user should be validated. 
Design, write, test and refine a system that:
1.	✔ Allows a player to enter their details, which are then authenticated to ensure that they are
    an authorised player.
2.	✔ Stores a list of song names and artists in an external file.
3.	✔ Selects a song from the file, displaying the artist and the first letter of each word of the
    song title.
4.	✔ Allows the user up to two chances to guess the name of the song, stopping the game if they
    guess a song incorrectly on the second chance.
5.	✔ If the guess is correct, add the points to the player's score depending on the number of
    guesses.
6.	✔ Displays the number of points the player has when the game ends.
7.	✔ Stores the name of the player and their score in an external file.
8.	Displays the score and player name of the top 5 winning scores from the external file.

"""

# import os
import datetime
import music_quiz_game_songs

player_username = "1"
player_password = "1"
# player_password = "42Th@nks-f0r_theF1sh"
username_input = ""
password_input = ""

while username_input != player_username and password_input != player_password:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
print("Username and password verified")

songs_list = music_quiz_game_songs.songs_and_artists
# print(songs_list)
"""
questions = []
for i in range(len(songs_list)):
    # Print artist:
    # print(songs_list[i][0] + f" {songs_list[i][1][0]}")
    artist = songs_list[i][0]
    # print(artist)
    song_split = songs_list[i][1]
    # print(song_split)
    song_split_1st_letters = [ s[0] for s in songs_list[i][1].split() ]
    song_join = "    ".join(song_split_1st_letters)
    questions.extend([[f"{artist}: ", f"{song_join}    "]])
    # print(f"{artist}   {song_join}    ")
    # song_split_1st_letters =
    # song_1st_letters = songs_list[i][1].split()[0]
    # print(artist, song_1st_letters)

    # for j in range(len(songs_list[i])):
        # print(songs_list[i][j])
# print(questions)
points = 0
for i in range(len(questions)):
    print(questions[i][0] + questions[i][1])
    chances = 2
    while chances > 0:
        song_name = "".join(songs_list[i][1].lower())
        # print(song_name)
        response = input("Enter the artist's song: ").lower()
        response = "".join(response)
        # print(response)
        if response == song_name:
            print("Well done!")
            if chances == 2:
                points += 3
                print("You earned 3 points!")
            elif chances == 1:
                points += 1
                print("You earned 1 point.")
            break
        else:
            print("Uncultured fool, ya failiyer!")
            chances -= 1
    if chances == 0:
        print("Get cultured, dood")
        break

print(f"Your score: {points} points")
"""
# with os.scandir('Extended Programming Challenges/') as entries:
#     for entry in entries:
#         print(entry.name)

# player_scores = open(r"Extended Programming Challenges/player_scores.txt", "r", encoding="utf-8")

# print(player_scores.read())
# player_scores.close()

"""
# Writing to Scores file with username, score and time/date
player_scores = open(r"Extended Programming Challenges/player_scores.txt", "a", encoding="utf-8")
curr_time = datetime.datetime.now()
time = f"{curr_time.hour + 1}:{curr_time.minute}:{curr_time.second} - {curr_time.day}/{curr_time.month}/{curr_time.year}"
score_entry = f"\n{player_username}:        {points} points        {time}"
player_scores.write(score_entry)
player_scores.close()

player_scores = open(r"Extended Programming Challenges/player_scores.txt", "r", encoding="utf-8")
print(player_scores.read())
player_scores.close()
"""

# Retrieve content from player_scores.txt excluding 1st line:
player_scores = open(r"Extended Programming Challenges/player_scores.txt", "r", encoding="utf-8")
content = player_scores.readlines()
scores = content[1:]
print(scores)
player_scores.close()

# Split scores entries by whitespace to get a 2D array of
# player names, scores and times:
scores_split = []
for score_line in scores:
    scores_split.append(score_line.split())
    # Print each entry line of the scores file:
    print(score_line)

print(scores_split)

# Cast score ONLY from string to integer:
score_inted = []
for score_line in scores_split:
    inted_line = []

    for score_item in score_line:
        if score_line.index(score_item) == 1:
            print(score_item)
            inted_line.append(int(score_item))
            continue
        inted_line.append(score_item)

    score_inted.append(inted_line)

# Order scores from highest to lowest:
score_inted = sorted(score_inted, key=lambda score: -score[1])
print(score_inted)

# Re-string the scores:
score_stringed = []
for score_line in score_inted:
    stringed_line = []

    for score_item in score_line:
        if score_line.index(score_item) == 1:
            print(score_item)
            stringed_line.append(str(score_item))
            continue
        stringed_line.append(score_item)

    score_stringed.append(stringed_line)

print(score_stringed)

# Select each part of the line into separate variables for reformatting.
score_reformat = []
username = 0
score = 0
points = 0
time = 0
dash = 0
date = 0
for score_line in score_stringed:
    reformatted_line = []
    for score_item in score_line:
        reformatted_line = ""

        # Variables:
        match score_line.index(score_item):
            case 0:
                username = score_item
            case 1:
                score = score_item
            case 2:
                points = score_item
            case 3:
                time = score_item
            case 4:
                dash = score_item
            case 5:
                date = score_item
        
        reformatted_line = f"{username}        {score} {points}        {time} {dash} {date}"

    score_reformat.append(reformatted_line)

print(score_reformat)

# Rejoin scores:
scores_joined = []

scores_joined = "\n".join(score_reformat)
print(scores_joined)

# Rewrite to player_scores.txt
# print(f"PLAYER-------SCORE------------TIME\n{scores_joined}")
player_scores = open(r"Extended Programming Challenges/player_scores.txt", "w", encoding="utf-8")
player_scores.write(f"PLAYER-------SCORE------------TIME\n{scores_joined}")
player_scores.close()

# Read scores from player_scores.txt
player_scores = open(r"Extended Programming Challenges/player_scores.txt", "r", encoding="utf-8")
lines = player_scores.readlines()

# Output top 5 winning scores - have to join lines back together again here:
print("These are the top 5 winning scores!")
scores_joined = []
scores_joined = "".join(lines[0:6])
print(scores_joined)
player_scores.close()
