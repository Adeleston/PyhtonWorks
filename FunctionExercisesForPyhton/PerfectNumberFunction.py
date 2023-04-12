def PerfectNumbersUntilNumber(x):
    for j in range(1,x):
        toplam = 0
        a = []
        for i in range(1,j):
            if j % i == 0:
                a.append(i)
        for i in a:
            toplam += i
        if toplam == j:
            print(j)
number = int(input("Number ="))
PerfectNumbersUntilNumber(number)