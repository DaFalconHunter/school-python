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

player_username = "Bill"
player_password = "123"
# player_password = "42Th@nks-f0r_theF1sh"
username_input = ""
password_input = ""

while username_input != player_username and password_input != player_password:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
print("Username and password verified")

songs_list = music_quiz_game_songs.songs_and_artists
# print(songs_list)
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

# with os.scandir('Extended Programming Challenges/') as entries:
#     for entry in entries:
#         print(entry.name)

# player_scores = open(r"Extended Programming Challenges/player_scores.txt", "r", encoding="utf-8")

# print(player_scores.read())
# player_scores.close()

player_scores = open(r"Extended Programming Challenges/player_scores.txt", "a", encoding="utf-8")
curr_time = datetime.datetime.now()
time = f"{curr_time.hour + 1}:{curr_time.minute}:{curr_time.second} - {curr_time.day}/{curr_time.month}/{curr_time.year}"
score_entry = f"\n{player_username}:        {points} points        {time}"
player_scores.write(score_entry)
player_scores.close()

player_scores = open(r"Extended Programming Challenges/player_scores.txt", "r", encoding="utf-8")
print(player_scores.read())
player_scores.close()
