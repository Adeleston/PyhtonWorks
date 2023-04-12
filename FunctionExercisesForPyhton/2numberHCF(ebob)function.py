#This Function determines hcf.
def hcffunction(x,y):
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
            hcf = i
    print("highest common factor ={}".format(hcf))#function finish
number1 = int(input("Number 1 ="))
number2 = int(input("Number 2 ="))
hcffunction(number1,number2)