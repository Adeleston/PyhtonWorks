import random
import time
import os
RandomNumber = random.randint(1,10)
Guess_right = 0
while True:
    UserNumber = int(input("Guess one number in 1-10\n"))
    if UserNumber == RandomNumber:
        print("You guess is right")
        print("you win")
        time.sleep(5)
        os.system("cls")
        break
    elif (RandomNumber - UserNumber > 0 and RandomNumber - UserNumber < 4) or (UserNumber - RandomNumber > 0 and UserNumber -RandomNumber < 4):
        print("your guess is too close\nyour guess right is {}".format(3-Guess_right))
        Guess_right += 1
        time.sleep(3)
        os.system("cls")
    elif (RandomNumber - UserNumber > 0 and RandomNumber - UserNumber < 7) or (UserNumber - RandomNumber > 0 and UserNumber -RandomNumber < 7):
        print("your guess isn't close or far\nyour guess right is {}".format(3-Guess_right))
        Guess_right += 1
        time.sleep(3)
        os.system("cls")
    else:
        print("your guess is too far.\nyour guess right is {}".format(3-Guess_right))
        Guess_right += 1
        time.sleep(3)
        os.system("cls")
    if Guess_right == 4:
        print("you lost")
        time.sleep(10)
        os.system("cls")
        break
