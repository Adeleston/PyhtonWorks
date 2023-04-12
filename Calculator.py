import math
print("Choose you process\n1=Addition 2=Extraction 3=Division 4=Multiplication\n5=Factorial 6=Squaring 7=Square root 8=Cubing\n9=Tangent 10=Cotangent 11=Sinus 12=Cosine \n13=Atangent 14=Acotangent 15=Asinus 16=Acosine \n17=Decimal Log 18=Decimal Exp 19=Euler Log 20=Euler Exp")
def Addition(a,b):
    return a+b
def Extraction(a,b):
    return a-b
def Division(a,b):
    return a/b
def Multiplication(a,b):
    return a*b
def Factorial(a):
    return math.factorial(a)
def Squaring(a):
    return a ** 2
def Square_Root(a):
    return a ** 0.5
def Cubing(a):
    return a ** 3
def Tangent(a):
    return math.tan(a)
def Cotangent(a):
    return 1/math.tan(a)
def Sinus(a):
    return math.sin(a)
def Cosine(a):
    return math.cos(a)
def aTangent(a):
    return math.tan(a)
def Acotangent(a):
    return 1/math.tan(a)
def aSinus(a):
    return math.sin(a)
def Acosine(a):
    return math.cos(a)
def Log(a):
    return math.log10(a)
def Exp(a):
    return 10 ** a
def Euler_Log(a):
    return math.log1p(a)
def Euler_Exp(a):
    return math.exp(a)

def Calculator():
    Number1 = float(input("Number1 ="))
    while True:
        process = int(input("Choose process number"))
        if process in range(1,5):
            Number2 = float(input("Number2="))
            if process == 1:
                LastValue = Addition(Number1,Number2)
            if process == 2:
                LastValue = Extraction(Number1,Number2)
            if process == 3:
                LastValue = Division(Number1,Number2)
            if process == 4:
                Multiplication(Number1,Number2)
        elif process in range(5,20):
            if process == 5:
                LastValue = Factorial(Number1)
            if process == 6:
                LastValue = Squaring(Number1)
            if process == 7:
                LastValue = Square_Root(Number1)
            if process == 8:
                LastValue = Cubing(Number1)
            if process == 9:
                LastValue = Tangent(Number1)
            if process == 10:
                LastValue = Cotangent(Number1)
            if process == 11:
                LastValue = Sinus(Number1)
            if process == 12:
                LastValue = Cosine(Number1)
            if process == 13:
                LastValue = aTangent(Number1)
            if process == 14:
                LastValue = Acotangent(Number1)
            if process == 15:
                LastValue = aSinus(Number1)
            if process == 16:
                LastValue = Acosine(Number1)
            if process == 17:
                LastValue = Log(Number1)
            if process == 18:
                LastValue = Exp(Number1)
            if process == 19:
                LastValue = Euler_Log(Number1)
            if process == 20:
                LastValue = Euler_Exp(Number1)
        decision = input("Do you want to continue calculating with your value ?")
        if decision.upper() == "YES":
            break
        else:
            Number1 = LastValue
    return LastValue
print(Calculator())

        