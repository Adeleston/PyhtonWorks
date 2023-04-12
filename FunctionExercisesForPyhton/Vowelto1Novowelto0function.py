#Function for detect vowels in one word 
def vowelfunction(a):
    vowel =["a","e","u","o","i","I","A","E","U","O"]
    c = []
    for i in a:
        if i in vowel:
            c.append("1")
        else:
            c.append("0")
    for i in c:
        print("{}".format(i),end="")
word = input("Please write a word\n")
vowelfunction(word)
            