# Computer Science Quiz

questions = [
    ["What is the term for services or storage accessible via the Internet?", "cloud"],
    ["What is the term for a network spanning a large geographical area?", "wan"],
    ["What is the form of wireless data transmission commonly used with headphones and smart watches?", "bluetooth"],
    ["What is the name of the network hardware which sends packets along the Internet from a sending to recipient IP address?", "router"],
    ["What is the term for a network spanning a small geographical area?", "lan"],
    ["Which type of address is the following: 6C-3D-11-89-FF-DC ?", "mac"],
    ["What is the term for a worldwide collection of interconnected networks?", "internet"],
    ["What is the name of the computer responsible for receiving and responding to network requests?", "server"],
    ["What is the term for the amount of data can be sent and received correctly on a network?", "bandwidth"]
]

print("All answers are one word answers, e.g. IP, vs IP address.")

points = 0
for i in range(len(questions)):
    response = input(f"Q{i+1}) {questions[i][0]} ").lower()
    response = response.join(response.split())
    if response == questions[i][1]:
        points += 3
        print(f"Correct answer 🎉!\nThe correct answer was indeed {questions[i][1]}.\n3 points awarded ✅✅✅\n")
    else:
        points -= 1
        print(f"You daft fool 🤦! The correct answer was {questions[i][1]}.\n1 point deducted ❌\nGet educated dood\n")

print(f"Your score: {points} points")
