birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
def TurkishNumberWriter(x):
    birinci = x // 10
    ikinci = x % 10
    if birinci == 0 and ikinci == 0:
        print("sıfır")
    elif birinci < 10: 
        print(onlar[birinci]+" "+birler[ikinci])
    else:
        print("Not Two Digit Number")

number = int(input("Two Digit Number = "))
TurkishNumberWriter(number)