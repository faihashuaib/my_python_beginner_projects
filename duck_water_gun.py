import random

user_wins = 0
computer_wins = 0
options = ["duck", "water", "gun"]
while True:
    user_input = input('Type Duck/Water/Gun or Q to quit the game : ').lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_numb = random.randint(0, 2)
    #Duck:0,Water:1,Gun:2
    computer_pick = options[random_numb]
    print("Computer picked", computer_pick + ".")
    if user_input == "gun" and computer_pick == "duck":
        print('You won!')
        user_wins += 1
        continue
    if user_input == "duck" and computer_pick == "water":
        print('You won!')
        user_wins += 1
        continue
    if user_input == "water" and computer_pick == "gun":
        print('You won!')
        user_wins += 1
        continue
    else:
        print('You lost')
        computer_wins += 1


if user_wins == 1:
    print("You won", user_wins, "time.")
else:
    print("You won", user_wins, "times.")
if computer_wins == 1:
    print("Computer won", computer_wins, "time.")
else:
    print("Computer won", computer_wins, "times.")
print("Goodbye")
