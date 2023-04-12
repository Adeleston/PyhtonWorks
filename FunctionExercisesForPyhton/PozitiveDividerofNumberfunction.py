#This function is writing divisiors user's value.
def Numberdivisiors(x):
    divisiors = []
    for i in range(1,x+1):#also Number is number's divisior
        if x % i == 0:
            divisiors.append(i)#this add value to divisiors list.
    for i in divisiors:#I can also write this code with one for loop but I want to use list because I want to get return this values my work will be easy.
        print(i)
number = int(input("Number ="))
Numberdivisiors(number)
            