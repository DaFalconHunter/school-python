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
1.	✔ Allows a player to enter their details, which are then authenticated to ensure that they are an authorised player.
2.	✔ Stores a list of song names and artists in an external file.
3.	Selects a song from the file, displaying the artist and the first letter of each word of the song title.
4.	Allows the user up to two chances to guess the name of the song, stopping the game if they guess a song incorrectly on the second chance.
5.	If the guess is correct, add the points to the player's score depending on the number of guesses.
6.	Displays the number of points the player has when the game ends.
7.	Stores the name of the player and their score in an external file.
8.	Displays the score and player name of the top 5 winning scores from the external file.

"""

import music_quiz_game_songs

player_username = "Bob"
player_password = "468Th@nks-f0r_theF1sh"
username_input = 0
password_input = 0

"""
while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    if username_input == player_username and password_input == player_password:
        print("Username and password verified")
        break
    else:
        print("Incorrect username or password")
"""

songs_list = music_quiz_game_songs.songs_and_artists

for i in range(len(songs_list)):
    # Print artist:
    # print(songs_list[i][0] + f" {songs_list[i][1][0]}")
    artist = songs_list[i][0]
    # print(artist)
    song_split = songs_list[i][1].split()
    # print(song_split)
    song_split_1st_letters = [s[0] for s in songs_list[i][1].split()]
    song_join = "    ".join(song_split_1st_letters)
    print(f"{artist}   {song_join}")
    # song_split_1st_letters =
    # song_1st_letters = songs_list[i][1].split()[0]
    # print(artist, song_1st_letters)

    # for j in range(len(songs_list[i])):
    # print(songs_list[i][j])
