# This function take decision about input numbers nobility. 
def PrimeNumber(r):#r is user value.
    if not(r >= 2):
        print("Not Prime Number")
    if r == 2:
        print("Prime Number")
    if (r > 2):
        for i in range(2,r):
            if r % i == 0:#if r could divided by any pozitif number(excluding 1 and r) this loop finished.
                print("Not Prime Number")
                break
        if r % i != 0:#if upper loop couldn't finished by break function.This Number can divide only 1 and itself.
            print("Prime Number")
number = int(input("Number="))#int() is for switch input value string to int.
PrimeNumber(number)
