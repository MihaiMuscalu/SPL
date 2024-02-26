import random

def Add(n1,n2):
    return n1+n2

def Rand():
    return random.randrange(100,200)

def WordFromArray(Word):
    return Word[random.randrange(0,len(Word))]

List = ["s","a","223","oosd"]
print(WordFromArray(List))