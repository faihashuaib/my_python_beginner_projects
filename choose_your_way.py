name = input('Type your name:')
print('Welcome ', name, 'to the adventure ')
answer = input(
     "You are alone in a road and feel very hungry. "
     "All you can see is a way to a not so dangerous forest and a road to your least favourite high school teacher's house. "
    " What will you choose? forest/ teacher's house "
 ).lower()
if answer == "forest":
     q2 = input("After entering the forest,you find a basket with apples with no one nearby. Will you eat it? yes/no").lower()
     if q2 =="yes":
         print ('That act is like stealing.You lose!')
     else:
         print('You die with hunger and lose!')
elif answer == "teacher's house":
     q2 = input("You reach your teacher's house and find the door open.You ring the bell but get no response."
                "Your hunger level has also risen to the top."
                "Will you leave?"
                " Or will you enter the house since the door is open? "
                "leave/ enter ").lower()
     if q2 == "leave":
         print('You find no other place to get food and starve to death .You lose!')
     else:
         q3= input(" You enter the house. You find a kid who has a piece of bread in his hand.You ask him politely to give you some bread"
                   " The kid gives a no to your request. Will you grab it from the kid and run away or wait for your teacher to show up to seek help "
                   " grab/wait ").lower()
         if q3 == "grab":
             print('The kid starts crying.You eat the bread without realizing it was poisoned by the maid to kill the child '
                   'You die.You lose!')
         else:
             q4 = input('You wait and see your teacher coming. You felt so happy and relieved and desperately asks for food '
                   "Then the teacher asks you the quadratic formula which you didn't answer in school "
                   "You forgot the formula. "
                    "Will you burst out or politely tell her you forgot? burst/polite")
             if q4 == "burst":
                 print('You burst out and fall from bed .You realize it was all a dream. You win! ')
             else:
                 print("Your polite words didn't seem to impress her or have some sympathy for you.You starve and die! ")


else:
    print('Not a valid answer.You lose!')

