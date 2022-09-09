print('Welcome to my Quick quiz')
playing = input('All set to test your GK skills?')
if playing.lower() != "yes":
    quit()
print("Okay,so let's begin!")
score = 0
answer = input("Which planet has the most moons?").lower()
if answer ==("saturn"):
    print('You got it correct! What a great start!')
    score += 1
else:
    print("oops! You got it wrong. Better luck next time")

answer = input("What country has won the most World Cups?").lower()
if answer ==("brazil"):
    print('You got it correct! What a great start!')
    score += 1
else:
    print("oops! You got it wrong. Better luck next time")

answer = input("What is hundredth millionth of a second called?").lower()
if answer ==("nanosecond"):
    print('You got it correct! ')
    score += 1
else:
    print("oops! You got it wrong. Better luck next time")

answer = input("'Impossible is nothing' is the tagline of which sportswear company?").lower()
if answer ==("adidas"):
    print('You got it correct!')
    score += 1
else:
    print("oops! You got it wrong. Better luck next time")

answer = input("What is the colour of octopus blood ?").lower()
if answer ==("blue"):
    print('You got it correct! ')
    score += 1
else:
    print("oops! You got it wrong. ")

print("You total score is",score)
print("You got ",str((score/5)*100) + "%.")