#this function calculate lcm.
def LCMfunction(x,y):
    number1divisiors = []
    number2divisiors = []
    for i in range(1,x+1):
        if x % i == 0:
            number1divisiors.append(i)
    for i in range(1,y+1):
        if y % i == 0:
            number2divisiors.append(i)
    for i in number1divisiors:
        if i in number2divisiors:
            hcf = i#We need determine to hcf for calculating lcm.
    LCM =int( hcf * (x / hcf) * (y / hcf))#Lcm = hcf x (number1/hcf) x (number2/hcf)
    print("Least Common Multiply ={}".format(LCM))#function finish
number1 = int(input("Number 1 ="))
number2 = int(input("Number 2 ="))
LCMfunction(number1,number2)
